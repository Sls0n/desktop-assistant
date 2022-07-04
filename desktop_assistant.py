import random
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
from time import sleep
import keyboard


# Lists -->
Agree_List = ['Okay .', 'Alright .', 'Just a second .', 'On it.',
              'Sure .', 'One second .', 'I would love to do it.', 'Sure thing .']


# Speak Function -->
def speak(audio):
    engine = pyttsx3.init()
    # rate = engine.getProperty('rate')         [ getting details of current speaking rate ]
    # print (rate)
    engine.setProperty('rate', 170)             # Setting up speed rate.
    voices = engine.getProperty('voices')  # getting details of current voice
    # changing index, changes voices. 1 for female. 0 for male.
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()


def date():  # This function will extract the date.
    hour = str(datetime.date.today())
    speak("Today's date is " + hour)


def time():  # This function will extract the time.
    time_int = int(datetime.datetime.now().hour)
    if time_int >= 0 and time_int < 4:  # 0 is 1AM i.e Midnight
        speak("It's midnight I think you need to sleep. The time right now is " +
              str(time_int) + "AM")
    elif time_int >= 4 and time_int < 12:  # i.e Morning
        speak("Good morning ! It's " + str(time_int) + "AM right now.")
    elif time_int >= 12 and time_int < 18:  # i.e Noon
        speak("Noon  It's " + str(time_int) + " PM right now.")
    elif time_int >= 18 and time_int < 21:  # i.e Evening
        speak("Good Evening ! It's " + str(time_int) + "PM right now.")
    elif time_int >= 21 and time_int < 24:  # i.e Night
        speak("The time right now is " + str(time_int) + "PM. ")


def greet():
    time_int = int(datetime.datetime.now().hour)
    if time_int >= 0 and time_int < 4:  # 0 is 1AM i.e Midnight
        speak("Hi , assistant here. How can I be of service here at midnight. Umm")
    elif time_int >= 4 and time_int < 12:  # i.e Morning
        speak("Good morning ! assistant here. Is there anything I can help with?")
    elif time_int >= 12 and time_int < 18:  # i.e Noon
        speak("Noon ! assistant speaking. How can i assist you ?")
    elif time_int >= 18 and time_int < 21:  # i.e Evening
        speak("Good Evening ! assistant speaking. How can I help you?")
    elif time_int >= 21 and time_int < 24:  # i.e Night
        speak("Hi , How can I possibly help you while you are supposed to be sleeping? Always remember I can still operate while you are dreaming. ")


def AI_listen():  # This function is made for AI to listen your commands with speech recognition and run accordingly.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.7
        r.dynamic_energy_threshold = True
        r.dynamic_energy_ratio = 3
        audio = r.listen(source)

    try:
        print("Processing...")
        # Here I'm using "en-us" . You can put "in" instead of "us".
        query = r.recognize_google(audio, language='en-in')
        print(f"User's Query: {query}\n")

    except:
        # print("ERROR! Voice not clear")
        # speak(random.choice(["I didn't quite get you .","I didn't understand .", "Hmmm I am not sure if i understood your question ","Sorry ! Looks like you voice isn't clear","Can you repeat the question ","Your voice isn't audible "]))
        return "None"
    return query


def youtube_search(query):  # Searches in youtube.
    result = 'https://www.youtube.com/results?search_query=' + query
    webbrowser.open(result)
    speak("Searching in youtube")


