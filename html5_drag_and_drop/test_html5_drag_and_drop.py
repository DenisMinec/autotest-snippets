# coding: utf-8
from selenium import webdriver
from time import sleep

# подгружаем jquery (http://code.jquery.com/jquery-1.11.2.min.js)
jQuery = None
with open('jquery-1.11.2.js') as f:
    jQuery = f.read()

# подгружаем скрипт эмуляции (https://gist.github.com/rcorreia/2362544)
script = None
with open('drag_and_drop_helper.js') as f:
    script = f.read()

# создаем функцию, которой можно будет пользоваться в любом месте
def perform_html5_drag_and_drop(driver, source_css_selector, target_css_selector):
    driver.execute_script(jQuery)
    driver.execute_script(script)
    driver.execute_script(
        "$('%(source)s').simulateDragDrop({dropTarget: '%(target)s'});" % {
            'source': source_css_selector,
            'target': target_css_selector
        }
    )

driver = webdriver.Firefox()
driver.get('http://html5demos.com/drag')

# подгружаем jQuery
driver.execute_script(jQuery)

# подгружаем скрипт
driver.execute_script(script)

# выполдняем перетаскивание с задержкой (для демо)
for source in ('#one', '#two', '#three', '#four', '#five'):
    sleep(1)
    perform_html5_drag_and_drop(driver, source, '#bin')
