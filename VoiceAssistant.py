import openai
import pyttsx3
import speech_recognition as sr
import webbrowser

openai.api_key = "Chat-GPT API"

completion=openai.Completion()

def Reply(question):
    prompt=f'RAGHAV: {question}\n JARVIS: '
    response=completion.create(prompt=prompt, engine="davinci-text-003 ", stop=['\RAGHAV'], max_tokens=3000)
    answer=response.choices[0].text.strip()
    return answer

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello Raghav! Jarvis this side ")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio, language='en-in')
        print("RAGHAV SAID: {} \n".format(query))
    except Exception as e:
        print("Say That Again....")
        return "None"
    return query


if __name__ == '__main__':
    
    while True:
        query=takeCommand().lower()
        ans=Reply(query)
        print(ans)
        speak(ans)

        if 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        if 'open google' in query:
            webbrowser.open("www.google.com")
        if 'bye' in query:
            speak("BYE RAGHAV ! HAVE A GOOD DAY")
            break


