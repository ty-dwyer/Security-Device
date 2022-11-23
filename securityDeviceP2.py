import random
from time import sleep

def LockCheck(key, LockStatus):
    if key == 1 and LockStatus is True:
        print("Unlocked")
        return False

    elif key == 4 and LockStatus is False:
        print("Locked")
        return True

    else:
        if (key == 1) or (key == 4):
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
    seconds = 0
    Code = random.randint(0,99999)
    print("Code is:",Code)
    LockStatus = True 
    State = numDigits(Code) - 1 
    currState = State

    sleep(3)
    print("Part 2")
    while(True):
        
        if DoorCheck(LockStatus) is False:
            print(seconds, "seconds")
            break

        val = random.randint(0,9)
        key = getDigit(Code, currState)
        seconds += 1
        print(" >> ", val)

        if val == key:
            currState -= 1
        else:
            currState = State

        if currState == -1:
            Value = random.randint(0,9)
            print("key >> ", Value)
            LockStatus = LockCheck(Value, LockStatus)
            currState = State


if __name__ == "__main__":
    main()
