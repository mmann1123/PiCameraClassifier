 
#GPIO Buttons
#The PiTFT comes with some built in options for button control (backlight and shut down), but I never really understood why as it’s easy to start your own Python script on boot to control whatever you want – much more fun!
#From left to right (buttons on the PiTFT), the GPIO numbering (GPIO.BCM) is as follows:
# 23 | 22 | 27 | 18
#The GPIO pins feeding these buttons are set high by default, so to trigger them you have to tell your script to look for ‘FALSE’…let me show you my script – copy it, tweak it, freak it – go for it! I’d love to hear what you’ve done with your PiTFT buttons.
#!/usr/bin/python  
  
 import RPi.GPIO as GPIO  
 import time    
 import os  
  
 #Set GPIO mode  
 GPIO.setmode(GPIO.BCM)  
  
 #Setup GPIO  
 GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
 GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
 GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
 GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
  
 #Set up backlight GPIO  
 os.system("sudo sh -c 'echo 252 &gt; /sys/class/gpio/export'")  
  
 #Give the system a quick break  
 time.sleep(0.5)  
  
 #Set the intitial counter value to zero  
 counter = 0 
  
 #var for the 'while' statement to keep it running  
 var = 1 
  
 #Main program  
 while var == 1:  
  if (GPIO.input(23) == False): #Backlight control
  
   if (counter == 0):  
    os.system("sudo sh -c 'echo 'out' &gt; /sys/class/gpio/gpio252/direction'")  
    counter = 1 
    print("counter now 1")  
    time.sleep(0.5)  
  
   elif (counter == 1) or (counter == 3):  
    os.system("sudo sh -c 'echo '1' &gt; /sys/class/gpio/gpio252/value'")  
    counter = 2 
    print("counter now 2")  
    time.sleep(0.5)  
  
   elif (counter == 2):  
    os.system("sudo sh -c 'echo '0' &gt; /sys/class/gpio/gpio252/value'")  
    counter = 3 
    print("counter now 3")  
    time.sleep(0.5)  
  
  if (GPIO.input(22) == False):  
   print("22 Working")  
   time.sleep(0.5)  
  
  if (GPIO.input(27) == False):  
   print("27 working")  
   time.sleep(0.5)  
  
  if (GPIO.input(18) == False): #Shutdown button  
   print("SHUTDOWN")  
   os.system("sudo halt")  
  
 GPIO.cleanup()