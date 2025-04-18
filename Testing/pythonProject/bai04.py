import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex


service = Service(executable_path='.venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://tiki.vn/kem-duong-am-dang-gel-hada-labo-koi-gokujyun-perfect-gel-100g-p72711789.html?spid=72711790')

driver.execute_script('window.scroll(0,3000)')
time.sleep(2)
pages =WebDriverWait(driver,10).until(
    ex.presence_of_all_elements_located((By.CSS_SELECTOR, '.customer-reviews__pagination a'))
)

pages = pages[1:6]

for p in pages:
    p.click()
    print("-------------",p.text)
    time.sleep(2)
    comments = WebDriverWait(driver,10).until(
        ex.presence_of_all_elements_located((By.CLASS_NAME,'review-sub-comment__content'))
    )
    for c in comments:
            print(c.text)
    driver.save_screenshot(f'{p.text}.png')
driver.quit()