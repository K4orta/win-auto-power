import win32gui
import win32con
import time
from datetime import datetime

SC_MONITORPOWER = 0xF170
POWER_ON = -1
POWER_OFF = 2

display_on = True

# Returns True or False 
def check():
	now = datetime.now()

	# Check if it's the weekend
	if now.weekday() < 1 or now.weekday() > 5: 
		return False

	# Check if it's beteen the hours of 7:00pm and 7:00am 
	if now.hour > 16 or now.hour < 7:
		return False

	# If we passed the above tests the screen should be on
	return True

def change_display_state(next_state):
	if next_state: 
		win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, SC_MONITORPOWER, POWER_ON)
		display_on = True
	else:
		win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, SC_MONITORPOWER, POWER_OFF)
		display_on = False

def main():
	while True:
		# Check to see if the display should be on or off
		next_display_state = check()

		# If the display state is different from what it is currently, we need to turn it on of off
		if next_display_state != display_on:
			change_display_state(next_display_state)
		
		time.sleep(60)

if __name__ == "__main__":
	main() 
