from os import rename
from time import sleep

# Constants
MSG_PATH = "Path to .txt file (from this program) containing message to transmit"
FOLDER_A_PATH = "(Complete) Path to folder A"
FOLDER_B_PATH = "(Complete) Path to folder B"
MOVE_DATA_PATH = "Path to data to move (from within folder A at FOLDER_A_PATH)"
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

print("Starting in 5 seconds...")
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
