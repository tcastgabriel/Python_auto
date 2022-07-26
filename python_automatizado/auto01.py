import pyautogui #automatizar
import pyperclip
import time

#Delay
pyautogui.PAUSE = 1
#pressiona a tecla do Windows
pyautogui.press("win")
#Escreve o nome do navegador
pyautogui.write("Opera")
#entra no navegador
pyautogui.press("enter")

pyautogui.write("Youtube")

pyautogui.press("enter")
# site ta carregando
time.sleep(5)











