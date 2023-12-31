import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening  sir!")

    
    speak("I am jarvis, How may I help you ")         

def takeCommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_treshold = 2
        audio = r.listen(source)

        try:
            print("recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")  

        except Exception as e:
           #print(e)
            print("Say that again please...")
            return "None"
        return query

    def sendmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('nilayandeb20@gmail.com', 'ByhW280%')
        server.sendmail('nilayandeb20@gmail.com', to, content)
        server.close()


if __name__ == "__main__":
   WishMe()
   # while true:
   if 1:
    query = takeCommand().lower()


    if 'wikipedia' in query:
        speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
            webbrowser.open("youtube.com")

    elif 'open google' in query:
            webbrowser.open("google.com") 

    elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
        
    elif 'open code' in query:
        codePath = "C:\\Users\\OMEN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'email to rock' in query:
        try:
            speak("what should i say?")
            content = takeCommand()
            to = "nilayandeb18@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("couldn't send email")

    elif 'open spotify' in query:
        spt = "C:\\Users\\OMEN\\AppData\\Roaming\\Spotify\\Spotify.exe" 
        os.startfile(spt) 

    elif 'how are you' in query:
        speak("I am good sir, how are you?")      
            
    elif 'open intelli j' in query:
        path = "C:\\Program Files\\JetBrains\\IntelliJ IDEA 2022.2.2\\bin\\idea64.exe"
        os.startfile(path)

     
    

   