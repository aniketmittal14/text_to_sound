from gtts import gTTS
from playsound import playsound

audio='speech.mp3'
language='en'

sound=gTTS(text='hii mate! Nice to meet you',lang=language,slow=True)
sound.save(audio)
playsound(audio)
