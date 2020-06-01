from pynput.mouse import Controller, Button
from pynput import keyboard
import time
mouse = Controller()
break_program = False

build_button_position = (0, 0)
treasure_hunt_shop_position = (0, 0)
treasure_hunt_position = (0, 0)
treasure_hunt_confirm_position = (0, 0)
level_up_position = (0, 0)
level_up_button_position = (0, 0)
sell_button_position = (0, 0)
confirm_position = (0, 0)
blank_space = (0, 0)
level = 2
rounds = 100

def positioning():
  global build_button_position
  global treasure_hunt_shop_position
  global treasure_hunt_position
  global treasure_hunt_confirm_position
  global level_up_position
  global level_up_button_position
  global sell_button_position
  global confirm_position
  global blank_space
  global level
  global rounds

  f = open("config","r")
  build_button_position = eval(f.readline())
  treasure_hunt_shop_position = eval(f.readline())
  treasure_hunt_position = eval(f.readline())
  treasure_hunt_confirm_position = eval(f.readline())
  level_up_position = eval(f.readline())
  level_up_button_position = eval(f.readline())
  sell_button_position = eval(f.readline())
  confirm_position = eval(f.readline())
  blank_space = eval(f.readline())
  level = int(f.readline())
  rounds = int(f.readline())
  f.close()

print("Auto clicker will start in 3...")
time.sleep(1)
print("Auto clicker will start in 2...")
time.sleep(1)
print("Auto clicker will start in 1...")
time.sleep(1)
print("Auto clicker starts.")

def on_press(key):
  global break_program
  if key == keyboard.Key.esc:
    print ("ESC was pressed...")
    break_program = True
    return False

count = 0

def clicking(waiting = 0.1):
  mouse.press(Button.left)
  time.sleep(0.1)
  mouse.release(Button.left)
  time.sleep(waiting)

def levelUp():
  global level
  count = 1
  while count < level:
    print("- Leveling up Treasure Hunt to Lv." + str(count + 1))
    mouse.position = treasure_hunt_position #pressing Treasure Hunt
    clicking()
    mouse.position = level_up_position #pressing Lv up
    clicking()
    mouse.position = level_up_button_position #pressing Level up
    clicking()
    mouse.position = confirm_position #confirm
    print(" -- Waiting")
    clicking(4)
    mouse.position = blank_space
    clicking(0.5)
    count += 1

positioning()
with keyboard.Listener(on_press=on_press) as listener:
  while break_program == False and count < rounds:
    count += 1
    #open up Build
    print("Start the loop #", count)
    print("- Opening up Build")
    mouse.position = build_button_position
    clicking(3)

    #click on Treasure Hunt
    print("- Selecting Treasure Hunt")
    mouse.position = treasure_hunt_shop_position
    time.sleep(1.5)
    clicking()
    clicking(3.5)

    #place Treasure Hunt on the map
    print("- Placing Treasure Hunt")
    mouse.position = treasure_hunt_position
    clicking()
    mouse.position = treasure_hunt_confirm_position
    print(" -- Waiting...")
    clicking(4)

    #upgrade
    levelUp()

    #sell Treasure Hunt
    print("- Selling Treasure Hunt")
    mouse.position = treasure_hunt_position #pressing Treasure Hunt
    mouse.press(Button.left)
    clicking(0.5)
    mouse.position = sell_button_position #pressing Sell
    clicking(0.5)
    mouse.position = confirm_position #confirm
    clicking(1.5)
    print("End the loop.")
  listener.join()
