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

if __name__ == "__main__":
    driver = webdriver.Chrome()
    # login
    driver.get("https://apply-psd.uchicago.edu/account/login?r=https%3a%2f%2fapply-psd.uchicago.edu%2fapply%2faca")
    driver.find_element_by_id("_pc_1").click()
    driver.find_element_by_id("email").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Forgot Your Password?'])[1]/following::button[1]").click()
    driver.find_element_by_link_text("Education").click()
    driver.find_element_by_link_text("Add Course").click()
    # load courses
    raw = open('course.txt').read().split('\n')[:-1]
    for s in raw:
        print(s)
        c = s.split('\t')
        t = c[5].split('-')
        mm = {'Autumn': 'September', 'Summer': 'July', 'Spring': 'February'}[t[1]]
        sleep(1)
        wait_for_load(load_cond, driver)
        Select(driver.find_element_by_id("semester_m")).select_by_visible_text(mm)
        Select(driver.find_element_by_id("semester_y")).select_by_visible_text(t[0])
        driver.find_element_by_id("name").send_keys(c[1])
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Save'])[1]/following::button[1]").click()
