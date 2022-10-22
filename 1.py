import imp
from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from random_words import RandomWords
from eth_account import Account
import time


def initMetaMaskWallet(driver):
  driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/welcome")
  driver.close()
  handles = driver.window_handles
  driver.switch_to.window(handles[-1])
  driver.find_element(By.XPATH,'//button[text()="开始使用"]').click()
  driver.find_element(By.XPATH,'//button[text()="我同意"]').click()
  driver.find_element(By.XPATH,'//button[text()="导入钱包"]').click()
  # 输入助记词
  inputs = driver.find_elements(By.XPATH,'//input')
  Account.enable_unaudited_hdwallet_features()
  acct,mnemonic = Account.create_with_mnemonic()
  print(acct.address)
  print(mnemonic.split())
  key = mnemonic.split()

  inputs[0].send_keys(key[0])
  inputs[2].send_keys(key[1])
  inputs[4].send_keys(key[2])
  inputs[6].send_keys(key[3])
  inputs[8].send_keys(key[4])
  inputs[10].send_keys(key[5])
  inputs[12].send_keys(key[6])
  inputs[14].send_keys(key[7])
  inputs[16].send_keys(key[8])
  inputs[18].send_keys(key[9])
  inputs[20].send_keys(key[10])
  inputs[22].send_keys(key[11])
  inputs[24].send_keys(PASSWARD)
  inputs[25].send_keys(PASSWARD)
  inputs[26].click()

  driver.find_element(By.XPATH,'//button[text()="导入"]').click()
  wait.until(lambda driver: driver.find_element(By.XPATH,'//button[text()="全部完成"]'))
  driver.find_element(By.XPATH,'//button[text()="全部完成"]').click()



EXTENSION_PATH = "/Users/lu/Library/Application Support/Google/Chrome/Default/Extensions/nkbihfbeogaeaoehlefnkodbefgpgknn/10.20.0_0.crx"
PASSWARD = '66666666'

# 导入小狐狸插件
opt = webdriver.ChromeOptions()
opt.add_extension(EXTENSION_PATH)
driver = webdriver.Chrome(chrome_options=opt)
wait = ui.WebDriverWait(driver,10)

#初始化小狐狸钱包
initMetaMaskWallet(driver)
print("小狐狸钱包初始化成功！")

# driver.quit()

