"""
Samuel Greenberg
DT038G
25/11/2021
Labb 4 Reader-Writers problem
"""

"""
Använde en klass med metoder för det som trådarna ska kunna göra 
Källa: https://cppsecrets.com/users/120612197115104981111171149751485164103109971051084699111109/Python-Implementation-of-Reader-Writer-Solution-using-Semaphore.php
"""

from threading import Lock, Semaphore, Thread
from datetime import datetime
import time

readLock = Semaphore(3)
writeLock = Lock()
NrOfSemaphores = int(readLock._value)

def lockReaders(): #Låser alla semaforer
    for i in range(NrOfSemaphores):
        readLock.acquire()

def unlockReaders(): #Låser upp alla semaforer
    for i in range(NrOfSemaphores):
        readLock.release()

class ReadWriteThreads():
    date = (datetime.now()).strftime("%Y/%m/%d %H:%M:%S\n")
    def read(self):
        while(True):
            if(not writeLock.locked()):
                readLock.acquire()
                print(f"Thread is reading... {ReadWriteThreads.date}") #Här är kritiska sektionen för read
                readLock.release()

    def write(self):
        while(True):
            writeLock.acquire() #Detta betyder för readers att inga nya readers får köra
            lockReaders() #Tar reader låsen en efter en
            ReadWriteThreads.date = (datetime.now()).strftime("%Y/%m/%d %H:%M:%S") #Här är kritiska sektionen för write
            print("Thread is writing to Date")
            writeLock.release()
            unlockReaders()

    def writeReverse(self):
        while(True):
            writeLock.acquire() #Detta betyder för readers att inga nya readers får köra
            lockReaders() #Tar reader låsen en efter en
            ReadWriteThreads.date = (datetime.now()).strftime("%Y/%m/%d %H:%M:%S")[::-1] #Här är kritiska sektionen för writeReverse
            print("Thread is writing to Date in reverse")
            writeLock.release()
            unlockReaders()
    
    def startThreads(self):
        t1 = Thread(target = self.read)
        t1.start()
        t2 = Thread(target = self.write)
        t2.start()
        t3 = Thread(target = self.writeReverse)
        t3.start()
        t4 = Thread(target = self.read)
        t4.start()
        t5 = Thread(target = self.read)
        t5.start()

RW = ReadWriteThreads()
RW.startThreads()