class Config:
    # MySQL 配置
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_DB = 'flask_auth'
    MYSQL_CURSORCLASS = 'DictCursor'
    
    # 從環境變數加載敏感資訊
    MYSQL_PASSWORD = None  
    SECRET_KEY = None      
