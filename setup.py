from pynput.mouse import Controller, Button
mouse = Controller()

print('build_button_position: Build button on the left bottom side of the screen', end='')
next = input()
build_button_position = mouse.position
print(mouse.position)

print('treasure_hunt_shop_position: Treasure Hunt building on the shop', end='')
next = input()
treasure_hunt_shop_position = mouse.position
print(mouse.position)

print('treasure_hunt_position: Where Treasure Hunt is going to be placed', end='')
next = input()
treasure_hunt_position = mouse.position
print(mouse.position)

print('treasure_hunt_confirm_position: Treasure Hunt checked button', end='')
next = input()
treasure_hunt_confirm_position = mouse.position
print(mouse.position)

print('level_up_position: Lv up button on Treasure Hunt\'s menu', end='')
next = input()
level_up_position = mouse.position
print(mouse.position)

print('level_up_button_position: Level up button on Treasure Hunt\'s window', end='')
next = input()
level_up_button_position = mouse.position
print(mouse.position)

print('sell_button_position: Sell button on Treasure Hunt\' menu', end='')
next = input()
sell_button_position = mouse.position
print(mouse.position)

print('confirm_position: Confirm button', end='')
next = input()
confirm_position = mouse.position
print(mouse.position)

print('blank_space: Blank space', end='')
next = input()
blank_space = mouse.position
print(mouse.position)

print('level: Max level (default is 2): ', end='')
level = input()
if level == '':
  level = '2'
print(level)

print('rounds: How many rounds per run (default is 100): ', end='')
rounds = input()
if rounds == '':
  rounds = '100'
print(rounds)

f = open("config","w")
f.write(str(build_button_position) + '\n' +
     str(treasure_hunt_shop_position) + '\n' +
     str(treasure_hunt_position) + '\n' +
     str(treasure_hunt_confirm_position) + '\n' +
     str(level_up_position) + '\n' +
     str(level_up_button_position) + '\n' +
     str(sell_button_position) + '\n' +
     str(confirm_position) + '\n' +
     str(blank_space) + '\n' +
     level + '\n' + rounds)
f.close()

print('All completed. Please run client.py to start the script.\n**PRESS ANY KEY TO EXIT**')
input()
