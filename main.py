import pyttsx3 ##speech to text ##pip install pyttsx3
## is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
import speech_recognition as sr ##pip install speechRecognition
import datetime
import wikipedia ##pip install wikipedia
import os
import webbrowser
import smtplib

print('Initialising Dilly')

MASTER='Aish'
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) ##voice -> 1 (female)  ,voice->0 male


#This speak function will pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

#This function will wish you as per the current time
def WishMe():
    hour=int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning" + MASTER)
    elif hour>=12 and hour<=18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)
    speak('Hi Iam Dilly. How may I help you?..')    

#This function will take command from your microphone
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:  ##can recognise only default laptop microphone 
        r.adjust_for_ambient_noise(source,duration=1)
        print('Listening...')
        audio=r.listen(source)

    try :
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print("Could You repeat it please")
        query=None
    return query
#This function will send mail to whom you want
def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('dummymail@gmail.com', 'pwd')
    server.sendmail('dummymail@gmail.com', to, content)
    server.close()



#Main Program starts here
def main():

    speak("Initialising Dilly")
    WishMe()
    query=takeCommand()

    #Logic for executing basic tasks as per the query

    if 'wikipedia' in query.lower():
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 3)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query.lower():
        webbrowser.open("www.youtube.com")
        a = webbrowser.get('Brave')
        a.open('www.youtube.com') 
    elif 'open google' in query.lower():
        webbrowser.open("www.google.com")
        a = webbrowser.get('Brave')
        a.open('www.google.com') 
    elif 'open reddit' in query.lower():
        webbrowser.open("www.reddit.com")
        a = webbrowser.get('Brave')
        a.open('www.reddit.com') 
    elif 'play music' in query.lower():
        songs_dir="D:\\music"
        songs=os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir,songs[0]))
    elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")   
                speak(f"Sir, the time is {strTime}")

    elif 'open code' in query.lower():
        codePath="E:\\AishSoftwares\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
    elif 'email to master' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "dummy2@gmail.com"   
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")
main()