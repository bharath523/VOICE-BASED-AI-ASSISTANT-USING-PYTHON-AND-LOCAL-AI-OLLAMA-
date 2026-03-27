import speech_recognition as sr
import pyttsx3
import time

# ---------- Speech Recognition ----------
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source, phrase_time_limit=6)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except:
        return ""


# ---------- Text To Speech (RESET ENGINE EACH TIME) ----------
def speak(text):
    if not text or not text.strip():
        return

    engine = pyttsx3.init()
    engine.setProperty("rate", 170)

    # split long text safely
    max_len = 180
    chunks = [text[i:i+max_len] for i in range(0, len(text), max_len)]

    for chunk in chunks:
        engine.say(chunk)
        engine.runAndWait()
        time.sleep(0.2)

    engine.stop()
