import speech_recognition as sr
import os
import webbrowser as wb
import pyttsx3 as pt


r=sr.Recognizer()

# the with statement ensures proper opening and closing of resources
with sr.Microphone() as source:
    print("Say something")
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print(text)
    except:
        print("Sorry could not understand")

li=text.split()
if li[0]=="what" or li[0]=="why" or li[0]=="when":
    wb.open("https://google.com/search?q=%s"%text)
    
elif text.find("show")!=-1 and text.find("mail")!=-1:
    wb.open('https://mail.google.com/mail/u/0/#inbox') 
elif text.find("sleep")!=-1:
    os.system("shutdown.exe /h")
else:
    engine = pt.init()
    engine.say('well that was no command. So how are you?')
    engine.runAndWait()
        