import pyttsx3

if __name__ == '__main__':
    text_to_speech=pyttsx3.init()
    print("WELCOME TO ROBOSPEAKER,CREATED BY Varidhi")
    while True:
     yourWords=input("Enter what do you  want me to speak :")

     if yourWords =="quit":
         text_to_speech.say("see you again")
         text_to_speech.runAndWait()
         break
     text_to_speech.say(yourWords)
     text_to_speech.runAndWait()


