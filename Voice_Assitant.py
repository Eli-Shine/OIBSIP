import speech_recognition as sr
import pyttsx3
import wolframalpha
import datetime
import wikipedia
import subprocess
import webbrowser
import os
import pyjokes
import time
import requests


# Initialize speech recognition
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Function to recognize voice commands
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(f"User said: {command}")
            return command
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't understand you.")
        return ""


# Greet the user
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your Assistant MJs. What should I call you?")


# Main function to handle user commands
def run_assistant():
    greet()
    username = take_command()

    if username:
        speak(f"Welcome {username}, How can I assist you?")

    while True:
        command = take_command()

        if 'wikipedia' in command:
            speak('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'time' in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The current time is {current_time}")

        elif 'open youtube' in command:
            speak("Here you go to Youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in command:
            speak("Here you go to Google")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in command:
            speak("Opening stackoverflow...")
            webbrowser.open("stackoverflow.com")

        elif 'exit' in command:
            speak("Thanks for giving me your time")
            exit()
        
        elif 'the time' in command:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"the time is {strTime}")

        elif 'how are you' in command:
           speak("I am fine, Thank you")
           speak("How are you also?")

        elif 'fine' in command or "good" in command:
           speak("Great")

        elif "what's your name" in command or "What is your name" in command:
           assist_name = "MJ"
           speak("I am called")
           speak(assist_name)
      
        elif "who made you" in command or "who created you" in command:
           speak("I was created by Shine as a project for her internship.")

        elif 'joke' in command:
           speak(pyjokes.get_joke())

        elif "calculate" in command:
           app_id = "Wolframalpha api id"
           client = wolframalpha.Client(app_id)
           indx = command.lower().split().index('calculate')
           command = command.split()[indx + 1:]
           res = client.command(' '.join(command))
           answer = next(res.results).text
           print("The answer is " + answer)
           speak("The answer is " + answer)

        elif 'search' in command or 'play' in command:
           command = command.replace("search", "")
           command = command.replace("play", "")
           webbrowser.open(command)

        elif "who i am" in command:
           speak("you are human a child of God.")

        elif 'is love' in command:
           speak("It is 7th sense that destroy all other senses") 

        elif "who are you" in command:
           speak("I am your voice assistant created by Shine")

        elif 'shutdown system' in command:
           speak("system shuting down")
           subprocess.call('shutdown /p /f')

        elif "restart" in command:
           subprocess.call(["shutdown", "/r"])

        elif "don't listen" in command or "stop listening" in command:
           speak("how long should i stop listening?")
           a = int(take_command())
           time.sleep(a)
           print(a)

        elif "where is" in command:
           command = command.replace("where is", "")
           location = command
           speak("User asked to Locate")
           speak(location)
           webbrowser.open("https://www.google.nl/maps/place/" + location + "")

        elif "wikipedia" in command:
         webbrowser.open("wikipedia.com")

        elif "will you be my gf" in command or "will you be my bf" in command:
         speak("I am not real please ask a human being instead")

        elif "how are you" in command:
         speak("I'm fine")

        elif "i love you" in command:
         speak("i love you too")

        elif "what is" in command or "who is" in command:
         client = wolframalpha.Client("API_ID")
         res = client.command(command)
         try:
            print(next(res.results).text)
            speak(next(res.results).text)
         except StopIteration:
            print("No results")

    else:
         speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    run_assistant()
