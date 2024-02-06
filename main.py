import pyautogui  # Importa a biblioteca pyautogui para automação
import time       # Importa a biblioteca time para manipulação de tempo

time.sleep(3)      # Pausa a execução por 3 segundos

pyautogui.press('win')  # Simula a pressionar da tecla 'Win' (tecla do Windows)
time.sleep(1)

pyautogui.write('leag')  # Digita 'leag'
time.sleep(1)

pyautogui.press('enter')  # Simula a pressionar da tecla 'Enter'
time.sleep(7)

pyautogui.write('usuarioteste')  # Digita 'usuarioteste'
pyautogui.press('tab')  # Simula a pressionar da tecla 'Tab' (avança para o próximo campo)
time.sleep(1)

pyautogui.write('teste')  # Digita 'teste'
time.sleep(3)

pyautogui.click(x=403, y=542)  # Simula um clique do mouse nas coordenadas (403, 542)
time.sleep(1)

pyautogui.press('tab')  # Simula a pressionar da tecla 'Tab' (avança para o próximo campo)
pyautogui.press('enter')  # Simula a pressionar da tecla 'Enter'
