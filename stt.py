import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Say something...")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
    audio = recognizer.listen(source)

try:
    # Convert speech to text
    print("Recognizing speech...")
    text = recognizer.recognize_google(audio)
    print("You said: " + text)
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio")
except sr.RequestError:
    print("Sorry, the speech recognition service is unavailable")
