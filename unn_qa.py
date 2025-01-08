import pyttsx3
import speech_recognition as sr
from fuzzywuzzy import process
from py_avataaars import (
    PyAvataaar,
    AvatarStyle,
    SkinColor,
    TopType,
    HairColor,
    AccessoriesType,
    FacialHairType,
    ClotheType,
    Color,
    ClotheGraphicType,
    MouthType,
    EyesType,
    EyebrowType,
)
import cv2
import numpy as np
import threading

# Backend database (questions and answers)
qa_pairs = {
    "What is Python?": "Python is a high-level, interpreted programming language known for its simplicity and versatility.",
    "What is AI?": "AI, or Artificial Intelligence, refers to systems designed to perform tasks that typically require human intelligence.",
    "What is OpenCV?": "OpenCV is an open-source computer vision and machine learning library.",
    "How does speech recognition work?": "Speech recognition converts spoken language into text using algorithms and machine learning.",
}

# Text-to-speech setup
tts_engine = pyttsx3.init()
tts_engine.setProperty("rate", 180)

# Create avatar image
def create_avatar():
    avatar = PyAvataaar(
        style=AvatarStyle.CIRCLE,
        skin_color=SkinColor.LIGHT,
        top=TopType.SHORT_HAIR_SHORT_CURLY,
        hair_color=HairColor.BROWN,
        accessories=AccessoriesType.PRESCRIPTION_02,
        facial_hair=FacialHairType.BLANK,  # Corrected here
        clothing=ClotheType.GRAPHIC_SHIRT,
        clothing_color=Color.BLACK,
        graphic_type=ClotheGraphicType.BAT,
        mouth=MouthType.SMILE,
        eyes=EyesType.HAPPY,
        eyebrow=EyebrowType.DEFAULT,
    )
    avatar.render_png_file("avatar.png")
    return cv2.imread("avatar.png")

# Display avatar with animation
def show_avatar(text, speaking=False):
    avatar = create_avatar()
    canvas = np.zeros((600, 600, 3), dtype="uint8")
    canvas[:, :] = (255, 255, 255)

    # Resize and overlay avatar
    avatar = cv2.resize(avatar, (400, 400), interpolation=cv2.INTER_AREA)
    x_offset = (canvas.shape[1] - avatar.shape[1]) // 2
    y_offset = (canvas.shape[0] - avatar.shape[0]) // 4
    canvas[y_offset:y_offset + avatar.shape[0], x_offset:x_offset + avatar.shape[1]] = avatar

    # Add text below the avatar
    cv2.putText(canvas, text, (50, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    if speaking:
        for _ in range(3):  # Blinking "Speaking..." text
            temp_canvas = canvas.copy()
            cv2.putText(temp_canvas, "Speaking...", (50, 550), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            cv2.imshow("Avatar", temp_canvas)
            cv2.waitKey(500)  # Show speaking animation
            cv2.imshow("Avatar", canvas)
            cv2.waitKey(500)
    else:
        cv2.imshow("Avatar", canvas)

    cv2.waitKey(0)  # Wait until a key is pressed
    cv2.destroyWindow("Avatar")  # Destroy the window after closing

# Speech-to-text function
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your question...")
        try:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            question = recognizer.recognize_google(audio)
            return question
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."
        except sr.RequestError:
            return "Speech recognition service is unavailable. Please check your internet connection."

# Fetch answer from backend
def get_answer(user_question):
    best_match, match_score = process.extractOne(user_question, qa_pairs.keys())
    if match_score > 80:
        return qa_pairs[best_match]
    else:
        return "Sorry, I don't know the answer to that question."

# Speak text with avatar animation
def speak_text_with_avatar(text):
    def speak():
        tts_engine.say(text)
        tts_engine.runAndWait()

    speaking_thread = threading.Thread(target=speak)
    speaking_thread.start()
    show_avatar(text, speaking=True)
    speaking_thread.join()

# Main function
if __name__ == "__main__":
    print("Welcome to the voice-based Q&A system with avatar!")
    speak_text_with_avatar("Welcome! You can ask me questions now.")

    while True:
        user_question = recognize_speech()
        print(f"You asked: {user_question}")

        if user_question.lower() == "exit":
            print("Goodbye!")
            speak_text_with_avatar("Goodbye!")
            break

        answer = get_answer(user_question)
        print(f"Answer: {answer}")
        speak_text_with_avatar(answer)

    cv2.destroyAllWindows()
