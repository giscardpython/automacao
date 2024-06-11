import pyautogui as auto
import time
import logging

auto.PAUSE = 0.7

#abre o menu iniciar
auto.press('win')

#abre o chrome
auto.write('chrome')
auto.press('enter')

#maximizar a tela
auto.hotkey('alt', 'space')
auto.press('x')

#abre o github
auto.write('github.com')
auto.press('enter')

#aguarda 3 segundos 

time.sleep(3) 

#abre o classroom em uma nova guia
auto.hotkey('ctrl', 't')

auto.write('classroom.google.com')
auto.press('enter')
