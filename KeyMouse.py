import pyautogui
import time
import pyperclip

space_loc = (239, 927)
time.sleep(2)
print("start")
print("current location:",pyautogui.position())

pyautogui.moveTo(space_loc[0],space_loc[1])
time.sleep(1)
pyautogui.click()
pyautogui.press('a')
# pyautogui.click()
pyperclip.copy('要输入的汉字')  # 先复制a要输入的汉字Hello world!a要输入的汉字Hello world!
pyperclip.paste()
pyautogui.mouseDown()
time.sleep(4)
pyautogui.mouseUp()
