# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select

username = 'test@gmail.com'
password = 'test'

if __name__ == "__main__":
    driver = webdriver.Chrome()
    # login
    driver.get("https://www.lehrbetrieb.ethz.ch/eApply/ealogin.view?lang=en")
    driver.find_element_by_name("ea_mail").send_keys(username)
    driver.find_element_by_name("ea_password").send_keys(password)
    driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Forgot your password?'])[1]/following::input[1]").click()
    driver.get("https://www.lehrbetrieb.ethz.ch/eApply/overview.view?indx=0")
    driver.find_element_by_link_text("Courses").click()
    # load courses
    raw = open('course.txt').read().split('\n')[:-1]
    for s in raw:
        print(s)
        c = s.split('\t')
        driver.find_element_by_id("add").click()
        Select(driver.find_element_by_id("subjectCategory")).select_by_visible_text("Course")
        driver.find_element_by_id("title").send_keys(c[1])
        driver.find_element_by_id("academicYear").send_keys(c[5].split('-')[0])
        driver.find_element_by_id("courseNumber").send_keys(c[0])
        driver.find_element_by_id("weeks").send_keys(c[9])
        driver.find_element_by_id("hoursTutorial").send_keys(c[6])
        driver.find_element_by_id("hoursLectures").send_keys(c[7])
        driver.find_element_by_id("hoursPracticalWork").send_keys(c[8])
        driver.find_element_by_id("grade").send_keys(c[3])
        driver.find_element_by_id("credits").send_keys(c[2])
        driver.find_element_by_id("store").click()
