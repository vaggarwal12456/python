import wolframalpha as wf
import wikipedia as wiki
import pyttsx3
import speech_recognition as sr
import os

r = sr.Recognizer()
client = wf.Client('V7TGPA-EE3XH495AR')
en = pyttsx3.init()
en.setProperty(
    'voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
en.setProperty('rate', 130)


flag = True
while(flag):
    try:
        while(1):
            with sr.Microphone() as source:

                r.adjust_for_ambient_noise(source,duration=2)
                print('How can I help you!\n ')
                audio = r.listen(source)
                print(r.recognize_google(audio))

            que = r.recognize_google(audio)

            que = que.lower()
            que = que.split(' ')


            if(' '.join(que)=='go to sleep' or ' '.join(que)=='bye bye'):
                flag = False
                en.say('bye See you later!')
                en.runAndWait()
                break

            if(que[0]=='open'):
                temp = ' '.join(que[1:])
                if(que[1]=='calculator'):
                    os.system('calc')
                elif(' '.join(que[1:])=='control panel'):
                    os.system('control')
                elif(' '.join(que[1:])=='notepad'):
                    os.system('notepad')
                elif(temp == 'windows media player'):
                    os.system('wmplayer')




            else:

                if(' '.join(que[:2]) == 'who was' or ' '.join(que[:2]) == 'who is' or ' '.join(que[:3]) == 'tell me about'):

                    ans = wiki.summary(' '.join(que[2:]), sentences=2)
                    print(ans)
                else:
                    que = ' '.join(que)
                    try:

                        re = client.query(que)
                        ans = re.results

                        ans = next(re.results).text

                    except:
                        ans = wiki.summary(que, 'html.parser', sentences=2)
                        print(ans)


                print(ans)
                en.say(ans)
                en.runAndWait()

    except:
        pass
