import speech_recognition as sr

r = sr.Recognizer()
## this is the same path of the audio file 
audio = r'C:/Users/Null/Desktop/SWE2222/vid2txt/trumpcovid.mp4wav.wav'

with sr.AudioFile(audio) as source:
    audio = r.record(source)
    print ('Done!')

try:
    text = r.recognize_google(audio)
    #print("Hello stackoverflow!", file=open("output.txt", "a"))
    x= open("C:/Users/Null/Desktop/SWE2222/vid2txt/output5.txt",'w')
    x.write(text)
    x.close()
    print (text)

    
except Exception as e:
    print (e)