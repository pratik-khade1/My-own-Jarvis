import webbrowser
import pyttsx3
import speech_recognition as sr

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process(c):
    if c.lower()=="open google":
        speak("Opening Google")
        webbrowser.open("https://google.com")

if __name__ == "__main__":
    
    count = 0
    status = True
    while status:
        
        try:
            #Listening word
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source,timeout=3,phrase_time_limit=1)
            
            word = recognizer.recognize_google(audio)

            #Activating Jarvis
            if word.lower() == "activate":
                if count==0:
                    speak("Activating Jarvis...")
                    count += 1
                elif count!= 1:
                    speak("I am already active")

                #Jarvis is active    
            if word.lower() == "jarvis" or count==2:
                speak("yeah")
                
                with sr.Microphone() as source:
                    print("Jarvis Listening...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    process(command)
            #Deactivate  
            if word.lower() == "deactivate":
                    speak("Deactivating Jarvis...")
                    status = False
                    count = 0
                    
            
                    
        except sr.UnknownValueError:
            print("error")
        except sr.WaitTimeoutError:
            print("Timeout")
        except Exception as e:
            print("Speak something")
    