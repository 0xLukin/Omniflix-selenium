import imp
from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from random_words import RandomWords
from eth_account import Account
import time


def initKeplrWallet(driver,EXTENSION_ID,PASSWARD,wait):
  driver.get('chrome-extension://{}/popup.html#/register'.format(EXTENSION_ID))

  # driver.close()
  # handles = driver.window_handles
  # driver.switch_to.window(handles[-1])

  driver.find_element(By.XPATH,'//button[text()="Import existing account"]').click()

  # # 输入助记词
  inputs = driver.find_elements(By.XPATH,'//input')
  Account.enable_unaudited_hdwallet_features()
  acct,mnemonic = Account.create_with_mnemonic()
  print(acct.address)
  print(mnemonic.split())
  key = mnemonic.split()

  inputs[0].send_keys(key[0])
  inputs[1].send_keys(key[1])
  inputs[2].send_keys(key[2])
  inputs[3].send_keys(key[3])
  inputs[4].send_keys(key[4])
  inputs[5].send_keys(key[5])
  inputs[6].send_keys(key[6])
  inputs[7].send_keys(key[7])
  inputs[8].send_keys(key[8])
  inputs[9].send_keys(key[9])
  inputs[10].send_keys(key[10])
  inputs[11].send_keys(key[11])
  inputs[12].send_keys("Main")
  inputs[13].send_keys(PASSWARD)
  inputs[14].send_keys(PASSWARD)

  driver.find_element(By.XPATH,'//button[text()="Next"]').click()
  wait.until(lambda driver: driver.find_element(By.XPATH,'//button[text()="Done"]'))
  # driver.find_element(By.XPATH,'//button[text()="Done"]').click()
  driver.get('chrome-extension://{}/popup.html#/'.format(EXTENSION_ID))
 
def addUser(num):
  EXTENSION_PATH = "/Users/lu/Library/Application Support/Google/Chrome/Default/Extensions/dmkamcknogkgcdfhhbddcghachkejeap/0.11.12_0.crx"
  EXTENSION_ID = "dmkamcknogkgcdfhhbddcghachkejeap"
  PASSWARD = '66666666'

  # 导入小狐狸插件
  opt = webdriver.ChromeOptions()
  opt.add_argument("--user-data-dir=/Users/lu/Library/Application Support/Google/Chrome/Default/{}".format(num))
  opt.add_extension(EXTENSION_PATH)
  driver = webdriver.Chrome(chrome_options=opt)
  wait = ui.WebDriverWait(driver,10)

  #初始化Keplr钱包
  initKeplrWallet(driver,EXTENSION_ID,PASSWARD,wait)
  print("Keplr钱包初始化成功！")
  driver.execute_script("window.open('https://baidu.com','_blank');")
  handles = driver.window_handles
  driver.switch_to.window(handles[1])
  driver.quit()

for i in range(5,10,1):
  print(i)
  addUser(str(i))

