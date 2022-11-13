import playsound
import requests
import speech_recognition as sr
import random
import os
from gtts import gTTS

bot_message = ""
message = ""

while bot_message != "bye" or bot_message != 'thanks':
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak,Poorni is listening :")
        audio = r.listen(source)
        try:
            message = r.recognize_google(audio)
            print("You said : {}".format(message))
        except:
            print("Sorry,I could not hear you")
            if len(message) == 0:
                continue
    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})
    print(end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")
        myobj = gTTS(text=bot_message)
        r1 = random.randint(1, 10000000)
        r2 = random.randint(1, 10000000)

        randfile = str(r2) + "randomtext" + str(r1) + ".mp3"

        myobj.save(randfile)
        print('saved')
        playsound.playsound(randfile)
        os.remove(randfile)
