import time
from subprocess import Popen, PIPE
from threading import Thread
import os
import sys

COMMAND = """ffmpeg -r 24 -i movie.mp4 -vf drawtext="fontfile=font.ttf: \
        textfile=text.txt: fontcolor=white: fontsize=64: box=1: boxcolor=teal@0.75: \
        boxborderw=8: x=(w-text_w)/2: y=h/2:reload=1" -codec:a copy -r 24 output.mp4"""

TEXT = "Thank you all 19 nice people.".upper()

# write a text writer
# we need to execute this external shell command (and fetch the output of it)
# start the text writer
# start the external shell
# wait for all
# open the final movie


def textwriter(text: str):
    open("text.txt", "w").close()
    time.sleep(0.5)
    with open("text.txt", "w") as handler:
        for c in text:
            time.sleep(1 / 24)
            handler.write(c)
            handler.flush()  ## Always flush your buffer in concurrent programs


def execute(cmd: str):
    p = Popen(cmd, stderr=PIPE, bufsize=128, universal_newlines=True, shell=True)
    for line in iter(p.stderr.readline, ""):
        if p.poll():
            break
        yield line
    p.wait()


if os.path.isfile("output.mp4"):
    os.remove("output.mp4")

t = Thread(target=textwriter, args=(TEXT,))
t.start()


for _each in execute(COMMAND):
    print("•", end="", file=sys.stderr, flush=True)

t.join()

os.system("open output.mp4")
