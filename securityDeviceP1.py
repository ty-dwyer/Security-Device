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
                print("Still Locked")
            else:
                print("Still Unlocked")
        return LockStatus

def getDigit(number, n):
    return number[n]

def main():
    Code = "83363"
    LockStatus = True
    State = 0

    print("Part 1")
    print(" Your program will read from standard input without echoing the input characters. Characters other than digits 0 throuh 9 will be quietly discarded. \n",
            "Your engine will recognize a fixed access code. The access code will be the least significant five digits in your student ID, \n",
            "followed by a 1 for the unlock code and by a 4 for the locking code.\n",
            "\n",
            "DDDDD1 is the unlocking code \n",
            "DDDDD4 is the locking code \n",
            "\n",
            "Where DDDDD are the lest significant five digits in your student ID. \n",
            "As soon as the last digit of the access code is entered, your program will signal the action taken (lock or unlock).)")
    while(True):
        val = input(">> ")
        key = getDigit(Code, State)
    
        if val is key:
            State += 1
        else:
            State = 0
        if State == 5:
            Value = int(input("key >> "))
            LockStatus = LockCheck(Value, LockStatus)
            State = 0


if __name__ == "__main__":
    main()
