**README**
          
What is this repository?
> This repository is a CS330 Coding Project that contains a Python Demo code that simulates a security lock that you would see at an office or your house.


> The code ultilizes a Finite State Machine to tell wether the correct passcode is inputted and changes from locked to unlocked.
 
How do I run this project?
> Instructions are int his README file and are for a ubuntu environment

Summary of setup
> You Must have python installed

Configuration
> 1. Clone the repository
       ```  $ git clone https://github.com/ty-dwyer/Security-Device.git ```
> 2. Run the code for the corresponding part

>```$ python3 securityDeviceP1.py```

>```$ python3 securityDeviceP2.py```

>After running the code input individual digits 0-9. If a non integer is entered the machine will restart your code input. After the correct passcode is entered it will prompt you for the key enter 1 or 4 for the corresponding lock and unlock. If anything else is entered as the key the machine will ask you for the passcode again.

Unit Test Coverage
>This lockCheck function takes in a key, which is a numerical unlock or lock value and the current LockStatus which tells us if the access is currently locked and unlocked. This code block, or method, is called when the correct sequence is entered to the keypad.

Known Bugs
>no bugs it is perfect like my physiche

Questions?
>Email tdwyer@hawk.iit.edu
