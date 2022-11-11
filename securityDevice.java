import java.util.Scanner;
import java.util.*;

public class securityDevice {
    Scanner input = new Scanner(System.in);
        // System.out.println("Please input your key");
        String code = input.nextLine();
        boolean search = false;

        int in;
        public void find() {
            while (!search) {
                try {
                    input.skip("[^0-9]*");
                    in = input.nextInt();
                    search = true;
                } catch (InputMismatchException e) {
                    search = false;
                }
            }
        }

   public String passcode = "83363";
    boolean isLocked = true;

   public String toString(){
        if(isLocked){
            return "The Keypad is Locked";
        }
        else{
            return "The Keypad is Unlocked";
        }
    }
    public void checkLock() {
        if (code.contains(passcode)) {
            if (code.indexOf(passcode) == 1) {
                isLocked = false;
                System.out.println("The Keypad is Unlocked");
            } else if (code.indexOf(passcode) == 4) {
                isLocked = true;
                System.out.println("The Keypad is Locked");
            }
        }
    }
}
