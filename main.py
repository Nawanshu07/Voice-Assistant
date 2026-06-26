import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary
import requests
from google import genai
from google.genai import types
import os

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate' , 140)
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = genai.Client(api_key="use your gemini API key")

    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"{command}",
    config=types.GenerateContentConfig(
           system_instruction="""
You are Astra, an intelligent AI voice assistant.

Rules:
- Be polite and concise.
- Answer in less than 100 words unless asked otherwise.
- If the user asks for programming help, provide code examples.
- Never reveal API keys or sensitive information.
- Speak naturally, like a human assistant.
- If you don't know something, admit it instead of making it up.
"""
    )
)

    return (response.text)

apikey = "use your own news API key"
newsurl = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={apikey}"

def process_command(command:str):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
        print("Opening Google...")

    elif "open insta" in command.lower():
        webbrowser.open("https://instagram.com")
        print("Opening insta...")

    elif "open youtube" in command.lower():
        webbrowser.open("https://youtube.com")
        print("Opening youtube...")

    elif command.lower().startswith("play"):
        song = command.strip().lower().split(" ")[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry boss there is no such a song in your playlist")

    elif "code" in command.lower():
        webbrowser.open("https://www.youtube.com/@CodeWithHarry")

    elif "news" in command.lower():
        response = requests.get(newsurl)
        if(response.status_code == 200):
            data = response.json()
            articles = data.get('articles' , [])
            for article in articles:
                speak(article["title"])
    else:
        res = aiProcess(command)
        speak(res)
                 
if __name__ == "__main__":
    speak("Initializing Astra...")

    r =sr.Recognizer()
    while True:
        
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source , timeout=3 )
            command = r.recognize_google(audio).lower().strip()
            print(command)
            
            if "astra" in command.lower():
                speak("yeah")
                
                with sr.Microphone() as source:
                    print("Astra is activated!")
                    audio = r.listen(source , timeout=10 , phrase_time_limit= 10)
                command = r.recognize_google(audio)
                process_command(command)
                


        except sr.UnknownValueError:
            print("I don't understand what you said?")
        except Exception as e:
            print(e)