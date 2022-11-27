from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import json
driver = webdriver.Chrome(executable_path= "venv/chromedriver.exe")
driver.get("https://lms.ou.edu.vn/")

driver.find_element(By.CLASS_NAME,'main-btn').click()
driver.find_element(By.CLASS_NAME,'login100-form-btn').click()

user = Select(driver.find_element(By.ID,'form-usertype'))
user.select_by_index(0)

with open('data/account.json', encoding='utf-8') as f:
    acct = json.load(f)

print(acct)
print(acct["username"])
print(acct["password"])
driver.find_element(By.ID, 'form-username').send_keys(acct["username"])
driver.find_element(By.ID, 'form-password').send_keys(acct["password"])

# driver.find_element(By.ID, 'form-username').send_keys('2051010290')
# driver.find_element(By.ID, 'form-password').send_keys('0344142375')
driver.find_element(By.CLASS_NAME, 'm-loginbox-submit-btn').click()

# driver.implicitly_wait(3)
# courses = driver.find_elements(By.CSS_SELECTOR,".dashboard-card-deck .dashboard-card")
courses = WebDriverWait(driver,20).until(
    ec.presence_of_all_elements_located((By.CSS_SELECTOR,'.dashboard-card-deck .dashboard-card'))
)
for c in courses:
    print(c.text)


driver.save_screenshot('test.png')
driver.execute_script("window.scroll(0, 400)")
driver.save_screenshot('test2.png')

driver.quit()