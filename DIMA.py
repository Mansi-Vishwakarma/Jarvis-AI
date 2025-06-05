import  pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
     engine.say(audio)
     engine.runAndWait()
def wishMe():
     hour = int(datetime.datetime.now().hour)
     if hour >=0 and hour<12:
          speak("good morning!")

     elif hour>=12 and hour <18:
          speak("good afternoon!")

     else:
          speak("good evening!")
     speak(" I am your AI assistant please tell me how may I help you")
def takeCommand():
     r=sr.Recognizer()
     with sr.Microphone() as source:
          print("listening...")
          r.pause_threshold = 0.8
          audio = r.listen(source)
     try:
          print("Recognizing....")
          query = r.recognize_google(audio,language='en-in')
          print(f"User said: , {query}\n")
     except Exception as e:
          print(" say that again please..")
          return "None"
     return query
if __name__ == '__main__':
    wishMe()
    while True:
       query = takeCommand().lower()
       if 'wikipedia' in query:
            speak("searching wikipedia..")
            query = query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=2)
            speak(" according to wikipedia")
            print(results)
            speak(results)
       elif 'open youtube' in query:
           webbrowser.open_new("youtube.com")
       elif 'open google' in query:
           webbrowser.open_new("google.com")
       elif 'open whatsapp' in query:
           webbrowser.open_new("whatsapp.com")
       elif 'play music' in query :
            music_dir ='C:\\Users\\hp\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[1]))
       elif 'the time' in query:
           strTime  = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"Ma'am, the time is {strTime}")
       elif 'open code' in query:
           codePath="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(codePath)
       elif 'open lab' in query:
           path="C:\\Program Files\\scilab-2025.0.0\\bin\\WScilex.exe"
           os.startfile(path)
       elif 'who built you' in query:
           speak("Mansi Vishwakarma , Dipali Mishra and Lucky kanaujiya built me")
       elif 'open gmail' in query:
           G_mail="https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox"
           speak("opening your gmail Ma'am")
           os.startfile(G_mail)
       elif 'open gpt' in query:
           speak("opening chatgpt")
           chat="https://openai.com/index/chatgpt/"
           os.startfile(chat)
       elif 'how are you jarvis' in query:
           speak("Thankyou for asking I am good , how are you?")
       elif 'I am fine' in query:
           speak("that's great tell me how can I help you Ma'am")