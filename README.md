# Valkyrie Crusade - Automated leveling-up

<img src='https://lh3.googleusercontent.com/75feyTD9lq02u_2leJwdwkzjOj1YfYBNa5NZHPT-PQ4CSnugxeAGfdTT89uj3G2YNp2C=s180-rw' height='70'> 

[Valkyrie Crusade](https://play.google.com/store/apps/details?id=com.nubee.valkyriecrusade&hl=en)

Since I am lazy to level up the kingdom myself, here you go, the script for leveling up your kingdom on a emulator.

The concept is pretty easy: the script will be building and selling Treasure Hunt until you level up.

## Explaination
It is pretty simple python codes here. Firstly, it requires you to setup the environment of your Bluestacks (or whatever you use). There are 11 variables you need to setup:
```
build_button_position - where the build button position is
treasure_hunt_shop_position - where Treasure Hunt is on the shop
treasure_hunt_position - where Treasure Hunt will be placed
treasure_hunt_confirm_position - where the checking mark on top of Treasure Hunt is
level_up_position - where Lv up button on Treasure Hunt's menu is
level_up_button_position - where Level up button on Treasure Hunt's window is
sell_button_position - where Sell button on Treasure Hunt's menu is
confirm_position - where confirm button on pop-up is
blank_space - where there is no structure
level - level of Treasure Hunt that will be leveled up to before selling it (default is 2)
rounds - how many rounds you want to run (default is 100)
```
To setup, you need to run setup.py file and place your mouse on where those positions need to be, then press enter.
[vdo link will be available later]
To run the script, you just need to run client.py and leave your screen.

## Requirement
- Python3
- Emulator (such as Bluestacks)

## Setup
```bash
python ./setup.py
```

## Start the script
```bash
python ./client.py
```

## Download already built files
In case you don't have Python on your computer, [here](https://drive.google.com/drive/folders/1YO1RCV9mzByC2mQc2eC9GK7NIGCAK_xS?usp=sharing) is the exe files. Double click the files to use.
