from selenium import webdriver
from selenium.webdriver.common.by import By

class AuctionScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def __del__(self):
        self.driver.quit()

    def get_auction_data(self, url):
        self.driver.get(url)
        name_element = self.driver.find_element(By.CLASS_NAME, 'mgmw_wo.mli8_k4.mp0t_ji.munh_0.m3h2_0.mp4t_0.mqu1_1j.m9qz_yq.mgn2_16.mgn2_17_s.mryx_8._7030e_LKD2N')
        price_element = self.driver.find_element(By.CLASS_NAME, '_7030e_qVLm-')

        if name_element and price_element:
            name = name_element.text
            price = float(price_element.text.replace(" zł", "").replace(",", "."))
            return name, price
        else:
            print('No element with the specified class name found.')
            return None, None
