from datetime import datetime
import os
import time

MyInputTime=input("Set the programmation of the script: (ex: 12:00:00)")
# MyInputTime="13:43:00"

ItsNotTime= True
while ItsNotTime:
    Now=datetime.now()
    timing = Now.strftime("%H:%M:%S")
    print(timing)
    if timing == MyInputTime:
        print("Its time to go")
        ItsNotTime=False
