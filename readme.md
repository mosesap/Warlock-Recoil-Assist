# Warlock Configurable Recoil Control

**Disclaimer:** Use this at your own risk. A basic anti-cheat _should_ detect a program like this.

**Dependancies:** playsound, pypiwin32, pywin32

**Set up:** Configure anti-recoil arrays in guns.json. A very basic Kilo array has been preconfigured. 

-1 moves your cursor left on the x-axis  
1 moves your cursor right on the x-axis  
-1 moves your cursor  up on the y-axis  
1 moves your cursor down on the y-axis  

Do not forget to configure the gun's rate of fire in RPM. The script will move your mouse down by the pre-configured amount each time the gun fires.


**Controls:** 

INSERT: enable/disable  
DELETE: stop execution  
H: Hold to select gun from guns.json. You will hear 3 hitmarker sounds once you are able to select a gun.  
1 thru 0: After holding H press a number to select a re-configured gun. You will hear 2 hitmarker sounds once a gun is selected.
1 or 2: Once a gun has been selected, 1 or 2 can be pressed to disable/enable the script (in addition to INSERT), simulating a weapon change. _Most secondaries do not require recoil control._  
