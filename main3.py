import speech_recognition as sr
import pywhatkit

# Initialize the recognizer
r = sr.Recognizer()

with sr.Microphone() as source:
    
    r.adjust_for_ambient_noise(source)

    try:
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print(text)
        pywhatkit.playonyt(text)
        # ch = int(input("enter 1 for tutorial and 2 for song "))
    except sr.UnknownValueError:
            print("Could not understand audio")
