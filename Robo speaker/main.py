import pyttsx3

speaker= pyttsx3.init()

while(True):
    print("Welocome to RoboSpeaker 1.0 Created by Sharad")
    x=input("What do you want me to speak: ")
    if(x=='q'):
        speaker.say("Bye Bye")
        speaker.runAndWait()
        break
    
    speaker.say(x)
    speaker.runAndWait()


