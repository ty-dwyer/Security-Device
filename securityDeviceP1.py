#Lock Check Method
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
                print("Still Locked")
            else:
                print("Still Unlocked")
        return LockStatus

def getDigit(number, n):
    return number[n]

#State = 4
#Code = 59823
# 59823 // 10000 = 5 % 10 = 5
# 59823 // 1000 = 59 % 10 = 9
# 59823 // 100 = 598 % 10 = 8
# 59823 // 10 = 5982 % 10 = 2
# 59823 // 1 = (59820 + 3) % 10 = 3

def main():
    # Global Variables
    Code = "83363"  # Our code Student ID: A204(59823)
    LockStatus = True # current status of lock
    State = 0  # Current state in FSM

    #Main method
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
    while(True): # Part 1
        # enter value in one at a time
        val = input(">> ")
        key = getDigit(Code, State)
    
        if val is key: #if the the nth digit in key was match in sequence
            State += 1
        else: #if you break the sequence
            State = 0
        if State == 5: #if you reach end of code
            Value = int(input("key >> "))
            LockStatus = LockCheck(Value, LockStatus)
            State = 0 #reset state


if __name__ == "__main__":
    main()
