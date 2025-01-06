import speech_recognition as sr
from fuzzywuzzy import process
import pyttsx3

# Predefined questions and answers
qa_pairs = {
    "What is Python?": "Python is a high-level, interpreted programming language known for its simplicity and versatility.",
    "What is AI?": "AI, or Artificial Intelligence, refers to systems designed to perform tasks that typically require human intelligence.",
    "What is OpenCV?": "OpenCV is an open-source computer vision and machine learning library.",
    "How does speech recognition work?": "Speech recognition converts spoken language into text using algorithms and machine learning."
}

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()

def speak_text(text):
    """Speak the given text using pyttsx3."""
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to match user's question and provide an answer
def get_answer(user_question):
    # Find the best match from predefined questions
    best_match, match_score = process.extractOne(user_question, qa_pairs.keys())
    
    # Check if match is above the threshold
    if match_score > 80:  # Threshold for similarity
        return qa_pairs[best_match]
    else:
        return "Sorry, I don't have an answer to that question."

# Function to capture and transcribe speech
def recognize_speech():
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

# Main loop for the Q&A system
if __name__ == "__main__":
    print("Welcome to the voice-based Q&A system. Say 'exit' to quit.")
    speak_text("Welcome to the voice-based question and answer system. You can ask your questions now.")
    
    while True:
        user_question = recognize_speech()
        
        if user_question.lower() == "exit":
            print("Goodbye!")
            speak_text("Goodbye!")
            break
        
        print(f"You asked: {user_question}")
        
        if user_question.startswith("Sorry,"):
            print(user_question)  # Print error message if speech couldn't be understood
            speak_text(user_question)
        else:
            answer = get_answer(user_question)
            print(f"Answer: {answer}")
            speak_text(answer)
