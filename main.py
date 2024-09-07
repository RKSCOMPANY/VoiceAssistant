import random
import openai
import speech_recognition as sr
import os
import webbrowser
from openai import OpenAI
import datetime


Name = "Rashmi"              #your name
Model_Name = "friday"           #model name

                             #function for voice

def say(text):
  # Escape the text to prevent shell misinterpretation
  safe_text = text.replace(".", " ").replace(",", " ")
  os.system(f"say \"{safe_text}\"")

'''
def say(text):
    os.system(f"say {text}")
'''

                            # function to fetch the answer


def ai(prompt):
    client = OpenAI()
    text = f"{Name} questions response from {Model_Name}: \n\n Question: {prompt} \n ****************************** \n\n"
    openai.api_key= "openai_api_key"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages =  [
            {"role": "user", "content":f" You are an AI assistant that provides concise and to-the-point answers. Keep your responses brief and ensure that the information is clear and direct. Avoid elaboration unless absolutely necessary. here is the question : {prompt}  "}
                   ] ,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    try:
        message = response.choices[0].message.content
        print(message)
        say(message)
    except Exception as e:
        say("Sorry I don't have answer for it")

    text += response.choices[0].message.content
    if not os.path.exists("Questions&Answers"):
       os.mkdir("Questions&Answers")

    with open(f"Questions&Answers/prompt{random.randint(1, 2343434356)}", "w") as f:
        f.write(text)


                                   #function to take input as voice and return the string


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            que = r.recognize_google_cloud(
                audio,
                credentials_json=None,
                language="en-in",
                preferred_phrases=None,
                show_all=False
            )
            print(f"{Name} Said: {que}")
            return que
        except Exception as e:
            say(f"Sorry {Name} I can't Understand ! tell me one more time")
            exit()


'''
def after_exception():
    say(f"Sorry {Name} I can't Understand ! tell me one more time")
    print("listening...")
    query = take_command()
    ai(query)
'''


if __name__ == '__main__':
   Name = input("Enter your Name")
   print(f"Hii! {Name}! {Model_Name} this side")
   say(f"Hi! {Name}! {Model_Name} this side")

   while True :
     print("Listening...")
     query1 = take_command()

     #opening the sites
     sites = [["facebook","https://www.facebook.com"],["instagram","https://www.instagram.com"],["google","https://www.google.com"],["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["gmail","https://www.gmail.com"]]
     for site in sites:
         if f"Open {site[0]}".lower() in query1.lower():
             say(f"Opening {site[0]} sir...")
             webbrowser.open(site[1])
             exit()

     if "the time" in query1:
         strfTime = datetime.datetime.now().strftime("%H:%M:%S")
         say(f"sir the time is {strfTime} ")

     elif "open facetime".lower() in query1.lower():
          say(f"opening {Name }sir ")
          os.system(f"open /System/Applications/FaceTime.app")
          exit()

     elif "open whatsapp".lower() in query1.lower():
         say(f"opening {Name}sir ")
         os.system(f" open /Applications/WhatsApp.app")
         exit()

     elif f"bye bye".lower() in query1.lower():
         say(f"byeeeee {Name} ! Catch me Later ! I miss you  ")
         exit()

     elif f"{Model_Name} ".lower() in query1.lower():
         ai(prompt=query1)
