from selenium import webdriver
from selenium.webdriver.common.by import By


class AuctionScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def __del__(self):
        self.driver.quit()

    def get_auction_name(self, url):
        self.driver.get(url)
        name_element = self.driver.find_element(By.CLASS_NAME,
                                                'mgmw_wo.mli8_k4.mp0t_ji.munh_0.m3h2_0.mp4t_0.mqu1_1j.m9qz_yq.mgn2_16.mgn2_17_s.mryx_8._7030e_LKD2N')

        if name_element:
            name = name_element.text
            print(f"Auction name: {name}")
        else:
            print('No element with the specified class name found.')

    def get_auction_price(self, url):
        self.driver.get(url)
        price_element = self.driver.find_element(By.CLASS_NAME, '_7030e_qVLm-')

        if price_element:
            price = price_element.text
            price = float(price.replace(" zł", "").replace(",", "."))
            print(f"Price: {price}")
        else:
            print('No element with the specified class name found.')


if __name__ == "__main__":
    url = 'https://allegro.pl/oferta/rust-pelna-wersja-steam-13857559260?reco_id=cd6da594-258f-11ee-8851-4e991bb352df&sid=7d57f5ef092032639969aa24b7a6e07a65c247015427a0fba01293aeed154791'
    scraper = AuctionScraper()
    scraper.get_auction_name(url)
    scraper.get_auction_price(url)
