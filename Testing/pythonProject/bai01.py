from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

kw = input("You keyword =")

service = Service(executable_path='.venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://dhthanhit.pythonanywhere.com/')

k = driver.find_element(By.NAME,'keyword')
k.send_keys(kw)

driver.find_element(By.CSS_SELECTOR,'nav button[type =submit]').click()
print(driver.title)

driver.implicitly_wait(5)
products = driver.find_elements(By.CLASS_NAME,'card')
for p in products:
    try:
        title = p.find_element(By.CLASS_NAME,'card-title')
        price = p.find_element(By.TAG_NAME,'p')
        img = p.find_element(By.TAG_NAME,'img')
    except:
        pass
    else:
        print(title.text)
        print(price.text)
        print(img.get_attribute('src'))

urls=[]
cates = driver.find_elements(By.CSS_SELECTOR, '.navbar-nav li')[1:-3]
for c in cates:
    print(c.text)
    urls.append(c.find_element(By.TAG_NAME,'a').get_attribute('href'))

print(urls)
driver.quit()

