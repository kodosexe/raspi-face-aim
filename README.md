#Raspi Face Aim

This is a program that looks for faces in real time from a USB webcam feed, trying to center it in the frame by outputting instructions through the GPIO pins.
Directions on the pinout to follow, but it is self Explanatory.

You will need OpenCV2 with all it's dependencies installed.

A variable ending with OF means ON-OFF, so whether the motor should be enabled.
A variable ending with DIR means Direction, so in what direction the motor should turn.

This program can be used with my ArduinoVexRobotControl repo, as it was designed to work together, but you can build your own interface.



I DO NOT TAKE ANY RESPONSIBILITY FOR THE CODE, IT'S FUNCTIONALITY, OR IT'S EFFECTS. I ASSUME NO LIABILITY FOR ANY DAMAGE DONE TO YOURS OR SOMEONE ELSES SYSTEM CAUSED DIRECTLY OR INDIRECTLY BY THIS CODE, IT'S HANDLING OR ANY OTHER ASPECT.