def main_logic():
    if __name__ == '__main__':  # Gives output according to query

        while True:
            query = AI_listen().lower()


            if 'hey' in query:
                speak(random.choice(['Hi whats up!', 'Hey! How can I be of service',
                      'Heya  how can I help you?', 'how can I help you .']))
                AI_listen()

            elif 'hi' in query or 'hey' in query:
                speak("Hi ! ")

            elif 'hello' in query:
                speak("Hi ! ")

            elif 'how are you' in query:
                speak(random.choice(
                    ["I am fine .", "Couldn't be better than this", "Fine ! What about you?"]))

            elif 'fine' in query:
                speak(random.choice(
                    ["I'm glad you're fine .", "Nice to hear it ."]))

            elif 'thanks' in query:
                speak(random.choice(["No Problem !", "I am happy to serve you .",
                      "No problem, I'm programmed to help.", "You are welcome ."]))

            elif 'thank you' in query:
                speak(random.choice(["No Problem !", "I am happy to assist you .",
                      "No problem ! Is there any other thing I can help with?", "You are welcome ."]))

            elif 'wikipedia' in query:
                try:
                    query = query.replace("wikipedia", "")
                    query = query.replace("according to", "")
                    query = query.replace("what is", "")
                    query = query.replace("can", "")
                    query = query.replace("search", "")
                    query = query.replace("you", "")
                    query = query.replace("in", "")
                    query = query.replace("for", "")
                    results = wikipedia.summary(query, sentences=1)
                    speak("According to the WikiPedia")
                    print(results)
                    speak(results)
                except:
                    speak(random.choice(["Sorry I couldn't search your query? can you try again?",
                          " due to some error I couldn't search it", "Can you repeat the query ?"]))

            elif 'what is' in query:
                try:
                    query = query.replace("wikipedia", "")
                    query = query.replace("according to", "")
                    query = query.replace("what is", "")
                    query = query.replace("can", "")
                    query = query.replace("search", "")
                    query = query.replace("you", "")
                    query = query.replace("in", "")
                    query = query.replace("for", "")
                    results = wikipedia.summary(query, sentences=1)
                    speak("According to the WikiPedia")
                    print(results)
                    speak(results)
                except:
                    speak(random.choice(["Sorry I couldn't search your query? can you try again?",
                          "Ehh due to some error I couldn't search it", "Can you repeat the query ?"]))

            elif 'what is your name' in query:
                speak(
                    f"I don't have a name yet")

            elif 'your name' in query:
                speak("I don't have my name yet ")

            elif 'time' in query:
                time()

            elif 'date' in query:
                date()

            elif 'date time' in query:
                date()
                time()

            elif 'feature' in query or 'abilities' in query or 'what can you do' in query:
                speak(random.choice(["I can call your girlfriend and tell you are cheating with her. Whoops! I forget you dont have girlfriend", "I can upload your facecam",
                      "I can delete system32 from your computer.", "I can initialize self destroy protocol. It blows up your PC by the way."]))

            elif 'sing a song' in query:
                speak(
                    "I can't do that yet . But I hope I will be able to do it soon.")

            elif 'founder' in query:
                speak(random.choice(
                    ["Silson is the founder of this bot."]))

            elif 'open youtube' in query:
                URL = "https://www.youtube.com"
                speak("Opening youtube")
                webbrowser.open(URL)

            elif 'open google' in query:
                URL = "https://www.google.com"
                speak(random.choice(
                    ["Opening google", "Hold up a bit ", "Okay .", "just one second ."]))
                webbrowser.open(URL)
                speak("Opened google")

            elif 'check my instagram' in query:
                URL = "https://www.instagram.com"
                speak(random.choice(
                    ["checking your instagram", "Alright ", "Okay .", "just one second ."]))
                webbrowser.open(URL)

            elif 'open brave' in query:
                speak(random.choice(
                    ["Opening..", "Hold up a bit ", "Okay .", "just one second ."]))
                sleep(1)
                speak('Searching for the app.')
                keyboard.press_and_release('win + s')
                sleep(1)
                keyboard.write('brave')
                sleep(1)
                keyboard.press('enter')

            elif 'open spotify' in query:
                speak(random.choice(
                    ["Opening spotify", "just a second ", "Okay .", "Opening "]))
                sleep(1)
                speak('Searching for the app.')
                keyboard.press_and_release('win + s')
                sleep(1)
                keyboard.write('spotify')
                sleep(1)
                keyboard.press('enter')

            elif 'open lunar' in query:
                speak(random.choice(Agree_List))
                sleep(1)
                speak('Searching for the app.')
                keyboard.press_and_release('win + s')
                sleep(1)
                keyboard.write('lunar')
                sleep(1)
                keyboard.press('enter')

            elif 'search' in query and 'youtube' in query:
                query = query.replace("youtube", "")
                query = query.replace("can", "")
                query = query.replace("search", "")
                query = query.replace("you", "")
                query = query.replace("in", "")
                query = query.replace("for", "")
                query = query.replace('the', '')
                youtube_search(query)

            elif 'discord' in query:
                speak(random.choice(Agree_List))
                sleep(1)
                speak('Searching for the app.')
                keyboard.press_and_release('win + s')
                sleep(1)
                keyboard.write('discord')
                sleep(1)
                keyboard.press('enter')

            elif 'open' in query:  # Searching for app on search bar.
                try:
                    speak('Finding the app.')
                    query = query.replace('can', '')
                    query = query.replace('you', '')
                    query = query.replace('app', '')
                    query = query.replace('open', '')
                    query = query.replace('from', '')
                    query = query.replace('search', '')
                    query = query.replace('bar', '')
                    query = query.replace('the', '')
                    query = query.replace(' ', '')
                    query = query.replace('could', '')
                    keyboard.press_and_release('win + s')
                    sleep(1)
                    keyboard.write(query)
                    sleep(1)
                    keyboard.press('enter')
                except Exception as e:
                    speak("Couldn't find the app! Sorry!")
            elif 'male voice' in query or 'change voice' in query:
                speak(random.choice(["I can't do that yet."]))

            elif 'exit' in query:
                speak("Okay ! Exiting. However if you ever need assistance, just say my name.")
                exit()

            elif 'sleep' in query:
                speak(
                    f"Alright ! Good bye.")
                exit()

try:
    greet()
    main_logic()

except:
    print("Some error")
    main_logic()
