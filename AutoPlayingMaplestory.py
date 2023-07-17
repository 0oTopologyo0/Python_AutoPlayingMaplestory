import pyautogui
import time
import datetime
#載入相關模組

print(pyautogui.position())
pyautogui.moveTo(1335, 649, duration = 1.5) #用1.5秒移動到x=943，y=1063的位置
pyautogui.click(clicks=1, button='left') #單擊左鍵並且中途間隔0.5秒

pyautogui.press('enter')
pyautogui.press('1')
pyautogui.press('enter')
# #轉換畫面到楓之谷

# #設定自動練等迴圈
# Running = True
# count = 0

# while Running:
#     count = 0
#     pyautogui.press('left')
#     time.sleep(1)
#     # while count < 10:
#     #     pyautogui.keyDown('A')
#     #     count += 1
#     # count = 0
#     pyautogui.press('right')
#     # while count < 10:
#     #     pyautogui.keyDown('A')
#     #     count += 1
#     Running = False
