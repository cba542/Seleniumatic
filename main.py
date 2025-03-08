from selenium_framework.browser import BrowserManager
from selenium_framework.sites.apk_tw import ApkTwSite
from selenium_framework.sites.bingfong import BingFongSite
from selenium_framework.sites.shopping_gamania import ShoppingGamaniaSite
from selenium_framework.sites.bahamut import BahamutSite

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('main')

def process_site(site_class, driver, site_name):
    """
    通用的站點處理函數
    """
    site = site_class(driver)
    site.navigate()
    
    if site.sign_in():
        logger.info(f"{site_name} 簽到成功")
    else:
        logger.error(f"{site_name} 簽到失敗")

def main():

    browser_manager = BrowserManager(user_data_dir="D:\\Selenium_Chrome\\User Data")
    driver = browser_manager.start()
    
    # 定義要處理的站點列表
    sites = [
        (ApkTwSite, "APK.tw"),
        (BingFongSite, "BingFongSite"),
        (ShoppingGamaniaSite, "ShoppingGamaniaSite"),
        (BahamutSite, "BahamutSite")
    ]
    
    # 依次處理每個站點
    for site_class, site_name in sites:
        try:
            process_site(site_class, driver, site_name)
        except Exception as e:
            logger.error(f"{site_name} 處理時發生錯誤: {str(e)}")

    # 如果需要等待查看結果
    # input('按 Enter 鍵關閉瀏覽器...')

if __name__ == "__main__":
    main()