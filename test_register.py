from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 設定 WebDriver
driver = webdriver.Edge()  # 如果你用 Chrome, 可以改為 webdriver.Chrome()
driver.get("http://127.0.0.1:5000/register")  # 你的 Flask 註冊頁面

# 等待網頁加載
time.sleep(2)

# 找到 Email 和 密碼的輸入框，並輸入測試帳號
email_input = driver.find_element(By.NAME, "email")
password_input = driver.find_element(By.NAME, "password")

email_input.send_keys("test@example.com")
password_input.send_keys("Test1234")

# 找到註冊按鈕，並點擊
register_button = driver.find_element(By.CSS_SELECTOR, "button.btn-success")
register_button.click()

# 等待頁面載入，確保有時間顯示 flash 訊息
time.sleep(3)

# 截圖確認結果
driver.save_screenshot("register_result.png")

# 關閉瀏覽器
driver.quit()
