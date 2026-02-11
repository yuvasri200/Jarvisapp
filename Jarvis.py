import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser


# ---------- SPEAK FUNCTION ----------
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


# ---------- TAKE VOICE COMMAND ----------
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")
        print("You said:", query)
        return query.lower()
    except:
        print("Did not understand")
        return ""


# ---------- START ----------
speak("Hello, I am Jarvis")

while True:
    command = take_command()
    command = command.replace(" ", "")
    print("Command:", command)

    if "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        speak("The time is " + time)

    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today is " + date)

    elif "wikipedia" in command:
        speak("Searching Wikipedia")
        command = command.replace("wikipedia", "")
        try:
            result = wikipedia.summary(command, sentences=2)
            speak(result)
        except:
            speak("No result found")

    elif "openyoutube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "opengoogle" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "openwhatsapp" in command:
        speak("Opening WhatsApp Web")
        webbrowser.open("https://web.whatsapp.com")

    elif "openchatgpt" in command:
        speak("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com")

    elif "whoareyou" in command:
        speak("I am Jarvis 🤖, your personal assistant.")

    elif "exit" in command:
        speak("Exiting Jarvis... Bye 👋")
        sys.exit()

     

