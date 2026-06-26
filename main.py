import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary
import requests


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate' , 140)
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

apikey = "34d829ec80d34dd49457d26ec3bb7ea4"
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