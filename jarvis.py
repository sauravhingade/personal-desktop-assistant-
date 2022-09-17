from email.mime import audio
from http import server
from logging import exception
import os
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import smtplib
l={"sanchi":"sanchimanwar9966@gmail.com"}
engine=pyttsx3.init('sapi5')      # it is a microsoft api that use windows voice for user
voices=engine.getProperty('voices')   #there are two voices in windows api male and female ,by using getproperty we can acces any of it

engine.setProperty('voice',voices[1].id)              #by using setproperty we set the voice
                                                        #there are two voices in window's api david's and zira's
                                                        #voice[0]--david , voice[1]--zira

def speak(audio):
    engine.say(audio)                                   #this is to say the audio
    engine.runAndWait()                                 # without using this the audio is not audible 

   
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
        speak("i am jarvis sir.  please tell me how can i help you")
    elif hour>=12 and hour<18:
        speak("good afternoon")
        speak("i am jarvis sir.  please tell me how can i help you")
    else :
        speak("good evening")
        speak("i am jarvis sir.  please tell me how can i help you")  

def takeCommand():
    # it takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:                  #auid input takes from microphone and microphone is use as source
        print("Listening......")      
        r.pause_threshold=1                              #seconds of non-speaking audio before a phase is considered as complete
        audio = r.listen(source)                                            #audio input me kitna time ka break lene ke baad input complte hogya aisa 
                                                  # consider hoga
                                                 
    try:
        print("recognizing....")
       
        query =r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        print("say that again please")
        return "None"
    return query
def sendEmail(to,msg):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sauravhingade66@gmail.com','ebmjqhnyrmgupurq')
    server.sendmail('sauravhingade66@gmail.com',to,msg)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
      if 1:  
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=1)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'who are you' in query:
            speak("i am a personal desktop assistant  i can follow your simple commands to save your time .")    
        elif 'instagram' in query:
            speak("opening instagram")
            webbrowser.open("instagram") 
       
        elif 'search' in query:
            speak("what do you want to search")
            q=takeCommand()
            webbrowser.open(q)            
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open map' in query:
            speak("opening google map")
            webbrowser.open("www.google.co.in")      
        elif 'overflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com") 
        elif 'play music' in query:
            s=random.randint(0,9)
            music_dir= 'E:\\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[s]))

        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'open code' in query:
            speak("opening code")
            code_path= "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        elif 'open word' in query:
            speak("opening word")
            word_path= "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Word 2013.lnk"  
            os.startfile(word_path)  
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            whpath= "C:\\Users\\HP\AppData\\Local\\WhatsApp\\WhatsApp.exe"   
            os.startfile(whpath) 
        elif 'open chrome' in query:
            speak("opening chrome")
            chpath= "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"   
            os.startfile(chpath)     
        elif 'open spotify' in query:
            speak("opening spotify")
            repath= "C:\\Users\\HP\\AppData\\Local\\Programs\\Resso\\Resso.exe"   
            os.startfile(repath)     
        elif 'movies' in query:
            speak("okay")
            
            movpath= 'E:\\MOVIES'
            os.startfile(movpath)
        elif 'my documents' in query:
            speak("okay")
            
            dpath= 'E:\\my documents'
            os.startfile(dpath)
        elif 'java' in query:
            speak("okay")
            
            jpath= 'E:\\java\\Samjava.pdf'
            os.startfile(jpath)    
        elif 'open email' in query:
            webbrowser.open("gmail.com")  
        elif 'send mail' in query:
  
              
              
               speak("enter gmail id")
 
               id =input()
              
               speak("what to say")

               content=takeCommand()
               sendEmail(id,content)
               speak("email has been sent")
               print("email has been sent")
            
       
            
        elif 'stop' in query :
               speak("okay")
               break   
          