import imp
from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from random_words import RandomWords
from eth_account import Account
import time

EXTENSION_PATH = "/Users/lu/Library/Application Support/Google/Chrome/Default/Extensions/dmkamcknogkgcdfhhbddcghachkejeap/0.11.12_0.crx"
EXTENSION_ID = "dmkamcknogkgcdfhhbddcghachkejeap"

opt = webdriver.ChromeOptions()

opt.add_argument("--lang=zh-CN")
opt.add_argument("--user-data-dir=/Users/lu/Library/Application Support/Google/Chrome/Default/2")
opt.add_extension(EXTENSION_PATH)
driver = webdriver.Chrome(chrome_options=opt)
wait = ui.WebDriverWait(driver,10)
driver.get('https://f4.omniflix.studio/')
# driver.execute_script("window.open('https://f4.omniflix.studio/');")

# 连接
driver.find_element(By.XPATH,'//*[@id="scroll-bar"]/div/div[2]/div/button').click()
time.sleep(1)

driver.switch_to.window(driver.window_handles[-1]) #keplr
driver.find_element(By.XPATH,'//input').send_keys('66666666')
driver.find_element(By.XPATH,'//button[text()="Unlock"]').click()
time.sleep(2)

driver.switch_to.window(driver.window_handles[0]) #dapp
driver.get('https://f4.omniflix.studio/')
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="scroll-bar"]/div/div[2]/div/button').click()
time.sleep(2)

driver.switch_to.window(driver.window_handles[-1]) #keplr
wait.until(lambda driver: driver.find_element(By.XPATH,'//button[text()="Approve"]'))
time.sleep(2)
driver.find_element(By.XPATH,'//button[text()="Approve"]').click()
time.sleep(2)

driver.switch_to.window(driver.window_handles[-1]) #keplr
wait.until(lambda driver: driver.find_element(By.XPATH,'//button[text()="Approve"]'))
time.sleep(2)
driver.find_element(By.XPATH,'//button[text()="Approve"]').click()
time.sleep(2)

driver.switch_to.window(driver.window_handles[-1]) #keplr
wait.until(lambda driver: driver.find_element(By.XPATH,'//button[text()="Approve"]'))
time.sleep(2)
driver.find_element(By.XPATH,'//button[text()="Approve"]').click()
time.sleep(2)
# 进入nft任务区
driver.switch_to.window(driver.window_handles[0]) #dapp
wait.until(lambda driver: driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div/button'))
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="scroll-bar"]/div/div/div[1]').click()
#进入小喇叭
wait.until(lambda driver: driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/button[3]'))
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/button[3]').click()
#任务一：领水按钮
wait.until(lambda driver: driver.find_element(By.XPATH,'//*[@id="scroll-bar"]/div/div/div[1]/div/button'))
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="scroll-bar"]/div/div/div[1]/div/button').click()
time.sleep(2)

driver.switch_to.window(driver.window_handles[-1]) #keplr
wait.until(lambda driver: driver.find_element(By.XPATH,'//button[text()="Approve"]'))
time.sleep(2)
driver.find_element(By.XPATH,'//button[text()="Approve"]').click()
time.sleep(2)

driver.switch_to.window(driver.window_handles[-1]) #keplr
wait.until(lambda driver: driver.find_element(By.XPATH,'//button[text()="Approve"]'))
time.sleep(2)
driver.find_element(By.XPATH,'//button[text()="Approve"]').click()
time.sleep(2)

#任务一：领flix
driver.switch_to.window(driver.window_handles[0]) #dapp
wait.until(lambda driver: driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/div/div[1]/button'))
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/div/div[1]/button').click()
#任务一：领SPAY
wait.until(lambda driver: driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/div/div[2]/button'))
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/div/div[2]/button').click()


# driver.quit()