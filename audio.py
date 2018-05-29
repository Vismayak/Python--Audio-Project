import pyglet as pg  # to use Pyglet in this program, need to install abvin
import speech_recognition as sr
import subprocess
from commands import Commands

def play_short_audio(filename):
    tune = pg.resource.media(filename, streaming=False)  # streaming set to false to lower cpu speed as file is short
    tune.play()
    pg.clock.schedule_once(loop_exit, 1.5)
    pg.app.run()


# play_short_audio('resources/to-the-point.mp3') #testing function


def loop_exit(dt):
    pg.app.exit()


def say(text):
    subprocess.call('say -v "Victoria" ' + text, shell=True)


recorder = sr.Recognizer()
cmd = Commands()
running = True


def init_speech():
    print("Speak at the end of the sound")
    play_short_audio('resources/to-the-point.mp3')
    # print("reached here")

    with sr.Microphone() as mic:  # recording here
        # print("Start")
        audio = recorder.listen(mic)

    play_short_audio('resources/decay.mp3')  # indicates the recording has been completed


    try:
        command = recorder.recognize_google(audio)  # use google to understand command
        print(command)
        if command in ["stop","quit","exit"]:
            say("Thank you and good night sir")
            global running
            running = False

        else:
            cmd.discover(command)
    except:
        print("Sorry, unable to understand")  # error message


while running:
    init_speech()
