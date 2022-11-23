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

    print("Input Passcode:")
    while(True):
        val = input(" ")
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
