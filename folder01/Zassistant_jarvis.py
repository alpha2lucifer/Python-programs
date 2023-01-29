import time
import androidhelper as A
#import wikipedia
var = A.Android()
def say(TeXt):
    var.ttsSpeak(TeXt)
def assistant():
    var.makeToast('Viyom version 1.0')
    test = 0
    while True :
        (id, result,error) = var.recognizeSpeech('say something')
        print(result)
        if "hello" in result :
            say("hi")
        elif 'time' in result :
            var.ttsSpeak(time.strftime("%I %M %p on %A, %B %e, %Y"))
        elif result == 'how are you' :
            say('i am good ,how are you ?')
        elif result == 'what is your name' :
            say('i just told you I am jarvis a chatbot your virtual assistant')
        elif result == "take a picture" :
            say("capturing a picture say cheese")
            var.cameraInteractiveCapturePicture('/sdcard/qpython.jpg')
        elif result == "make a phone call" :
            uri = var.pickContact(). result ['data']
            var.phoneCall(uri)
        elif 'quit' in result :
            say("quitting")
            break
        else:
            test+=1
            if (test < 3) :
                say("Sorry, say that again")
            elif (test == 3) :
                say("say or ask something meaningful or the system will close me ")
            elif (test == 4) :
                say("Good bye if you want to talk to me again, just run this program one more time ")
                break

say('''Hello I am Viyom''')         
assistant()
'''elif 'what' in result :
            try :
                wiki_res = wikipedia.summary(result, sentences=2)
                say(wiki_res)
            except :
                wiki_res = wikipedia.summary(result, sentences=2)
                say(wiki_res)'''