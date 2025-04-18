from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path='.venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://dhthanhit.pythonanywhere.com/')

driver.implicitly_wait(2)
urls = []
name =[]
cates = driver.find_elements(By.CSS_SELECTOR,'.navbar-nav li')[1:-3]#bỏ 1 ô đầu tiên và 3 ô cuối cùng 
for c in cates:
    name.append(c.text)
    urls.append(c.find_element(By.TAG_NAME,'a').get_attribute('href'))

for u,n in zip(urls,name):
    print("============")
    print(n)#tên loại sản phẩm ví dụ laptop , điện thoại, tivi
    driver.get(u)#truy cập vào trang của loại sản phẩm tương ứng ví dụ như điện thoại vào trang điện thoại lấy tên sản phâmr giá hình ảnh

    time.sleep(2)
    products = driver.find_elements(By.CLASS_NAME,'card')
    for p in products:
        try:
            title = p.find_element(By.CLASS_NAME,'card-title')
            price = p.find_element(By.CLASS_NAME,'card-text')
            img = p.find_element(By.TAG_NAME,'img')
        except:
            pass
        else:
            print(title.text)
            print(price.text)
            print(img.get_attribute('src'))

driver.quit()