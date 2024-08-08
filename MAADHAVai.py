import pyttsx3
import speech_recognition as sr  
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishME():
     hour = int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
        speak("Good morning Sir!")

     elif hour>=12 and hour<18:
        speak("Good afternoon Sir!")

     else:
         speak("Good Evening Sir!")


     speak("I am Madhav your virtual assistant. How may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 0.8
        try:
            audio = r.listen(source)
        except Exception as e:
            print(f"Error: {str(e)}")
            speak("I encountered a problem with the microphone.")
            return "None"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        speak("Sorry, I did not understand that. Please say that again.")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        speak("I am unable to reach the recognition service at the moment.")
        return "None"

    return query


if __name__ == '__main__':

     wishME()
     if 1:
        
        query = takeCommand().lower()
        if 'wikipedia' in query:
          speak("Searching wikipedia...")
          query = query.replace("wikipedia", "")
          results = wikipedia.summary(query, sentences=3)
          speak("According to wikipedia")
          print(results)
          speak(results)
        elif 'open youtube' in query:
          webbrowser.open("youtube.com")

        elif 'open google' in query:
          webbrowser.open("google.com")

        elif 'open amazon' in query:
           webbrowser.open("amazon.com")

        elif 'open apple' in query:
            webbrowser.open("apple.com")
        

        elif 'play music' in query:
            webbrowser.open("spotify.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%m:%S")
            speak(f"Sir The time is {strTime}")
        elif 'open code' in query:
            codepath = "C:\\Users\\Harsh Singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'joke' in query:      
          speak(pyjokes.get_joke())

        elif 'how are you' in query:
            speak("I am fine sir, Do you need any help")

        elif 'are you single' in query:
          speak("No sir, I am in a relationship with wifi")

        elif 'play' in query:
          song = query.replace('play','')
          speak('playing'+ song)
          pywhatkit.playonyt(song)

        elif 'thank you' in query:
            speak("you're welcome sir. is there anything else")

        elif 'who is your developer' in query:
          speak("My developer is Utkarsh Singh")

        elif 'stop' in query:
           exit()

       
