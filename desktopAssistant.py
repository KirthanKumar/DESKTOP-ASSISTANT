import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import random

from selenium import webdriver

# requirements
# pyttsx3==2.87
# SpeechRecognition==3.8.1
# wikipedia==1.4.0

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id) # 0 --> david voice, 1 --> zira voice
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! ")

    elif hour >= 12 and hour < 17:
        speak("Good Afternoon! ")

    elif hour >= 17 and hour < 19:
        speak("Good Evening! ")

    else:
        speak("Good Night! ")

    speak("I am your virtual assistant. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # user can pause for 1 sec while talking
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("Connection error")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kirthan.cs21@bmsce.ac.in', '##########')
    server.sendmail('kirthan.cs21@bmsce.ac.in', to, content)
    server.close()
    # print(f"Email to {to} send with subject {sub} and message {msg}")
    # s = smtplib.SMTP('smtp.gmail.com', 587)
    # s.starttls()
    # s.login(GMAIL_ID, GMAIL_PSWD)

    # s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")
    # s.quit()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif name := 'stack overflow' in query:
            c = webdriver.ChromeOptions()
            c.add_argument("--incognito")
            driver = webdriver.Chrome(
                executable_path="C:\chromedriver.exe", options=c)
            driver.implicitly_wait(0.5)
            driver.get("https://www.stackoverflow.com")

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")

        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("opening stackoverflow")

        elif 'play music' in query:
            music_dir = 'music folder\\path'
            songs = os.listdir(music_dir)
            no_of_songs = len(songs)
            randomNumber = random.randint(0, no_of_songs)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[randomNumber]))

        elif "play video" in query:
            video_dir = 'D:\\FFOutput\\Screen Record'
            Videos = os.listdir(video_dir)
            no_of_videos = len(Videos)
            randomNumber = random.randint(0, no_of_videos)
            # print(Videos)
            os.startfile(os.path.join(video_dir, Videos[randomNumber]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\kirthan kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" # this is target og application vs code taken form properties
            os.startfile(codePath)
            
        elif 'send email' in query: #enable less secure apps
            try:
                speak("to whom?")
                emailto = takeCommand().lower()
                speak("What should I say?")
                content = takeCommand().lower()
                sendEmail(emailto +".cs21@bmsce.ac.in", content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send this email")
            
        elif 'quit' in query:
            speak("ok quitting sir")
            exit()

        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s')

        elif 'how are you' in query:
            setMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!']
            ans_qus = random.choice(setMsgs)
            speak(ans_qus)
            speak(" How are you'")
            ans_from_user_how_are_you = takeCommand()
            if 'fine' in ans_from_user_how_are_you or 'happy' in ans_from_user_how_are_you or 'good' in ans_from_user_how_are_you:
                speak('Great')
            elif 'sad' in ans_from_user_how_are_you or 'not good' in ans_from_user_how_are_you:
                speak('Tell me how can i make you happy')
            else:
                speak("I can't understand. Please say that again !")

        else:
            temp = query.replace(' ', '+')
            url = "https://www.google.com/search?q="
            res = 'sorry! i cant understand but i search from internet to give your answer !'
            print(res)
            speak(res)
            webbrowser.open(url+temp)
