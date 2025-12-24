import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os

#Text-to-Speech
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice
engine.setProperty('rate', 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning! I am Jija.")
    elif hour < 18:
        speak("Good afternoon! I am Jija.")
    else:
        speak("Good evening! I am Jija.")
    speak("How can I help you?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("🧠 Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        speak("Sorry, I didn't understand. Please say again.")
        return ""

def play_youtube(song):
    speak(f"Playing {song} on YouTube")
    query = song.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

def run_assistant():
    greet()

    while True:
        command = take_command()

        if command == "":
            continue

        # Play song on YouTube
        if "play" in command and "youtube" in command:
            song = command.replace("play", "").replace("on youtube", "").strip()
            play_youtube(song)

        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "open chatgpt" in command:
            speak("Opening ChatGPT")
            webbrowser.open("https://chat.openai.com")

        elif "open whatsapp" in command:
            speak("Opening WhatsApp")
            webbrowser.open("https://web.whatsapp.com")

        elif "open chrome" in command:
            speak("Opening Google Chrome")
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time}")

        elif "date" in command:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {date}")

        elif "your name" in command:
            speak("My name is Jija. I am your AI assistant.")

        elif "hello" in command or "hi" in command:
            speak("Hello! How can I help you?")

        elif "bye" in command or "exit" in command or "stop" in command:
            speak("Goodbye! Have a nice day.")
            break

        else:
            speak("Sorry, I can't do that yet.")
run_assistant()
