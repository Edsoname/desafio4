import pyautogui
import pyperclip

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','V')
pyautogui.moveTo(908,204, duration=2)
pyautogui.click()
escrever_frase('A automação é incrivel!')

