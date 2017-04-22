# -*- coding: utf-8 -*
# Zaimportowanie modułu webdriver

from selenium import webdriver
import time

#Stwórz nową sesję Firefox
driver = webdriver.Firefox()
#Maksymalizuj okno
driver.maximize_window()
#Przejdz do strony www.wsb.pl
driver.get("http://www.wsb.pl")
#Poczekaj 5 sekund
#Bardzo zła metoda - są specjalne waity
time.sleep(5)
#Zamknij okno
driver.quit()
