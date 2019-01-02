from os import rename
from time import sleep

# Constants
MSG_PATH = "Relative path to .txt file (from this program/) containing message to transmit"
FOLDER_A_PATH = "Absolute path to folder A"
FOLDER_B_PATH = "Absolute path to folder B"
MOVE_DATA_PATH = "Relative path (from within folder A at FOLDER_A_PATH) to data to move"
BIT_SLEEP_TIME = X
ONE_SLEEP_TIME = X
SECURITY_BIT_REPEATS = X
SECURITY_BIT_SLEEP_TIME = X

f = open(MSG_PATH,"r")
msg = list(f.read())
f.close()
m2state = "a"
fap = FOLDER_A_PATH + "/" + MOVE_DATA_PATH
fbp = FOLDER_B_PATH + "/" + MOVE_DATA_PATH

def move(m2state):
    if m2state == "a":
        rename(fap,fbp)
    elif m2state == "b":
        rename(fbp,fap)

print("Start camera in 5...")
sleep(1.5)
print("4")
sleep(1.5)
print("3")
sleep(1.5)
print("2")
sleep(1.5)
print("1")
sleep(1.5)
print("0 (Start Camera now!)\nStarting in 5 seconds...")
sleep(5)
try:
    for bit in msg:
        for i in range(SECURITY_BIT_REPEATS):
            if bit == "0":
                print("0====================")
            elif bit == "1":
                print("1============================================================")
            move(m2state)
            if m2state == "a":
                m2state = "b"
            elif m2state == "b":
                m2state = "a"
            if bit == "1":
                sleep(ONE_SLEEP_TIME)
                print("========================================")
                move(m2state)
                if m2state == "a":
                    m2state = "b"
                elif m2state == "b":
                    m2state = "a"
            sleep(SECURITY_BIT_SLEEP_TIME)
        sleep(BIT_SLEEP_TIME)

# Cleanup
finally:
    if m2state == "b":
        move("b")
