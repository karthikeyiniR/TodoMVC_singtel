import time
import requests
import uuid
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = "http://todomvc.com/examples/vue/"

driver = webdriver.Chrome('D:\Python3\chromedriver.exe')
driver.get(url)
driver.maximize_window()

#Add Task--------------------------------------------------------------------------------------------------------------------------------------
AddTask = driver.find_element_by_css_selector('body > section > header > input')

AddtaskItem =['Singtel_Task11','Singtel_Task12','Singtel_Task13','Singtel_Task14','Singtel_Task15']
for content in AddtaskItem:
    Result = AddTask.send_keys(content)
    AddTask.send_keys(Keys.ENTER)
    print(Result)
    time.sleep(1)

SelectAllTask = driver.find_element_by_css_selector('body > section > section > label')
SelectAllTask.click()
time.sleep(1)
DeselectAllTask = driver.find_element_by_css_selector('body > section > section > label')
DeselectAllTask.click()
#Complete Task-----------------------------------------------------------------------------------------------------------------------------------
CompleteTask1 = driver.find_element_by_css_selector('body > section > section > ul > li:nth-child(1) > div > input').click()
time.sleep(1)
#updateTask=driver.find_element_by_css_selector('body > section > section > ul > li:nth-child(2) > div > label')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/section/section/ul/li[2]/div/label'))).click()

#Remove Completed Task from the task list----------------------------------------------------------------------------------------------------------
ClearcompletedTask = driver.find_element_by_xpath('/html/body/section/footer/button')
print("ClearedcompletedTask")
CompletedTasklist = ClearcompletedTask.click()
time.sleep(2)

#Get Task name Ex:Singtel_Task12 from task list----------------------------------------------------------------------------------------------------

obj= driver.find_element_by_xpath('/html/body/section/section/ul/li[2]/div/label')
print("GetTaskName " + obj.text)
#View Completed Task-Singtel_Task14-----------------------------------------------------------------------------------------------------------------
CompleteTask2 = driver.find_element_by_xpath('/html/body/section/section/ul/li[3]/div/input').click()
print(CompleteTask2)
ViewCompletedTask =driver.find_element_by_css_selector('body > section > footer > ul > li:nth-child(3) > a').click()
time.sleep(3)
#View Active Task-----------------------------------------------------------------------------------------------------------------------------------
ViewActiveTask= driver.find_element_by_xpath('/html/body/section/footer/ul/li[2]/a').click()
#print(ViewActiveTask.text)
time.sleep(3)
#View All Task-----------------------------------------------------------------------------------------------------------------------------------
ViewAllTask= driver.find_element_by_xpath('/html/body/section/footer/ul/li[1]/a').click()
print(ViewAllTask)
time.sleep(5)
driver.close()


