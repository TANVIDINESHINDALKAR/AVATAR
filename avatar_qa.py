import speech_recognition as sr
from fuzzywuzzy import process
import pyttsx3
import cv2
import time
import numpy as np
import threading

qa_pairs = {
    "What is Python?": "Python is a high-level, interpreted programming language known for its simplicity and versatility.",
    "What is AI?": "AI, or Artificial Intelligence, refers to systems designed to perform tasks that typically require human intelligence.",
    "What is OpenCV?": "OpenCV is an open-source computer vision and machine learning library.",
    "How does speech recognition work?": "Speech recognition converts spoken language into text using algorithms and machine learning."
}


tts_engine = pyttsx3.init()
tts_engine.setProperty("rate", 200)   # Lower rate for slower speech


mouth_open_img = cv2.imread('mouth_open.png', cv2.IMREAD_UNCHANGED)  # Mouth open
mouth_closed_img = cv2.imread('mouth_closed.png', cv2.IMREAD_UNCHANGED)  # Mouth closed


is_speaking = threading.Event()


def resize_overlay(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)


def overlay_image(base_img, overlay_img, x, y):
    h, w = overlay_img.shape[:2]
    base_h, base_w = base_img.shape[:2]

    
    if y < 0: y = 0
    if x < 0: x = 0
    if y + h > base_h:
        h = base_h - y
        overlay_img = overlay_img[:h, :, :]
    if x + w > base_w:
        w = base_w - x
        overlay_img = overlay_img[:, :w, :]

    roi = base_img[y:y+h, x:x+w]

    if overlay_img.shape[2] == 4: 
        for c in range(3): 
            roi[:, :, c] = (
                overlay_img[:, :, c] * (overlay_img[:, :, 3] / 255.0) +
                roi[:, :, c] * (1.0 - overlay_img[:, :, 3] / 255.0)
            )
    else:  
        roi[:, :, :] = overlay_img

    base_img[y:y+h, x:x+w] = roi
    return base_img


def avatar_speaking():
    """Mimic speaking with the avatar while TTS is active."""
    
    mouth_width, mouth_height = 500, 250
    canvas_width, canvas_height = 800, 600
    canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)

  
    mouth_x = (canvas_width - mouth_width) // 2
    mouth_y = (canvas_height - mouth_height) // 2

    while is_speaking.is_set():
        for mouth_img in [mouth_open_img, mouth_closed_img]:
            if not is_speaking.is_set():
                break  # Stop animation if speaking ends

            resized_mouth = resize_overlay(mouth_img, mouth_width, mouth_height)
            speaking_face = canvas.copy()
            speaking_face = overlay_image(speaking_face, resized_mouth, mouth_x, mouth_y)
            cv2.imshow("Speaking Avatar", speaking_face)

            if cv2.waitKey(300) & 0xFF == ord('q'):  # Increased sleep time to slow down animation
                is_speaking.clear()
                cv2.destroyAllWindows()
                return

    cv2.destroyAllWindows()


def speak_text_with_avatar(text):
    """Speak the given text and animate the avatar's mouth."""

    is_speaking.set()


    threading.Thread(target=avatar_speaking, daemon=True).start()

    # Start text-to-speech
    tts_engine.say(text)
    tts_engine.runAndWait()

   
    is_speaking.clear()

def get_answer(user_question):
    best_match, match_score = process.extractOne(user_question, qa_pairs.keys())
    if match_score > 80:  
        return qa_pairs[best_match]
    else:
        return "Sorry, I don't have an answer to that question."


def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your question...")
        try:
            recognizer.adjust_for_ambient_noise(source) 
            audio = recognizer.listen(source)  
            print("Processing your question...")
            question = recognizer.recognize_google(audio)  
            return question
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand what you said. Please try again."
        except sr.RequestError:
            return "Speech recognition service is unavailable. Please check your internet connection."

if __name__ == "__main__":
    print("Welcome to the voice-based Q&A system with avatar. Say 'exit' to quit.")
    speak_text_with_avatar("Welcome to the voice-based Q&A system. You can ask your questions now.")
    
    while True:
        user_question = recognize_speech()
        
        if user_question.lower() == "exit":
            print("Goodbye!")
            speak_text_with_avatar("Goodbye!")
            break
        
        print(f"You asked: {user_question}")
        
        if user_question.startswith("Sorry,"):
            print(user_question)  # Print error message if speech couldn't be understood
            speak_text_with_avatar(user_question)
        else:
            answer = get_answer(user_question)
            print(f"Answer: {answer}")
            speak_text_with_avatar(answer)  
