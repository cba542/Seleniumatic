import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BrowserManager:
    def __init__(self, user_data_dir=None, headless=False):
        """初始化瀏覽器管理器
        
        Args:
            user_data_dir: Chrome用戶數據目錄
            headless: 是否啟用無頭模式
        """
        self.options = webdriver.ChromeOptions()
        
        # 設置用戶數據目錄
        if user_data_dir:
            self.options.add_argument(f"user-data-dir={user_data_dir}")
        else:
            username = os.getlogin()
            self.options.add_argument(f"user-data-dir=C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data")
        
        self.options.add_argument("--profile-directory=Default")
        self.options.add_argument("--log-level=3")  # 僅顯示嚴重錯誤
        
        if headless:
            self.options.add_argument("--headless")
        
        # 初始化驅動
        self.service = webdriver.ChromeService(executable_path="C:\\chromedriver.exe")
        self.driver = None
    
    def start(self, implicit_wait=5):
        """啟動瀏覽器"""
        if self.driver is None:
            self.driver = webdriver.Chrome(service=self.service, options=self.options)
            self.driver.implicitly_wait(implicit_wait)
        return self.driver
    
    def stop(self):
        """關閉瀏覽器"""
        if self.driver:
            self.driver.quit()
            self.driver = None
    
    def __enter__(self):
        """上下文管理器入口"""
        return self.start()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """上下文管理器出口"""
        self.stop()