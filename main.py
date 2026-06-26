import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import wikipedia
import pyjokes

engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def wish():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am your AI Virtual Assistant. How can I help you?")

def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-IN")
        print("You said:", query)
        return query.lower()

    except Exception:
        speak("Sorry, I didn't understand. Please say that again.")
        return ""

def execute_command(query):

    if "open google" in query:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in query:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open gmail" in query:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    elif ("open chatgpt" in query or
        "open chat gpt" in query or
      "chatgpt" in query or
      "chat gpt" in query):
       speak("Opening ChatGPT")
       webbrowser.open("https://chatgpt.com")

    elif "open github" in query:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    elif "search" in query:
        search = query.replace("search", "").strip()
        speak(f"Searching for {search}")
        webbrowser.open(f"https://www.google.com/search?q={search}")

    elif "wikipedia" in query:
        topic = query.replace("wikipedia", "").strip()
        try:
            result = wikipedia.summary(topic, sentences=2)
            speak(result)
        except:
            speak("Sorry, I couldn't find information.")

    elif "time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif "date" in query:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}")

    elif "joke" in query:
        speak(pyjokes.get_joke())

    elif "how are you" in query:
        speak("I am fine. Thank you for asking.")

    elif "your name" in query:
        speak("My name is Jarvis.")

    elif "thank you" in query:
        speak("You're welcome.")

    elif "exit" in query or "stop" in query:
        speak("Goodbye. Have a nice day!")
        exit()

    else:
        speak("Sorry, I don't know that command.")

wish()

while True:
    command = take_command()

    if command != "":
        execute_command(command)