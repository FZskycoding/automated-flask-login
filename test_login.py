from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 初始化 WebDriver
driver = webdriver.Edge()

try:
    # 打開登入頁面
    driver.get("http://127.0.0.1:5000/login")
    time.sleep(2)  # 等待頁面加載
    
    # 輸入 Email
    email_input = driver.find_element(By.NAME, "email")
    email_input.send_keys("test@example.com")  # 替換為你的測試 Email
    
    # 輸入密碼
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("Test1234")  # 替換為你的測試密碼

    # 按下登入按鈕
    login_button = driver.find_element(By.TAG_NAME, "button")
    login_button.click()

    time.sleep(2)  # 等待頁面跳轉

    # 確認是否成功登入（檢查 Dashboard 頁面的元素）
    if "歡迎" in driver.page_source:
        print("✅ 登入測試成功！")
    else:
        print("❌ 登入測試失敗！")

    # 截圖存檔
    driver.save_screenshot("login_test_result.png")

finally:
    # 關閉瀏覽器
    driver.quit()
