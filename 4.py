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
ACCOUNT_NAME = "5"

opt = webdriver.ChromeOptions()
opt.add_argument("--lang=zh-CN")
opt.add_argument("--user-data-dir=/Users/lu/Library/Application Support/Google/Chrome/Default/2")
opt.add_extension(EXTENSION_PATH)
driver = webdriver.Chrome(chrome_options=opt)
wait = ui.WebDriverWait(driver,10)
driver.get('chrome-extension://{}/popup.html#/'.format(EXTENSION_ID))
# driver.get('https://f4.omniflix.studio/')
# driver.execute_script("window.open('https://f4.omniflix.studio/');")
driver.find_element(By.XPATH,'//input').send_keys('66666666')
driver.find_element(By.XPATH,'//button[text()="Unlock"]').click()
time.sleep(2)
driver.get('chrome-extension://{}/popup.html#/register'.format(EXTENSION_ID))

driver.find_element(By.XPATH,'//button[text()="Import existing account"]').click()

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
inputs[12].send_keys(ACCOUNT_NAME)
# inputs[13].send_keys(PASSWARD)
# inputs[14].send_keys(PASSWARD)

driver.find_element(By.XPATH,'//button[text()="Next"]').click()
wait.until(lambda driver: driver.find_element(By.XPATH,'//button[text()="Done"]'))
# driver.find_element(By.XPATH,'//button[text()="Done"]').click()
driver.get('chrome-extension://{}/popup.html#/setting/set-keyring'.format(EXTENSION_ID))
account = driver.find_elements(By.CLASS_NAME,'container-2uHDJYw0Nr96cUDJhKob26')
account[-1].click()
time.sleep(2)

# 连接
driver.get('https://f4.omniflix.studio/')
driver.find_element(By.XPATH,'//*[@id="scroll-bar"]/div/div[2]/div/button').click()
time.sleep(3)

driver.switch_to.window(driver.window_handles[-1]) #keplr
wait.until(lambda driver: driver.find_element(By.XPATH,'//button[text()="Approve"]'))
time.sleep(2)
driver.find_element(By.XPATH,'//button[text()="Approve"]').click()
time.sleep(2)

# driver.switch_to.window(driver.window_handles[-1]) #keplr
# wait.until(lambda driver: driver.find_element(By.XPATH,'//button[text()="Approve"]'))
# time.sleep(2)
# driver.find_element(By.XPATH,'//button[text()="Approve"]').click()
# time.sleep(2)

# driver.switch_to.window(driver.window_handles[-1]) #keplr
# wait.until(lambda driver: driver.find_element(By.XPATH,'//button[text()="Approve"]'))
# time.sleep(2)
# driver.find_element(By.XPATH,'//button[text()="Approve"]').click()
# time.sleep(2)
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

# driver.switch_to.window(driver.window_handles[-1]) #keplr
# wait.until(lambda driver: driver.find_element(By.XPATH,'//button[text()="Approve"]'))
# time.sleep(2)
# driver.find_element(By.XPATH,'//button[text()="Approve"]').click()
# time.sleep(2)

# driver.switch_to.window(driver.window_handles[-1]) #keplr
# wait.until(lambda driver: driver.find_element(By.XPATH,'//button[text()="Approve"]'))
# time.sleep(2)
# driver.find_element(By.XPATH,'//button[text()="Approve"]').click()
# time.sleep(2)

#任务一：领flix
driver.switch_to.window(driver.window_handles[0]) #dapp
wait.until(lambda driver: driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/div/div[1]/button'))
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/div/div[1]/button').click()
driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/div/div[2]/button').click()
time.sleep(5)
#任务二：创建nft集合
driver.get('https://f4.omniflix.studio/createCollection')
driver.find_element(By.XPATH,'//*[@id="collection-symbol"]').send_keys(key[0])
driver.find_element(By.XPATH,'//*[@id="collection-name"]').send_keys(key[0])
driver.find_element(By.XPATH,'//*[@id="scroll-bar"]/div/div[2]/form/button').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/div[2]/button[2]').click()
time.sleep(2)

driver.switch_to.window(driver.window_handles[-1]) #keplr
wait.until(lambda driver: driver.find_element(By.XPATH,'//button[text()="Approve"]'))
time.sleep(2)
driver.find_element(By.XPATH,'//button[text()="Approve"]').click()
time.sleep(6)

#任务上传图片：参与拍卖
driver.switch_to.window(driver.window_handles[0]) #dapp
driver.get('https://f4.omniflix.studio/library')
# driver.quit()