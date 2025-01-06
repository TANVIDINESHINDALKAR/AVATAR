import cv2
import numpy as np
import pyttsx3
import speech_recognition as sr
from fuzzywuzzy import process
import threading
import time

# Predefined questions and answers
qa_pairs = {
    "What is Python?": "Python is a high-level, interpreted programming language known for its simplicity and versatility.",
    "What is AI?": "AI, or Artificial Intelligence, refers to systems designed to perform tasks that typically require human intelligence.",
    "What is OpenCV?": "OpenCV is an open-source computer vision and machine learning library.",
    "How does speech recognition work?": "Speech recognition converts spoken language into text using algorithms and machine learning."
}

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()

def speak_text_in_segments(text, segment_duration=2):
    """Speaks the given text in segments and synchronizes with the avatar's mouth animation."""
    words = text.split()  # Split the text into words
    segments = [' '.join(words[i:i + segment_duration]) for i in range(0, len(words), segment_duration)]

    for segment in segments:
        # Speak each segment
        speak_text(segment)
        
        # Animate avatar's mouth while speaking the segment
        speaking_animation(segment)
        time.sleep(segment_duration)  # Wait for the segment duration before continuing

# Function to speak the text using pyttsx3
def speak_text(text):
    """Speak the given text using pyttsx3."""
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to match user's question and provide an answer
def get_answer(user_question):
    """Match user's question and provide an answer."""
    best_match, match_score = process.extractOne(user_question, qa_pairs.keys())
    if match_score > 80:  # Threshold for similarity
        return qa_pairs[best_match]
    else:
        return "Sorry, I don't have an answer to that question."

# Function to capture and transcribe speech
def recognize_speech():
    """Capture and transcribe speech."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your question...")
        try:
            recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
            audio = recognizer.listen(source)  # Capture audio
            print("Processing your question...")
            question = recognizer.recognize_google(audio)  # Convert speech to text
            return question
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand what you said. Please try again."
        except sr.RequestError:
            return "Speech recognition service is unavailable. Please check your internet connection."

# Load images
face = cv2.imread("face.png", cv2.IMREAD_UNCHANGED)
mouth_open = cv2.imread("mouth_open.png", cv2.IMREAD_UNCHANGED)
mouth_closed = cv2.imread("mouth_closed.png", cv2.IMREAD_UNCHANGED)

# Resize images
def resize_image(image, width, height):
    return cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)

# Initial avatar sizes
face = resize_image(face, 600, 600)
mouth_open = resize_image(mouth_open, 200, 100)
mouth_closed = resize_image(mouth_closed, 200, 100)

# Global variables
canvas = np.zeros((800, 800, 3), dtype="uint8")
canvas[:] = (255, 255, 255)  # White background
button_clicked = False  # Flag to detect button clicks

# Draw the static avatar (face + button)
def draw_avatar():
    global canvas
    canvas[:] = (255, 255, 255)  # Clear canvas
    # Draw face
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    # Draw button
    button_color = (0, 255, 0)  # Green
    cv2.rectangle(canvas, (300, 700), (500, 750), button_color, -1)
    cv2.putText(canvas, "Speak", (330, 735), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Mouse callback function to detect clicks
def on_mouse(event, x, y, flags, param):
    global button_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the button is clicked
        if 300 <= x <= 500 and 700 <= y <= 750:
            button_clicked = True

# Speaking animation for the avatar
def speaking_animation(message):
    face_x, face_y = 100, 50
    canvas[face_y:face_y+600, face_x:face_x+600] = face[:, :, :3]
    mouth_x, mouth_y = 250, 450

    for i in range(len(message.split())):  # Number of word movements
        # Mouth open
        canvas[mouth_y:mouth_y+100, mouth_x:mouth_x+200] = mouth_open[:, :, :3]
        cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow("Avatar", canvas)
        cv2.waitKey(300)  # Delay for mouth movement to simulate speech

        # Mouth closed
        canvas[mouth_y:mouth_y+100, mouth_x:mouth_x+200] = mouth_closed[:, :, :3]
        cv2.putText(canvas, message, (150, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow("Avatar", canvas)
        cv2.waitKey(300)

# Initialize avatar
draw_avatar()

# Set up mouse callback
cv2.namedWindow("Avatar")
cv2.setMouseCallback("Avatar", on_mouse)

# Main loop
while True:
    if button_clicked:
        user_question = recognize_speech()
        if user_question.startswith("Sorry,"):
            message = user_question
        elif user_question.lower() == "exit":
            message = "Goodbye!"
            speak_text(message)
            break
        else:
            print(f"You asked: {user_question}")
            message = get_answer(user_question)
            # Start the speech and avatar animation in sync
            threading.Thread(target=speak_text_in_segments, args=(message, 3)).start()
        
        button_clicked = False  # Reset button click

    # Show the canvas
    draw_avatar()
    cv2.imshow("Avatar", canvas)

    # Exit on 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
