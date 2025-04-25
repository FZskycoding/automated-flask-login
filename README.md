# Flask Selenium Auth

這是一個使用 Flask 框架開發的網站認證系統，並整合了 Selenium 進行自動化測試。專案實現了基本的用戶註冊、登入功能，並包含完整的自動化測試流程。

## 功能特點

- 用戶註冊
- 用戶登入/登出
- 儀表板頁面
- 自動化測試套件
- MySQL 資料庫存儲

## 技術棧

- **後端框架**: Flask
- **資料庫**: MySQL
- **測試工具**: Selenium
- **瀏覽器**: Microsoft Edge
- **安全性**: Session 管理
- **前端**: HTML, Flask Templates


## 安裝依賴
```bash
pip install flask selenium flask-mysqldb
```

## 訪問網站

- 開啟瀏覽器訪問 `http://localhost:5000`
- 點擊註冊按鈕創建新帳號
- 使用創建的帳號登入系統

## 自動化測試

專案包含兩個測試檔案：
- `test_register.py`: 測試自動註冊功能
- `test_login.py`: 測試自動登入功能

執行測試：
```bash
python test_register.py
python test_login.py
```

## 注意事項

1. 確保已安裝 Microsoft Edge 瀏覽器
2. WebDriver 版本需要與 Edge 瀏覽器版本相符
3. 確保已創建 MySQL 資料庫並配置正確的連接資訊
