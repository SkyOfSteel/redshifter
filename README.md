# RedShift Reader

A script to quickly export tables from serverless RedShift workgroups with SSO access.

## Overview

After launching main_icon.pyw, the function works in the background and listens to mouse clicks and keyboard presses. 

If a user has been idle for 240 seconds, the function simulates a combination of movements and presses and continues to listen to the input. The key presses include the Shift and left/right arrow keys.

When a user-submitted input is detected, the timer resets to 240 seconds again.

## Usage

1. main_icon.pyw - launches a systray version that works in the background and stops after right-clicking the icon and clicking "Quit".

2. main_old.py - (outdated) launches the terminal version that stays windowed and continues to work until closed.

## Known Issues

Running the script prevents the computer from fully going to sleep - the screen turns dark, but the hard drive keep working. The current workaround is to manually quit the script whenever you need to hibernate/sleep.