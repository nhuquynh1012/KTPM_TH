from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex

service = Service(executable_path='.venv/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://dhthanhit.pythonanywhere.com/')

products = driver.find_elements(By.CLASS_NAME,'card')
urls= []
for p in products:
        title = p.find_element(By.CLASS_NAME,'card-title')
        print(title.text)
        b = p.find_element(By.CSS_SELECTOR,'a.btn.btn-primary')
        urls.append(b.get_attribute('href'))

for u in urls:
    print(u)#link cua trang chi tiet san pham

    driver.get(u)# chuyển từng trang theo url
    coments = WebDriverWait(driver,10).until(#Câu lệnh này bảo Selenium chờ tối đa 10 giây
        # để phần tử xuất hiện.Nếu phần tử xuất hiện trong vòng 10 giây → tiếp tục.Nếu sau 10 giây không thấy gì → báo lỗi TimeoutException.
        ex.presence_of_all_elements_located((By.CSS_SELECTOR,'#comments li p'))#Đây là điều kiện chờ: tìm tất cả các thẻ <p> nằm trong <li> bên trong phần tử có id="comments".
    )

    for c in coments:
        print(c.text)
driver.quit()

