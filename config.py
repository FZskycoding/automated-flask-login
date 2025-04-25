class Config:
    # MySQL 配置
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_DB = 'flask_auth'
    MYSQL_CURSORCLASS = 'DictCursor'
    
    # 從環境變數加載敏感資訊
    MYSQL_PASSWORD = None  # 將從 .env 加載
    SECRET_KEY = None      # 將從 .env 加載
