from gpiozero import Robot
from time import sleep

motor = Robot (left=(4,14), right=(24,25))
  motor.left()
  sleep(5)
  motor.stop()
  
