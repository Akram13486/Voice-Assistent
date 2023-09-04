import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else :
        speak("Good Evening!")
    speak("I am Nexa , Please tell me how may I help you?")    
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query    
if __name__ == "__main__":
    # speak("Akram is a good boy")
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()
        #logic for executing tasks based on query 
        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Acording to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query :
            webbrowser.open("google.com")
        elif 'open chatGpt' in query :
            webbrowser.open("chat.openai.com")
        elif 'play music' in query:
            music_dir = 'd:\\video songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak("Sir the time is ", strTime)   
        elif 'open code' in query:
            Code_Path = "C:\\Users\\aksfk\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(Code_Path)
            
        

    
    