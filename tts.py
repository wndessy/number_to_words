from solution import NumbersToWords
from gtts import gTTS
import os


class NumberToSpeech():
    def number_to_english(self):
        mytext = 'Hello world'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save('hello.mp3')
        os.system('hello.mp3')


if __name__ == '__main__':
    say = NumberToSpeech()
    say.number_to_english()
