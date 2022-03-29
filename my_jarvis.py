import time

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyautogui
import mouse


engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[1].id)
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

    else:
        speak("Good Evening!")

    speak("Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com', 'your-password')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()

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

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        # elif 'email to harry' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "harryyourEmail@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry my friend harry bhai. I am not able to send this email")

        elif 'click on start' in query:
            mouse.move(562, 871)
            mouse.click(button='left')
        elif 'stop' in query:
            speak("as you wish sir")
            pyautogui.hotkey("ctrl","f2")
        elif 'start' in query:
            speak('which file you want to open')
            r1 = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r1.pause_threshold = 1
                audio = r1.listen(source)

            try:
                print("Recognizing...")
                query = r1.recognize_google(audio, language='en-in')
                print(f"User said: {query}\n")

            except Exception as e:
                # print(e)
                print("Say that again please...")
            pyautogui.hotkey('Ctrl','Tab')
            time.sleep(4)
            path=f'C:\\Users\\vaghe\\PycharmProjects\\newprog\\{query}.py'
            time.sleep(3)
            pyautogui.write(path)
            pyautogui.click('Enter')
        elif 'modul' in query:
            pyautogui.hotkey("win","r")
            time.sleep(3)
            pyautogui.press("Enter")
            time.sleep(3)
            x=query.split(" ")
            pyautogui.write(f"pip install {x[0]}")
        elif 'jarvis' in query:
            speak("i have so many features like modul download "
                  "show time and play music and i also start and stop any program in any directroy")
