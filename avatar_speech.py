import os
from gtts import gTTS
from playsound import playsound
import tkinter as tk
from tkinter import PhotoImage

# Predefined questions and answers
qa_pairs = {
    "What is Python?": "Python is a high-level, interpreted programming language known for its simplicity and versatility.",
    "What is AI?": "AI, or Artificial Intelligence, refers to systems designed to perform tasks that typically require human intelligence.",
    "What is OpenCV?": "OpenCV is an open-source computer vision and machine learning library.",
    "How does speech recognition work?": "Speech recognition converts spoken language into text using algorithms and machine learning."
}

# Function to convert text to speech using gTTS
def speak_text(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    playsound("response.mp3")
    os.remove("response.mp3")

# Function to handle user questions
def handle_question():
    question = question_entry.get()
    answer = qa_pairs.get(question, "Sorry, I don't have an answer to that question.")
    
    # Display answer in the label
    answer_label.config(text=answer)
    
    # Avatar animation (basic)
    avatar_label.config(text="🤔 Speaking...")
    root.update()
    
    # Speak the answer
    speak_text(answer)
    
    # Reset avatar label
    avatar_label.config(text="🙂")

# Create the main window
root = tk.Tk()
root.title("Talking Avatar")
root.geometry("400x500")
root.resizable(False, False)

# Add avatar label
avatar_label = tk.Label(root, text="🙂", font=("Helvetica", 100))
avatar_label.pack(pady=20)

# Add question entry
question_label = tk.Label(root, text="Ask a question:", font=("Helvetica", 14))
question_label.pack(pady=10)

question_entry = tk.Entry(root, font=("Helvetica", 14), width=30)
question_entry.pack(pady=10)

# Add a submit button
submit_button = tk.Button(root, text="Submit", font=("Helvetica", 14), command=handle_question)
submit_button.pack(pady=20)

# Add answer label
answer_label = tk.Label(root, text="", font=("Helvetica", 14), wraplength=350, justify="center")
answer_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
