import datetime
import androidhelper.sl4a as android
import time

def dateandtime ():
    """This funk return the date and current time"""
    date=datetime.datetime.now()
    Time=f"{date.strftime('%A %e %B')} {[date.strftime ('%T')]}" 
    return Time
    
def speak (stri):
    """This funk speaks the given string"""
    droid=android.Android ()
    print ("\n\n",stri)
    droid.ttsSpeak (stri)

def save (str):
    """This funk saves the information in a file"""
    with open ("Manage.txt","a") as f:
        #f.write (f"\n\n{str}")
        speak ("data updated")
        speak ("Learn something new today with 😁")

def myinfo ():
    """This funk gives the info about your exercises"""
    with open ("Manage.txt") as fp:
            days_went=0
            days_left=0
            reason_left=0
            content=fp.readlines ()[:]
         
            for items in content:
                if "DONE✔" in items:
                    days_went+=1
                
                elif "Left🛇" in items:
                    days_left+=1
                
                elif "Reason" in items:
                    reason_left+=1
                    
            speak (f"You started from 1st of August ")
            time.sleep (2.5)
            speak (f"And today is {dateandtime ()} ")  
            time.sleep (2.5)   
            speak (f"You went {days_went} days for exercise .")
            time.sleep (2.4)
            speak (f"Left {reason_left} days due to raining")
            time.sleep (2)
            speak (f"And left {days_left} days for that sleep")

def showinfo ():
    """Prints all the info of your exercise"""
    speak("listing all of your info.")
    with open ("Manage.txt","r") as f:
        for lines in f.readlines():
            print (lines)        

def reason():
    """The reason why you didn't go for exercise"""
    speak ("Why !")
    reason_left=input("--> ").capitalize ()
    if reason_left=="It was raining" or "raining" in reason_left:
        speak ("Then just, grab a cup and start exercise  at home")
        speak ("You can't afford to leave okay !, Remember !")
    else:
        speak ("Whatever....")
    return reason_left
        

if __name__=="__main__":
    
    speak (" Hello!  I am your exercise manager ")
    time.sleep(2)
    speak ("I can add your exercise, And say you the info. just type right here")
    time.sleep (3.5)
    
    user=input ("--> ").capitalize()
    
    if user=="Exercise" or "Add my exercise" in user:
        speak ("Okay did you go for exercise today")
        time.sleep (1)
        user_inp=input ("---> ").capitalize()
        
        if user_inp=="Yes":
            speak (" Everything's starts with tooday keep moving")
            date=dateandtime()
            info=f"{date} [DONE✔]"
            save(info)
          
        elif user_inp=="No":
            reason=reason ()
            if reason=="":
                speak (" Still Being an ashhole you bastard to skip the exercise?")  
                speak ("You refused to take control of yourself")
                date=dateandtime ()
                info=f"{date} [LEFT🛇]"
                save (info)
            else:
                date=dateandtime ()
                info=f"{date} [Left🛇]\nReason : '{reason}'"
                save(info)  
        
    elif user=="What's my info" or user=="My info" or user=="Info":
        speak ("Analysing ,Your info")
        myinfo ()
    
    elif user=="Show info" or user=="Show my info":
        showinfo ()
          
    else:
        speak (" Invalid input ! ")
        speak (" I can only accepts the above given criteria ")
     