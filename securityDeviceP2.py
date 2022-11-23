#Lock Check Method
import random
from time import sleep

def LockCheck(key, LockStatus):
    if key == 1 and LockStatus is True: #if unlock value is entered and lock is locked
        print("Unlocked")
        return False

    elif key == 4 and LockStatus is False: #if lock value is entered and lock is unlocked
        print("Locked")
        return True

    else:
        if (key == 1) or (key == 4): #to ensure security
            if LockStatus is True:
                print("... Still Locked")
            else:
                print("... Still Unlocked")
        else:
            print("...")

        return LockStatus

def getDigit(number, n):
    return number // 10**n % 10


def numDigits(num):
    count = 0
    while num != 0:
        num //= 10
        count += 1
    return count


def DoorCheck(door):
    if door is False:
        print("Unlocked")
    else:
        print("Locked")
    return door

def main():
    # Global Variables
    seconds = 0
    Code = random.randint(0,99999)
    print("Code is:",Code)
    LockStatus = True # current status of lock
    State = numDigits(Code) - 1  # Current state in FSM
    currState = State

    sleep(3)
    #Main method
    print("Part 2")
    while(True): # Part 2
        
        if DoorCheck(LockStatus) is False: #Check Lock
            print(seconds, "seconds")
            break

        # enter value in one at a time
        val = random.randint(0,9)
        key = getDigit(Code, currState)
        seconds += 1
        print(" >> ", val)

        if val == key: #if the the nth digit in key was match in sequence
            currState -= 1
        else: #if you break the sequence
            currState = State

        if currState == -1: #if you reach end of code
            Value = random.randint(0,9)
            print("key >> ", Value)
            LockStatus = LockCheck(Value, LockStatus)
            currState = State #reset state


if __name__ == "__main__":
    main()
