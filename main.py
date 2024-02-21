from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3752324378&distance=25&f_AL=true&f_E=1%2C2%2C3&f_WT=2&geoId=104738515&keywords=Python&location=Irlanda&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
driver.maximize_window()
driver.implicitly_wait(3)

time.sleep(3)
log_in = driver.find_element(By.XPATH, value='/html/body/div[6]/a[1]')
log_in.click()

time.sleep(3)
email = driver.find_element(By.XPATH, value='//*[@id="username"]')
email.send_keys("")
password = driver.find_element(By.XPATH, value='//*[@id="password"]')
password.send_keys("")
login_button = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
login_button.click()

time.sleep(0)
skip = input("continue: ")

job_offers_div = driver.find_element(By.CSS_SELECTOR, value="div.jobs-search-results-list")

driver.execute_script("arguments[0].scrollIntoView(true);", job_offers_div)
driver.implicitly_wait(2)

# job_offers_tags = job_offers_div.find_elements(By.CSS_SELECTOR, value="a[aria-label][href][id][data-control-id]")
# job_offers_tags = WebDriverWait(driver, 10).until(
#     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[aria-label][href][id][data-control-id]"))
# )
job_offers_tags = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")


print(len(job_offers_tags))

for offer in job_offers_tags:
    time.sleep(5)
    driver.execute_script("arguments[0].scrollIntoView(true);", offer)
    offer.click()
    print(f"Click {offer.text}")
    time.sleep(10)
    try:
        save_offer = driver.find_element(By.XPATH, value="//button[contains(., 'Guardar')]")
        time.sleep(5)
        save_offer.click()
        print(f"Saved")
        time.sleep(5)
    except:
        print("Save button not found.")
    try:
        follow_button = driver.find_element(By.XPATH, value="//button[contains(., 'Seguir')]")
        driver.execute_script("arguments[0].scrollIntoView(true);", follow_button)
        follow_button.click()
        print(f"Followed")
        time.sleep(5)
    except:
        print("Follow button not found.")

# time.sleep(2)
# save_offer = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/button')
# save_offer.click()
#
# try:
#     follow_button = driver.find_element(By.XPATH, value='//*[@id="ember470"]/section/div[1]/div[1]/button')
#     follow_button.click()
# except:
#     print("Follow button not found.")
