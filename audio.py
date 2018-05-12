import pyglet as pg             #to use Pyglet in this program, need to install abvin
import speech_recognition as sr
def play_short_audio(filename):
    tune = pg.resource.media(filename,streaming= False)  #streaming set to false to lower cpu speed as file is short
    tune.play()
    pg.clock.schedule_once(exiter, 2)
    pg.app.run()

# play_short_audio('resources/to-the-point.mp3') #testing function


def exiter(dt):
    pg.app.exit()


recorder = sr.Recognizer()


def init_speech():
    print("Listening...")
    play_short_audio('resources/to-the-point.mp3')
    # print("reached here")

    with sr.Microphone() as mic:                # recording here
        # print("Start")
        audio = recorder.listen(mic)

    play_short_audio('resources/decay.mp3')    # indicates the recording has been completed

    command = ""
    try:
        command = recorder.recognize_google(audio)   # use google to understand command
    except:
        print("Sorry, unable to understand")        # error message 

    print(command)


init_speech()