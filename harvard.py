# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup as bs

username = 'test@gmail.com'
password = 'test'

time_sleep = 0.05
time_out = 5
def wait_for_load(cond, driver): # wait for loading info
    cnt = time_out / time_sleep # max try
    while cond(driver) and cnt > 0:
        sleep(time_sleep)
        cnt -= 1

def load_cond(driver):
    return len(bs(driver.page_source, 'html.parser').findAll(id='semester_m')) == 0

math_courses = '''
Calculus A(1)
Calculus A(2)
Linear Algebra(1)
Linear Algebra(2)
Introduction to Complex Analysis
Stochastic Mathematical Methods
Numerical Analysis
'''.split('\n')[:-1]

english_courses = '''
Listening & Speaking for Academic Purposes (1)
Listening & Speaking for Academic Purposes (2)
Listening & Speaking for Academic Purposes (3)
Listening & Speaking for Academic Purposes (4)
Foreign Language Application
Reading & Writing for Argumentative Essays
Art English(1)
Art English(2)
'''.split('\n')[:-1]

if __name__ == "__main__":
    driver = webdriver.Chrome()
    # login
    driver.get("https://apply.gsas.harvard.edu/account/login")
    driver.find_element_by_id("email").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Forgot Your Password?'])[1]/following::button[1]").click()
    driver.get('https://apply.gsas.harvard.edu/apply/aca')
    driver.find_element_by_link_text("Add Course").click()
    # load courses
    raw = open('course.txt').read().split('\n')[:-1]
    for s in raw:
        print(s)
        c = s.split('\t')
        t = c[5].split('-')
        mm = {'Autumn': 'September', 'Summer': 'July', 'Spring': 'February'}[t[1]]
        sleep(2)
        wait_for_load(load_cond, driver)
        Select(driver.find_element_by_id("semester_m")).select_by_visible_text(mm)
        Select(driver.find_element_by_id("semester_y")).select_by_visible_text(t[0])
        driver.find_element_by_id("name").send_keys(c[1])
        Select(driver.find_element_by_id("level")).select_by_visible_text("Undergraduate")
        driver.find_element_by_id("number").send_keys(c[0])
        driver.find_element_by_id("grade").send_keys(c[3])
        Select(driver.find_element_by_id("courses_foreign_language")).select_by_visible_text("Yes" if c[1] in english_courses else "No")
        Select(driver.find_element_by_id("courses_mathematics")).select_by_visible_text("Yes" if c[1] in math_courses else "No")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Save'])[1]/following::button[1]").click()
    
