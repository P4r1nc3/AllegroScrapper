from bs4 import BeautifulSoup
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
            return name
        else:
            print('No element with the specified class name found.')
            return None

    def get_auction_price(self, url):
        self.driver.get(url)
        price_element = self.driver.find_element(By.CLASS_NAME, '_7030e_qVLm-')

        if price_element:
            price = price_element.text
            price = float(price.replace(" zł", "").replace(",", "."))
            return price
        else:
            print('No element with the specified class name found.')
            return None

class HtmlGenerator:
    def __init__(self, url_list):
        self.url_list = url_list

    def scrape_auction_data(self):
        auction_data = []
        for url in self.url_list:
            scraper = AuctionScraper()
            auction_name = scraper.get_auction_name(url)
            auction_price = scraper.get_auction_price(url)

            if auction_name and auction_price:
                auction_data.append((auction_name, auction_price, url))

        return auction_data

    def generate_table_html(self, auction_data):
        table_rows = []
        for auction in auction_data:
            auction_name, auction_price, url = auction
            row = f'<tr><td>{auction_name}</td><td>{auction_price}</td><td><a href="{url}">Link</a></td></tr>'
            table_rows.append(row)

        table_html = '<table class="table">'
        table_html += '<thead><tr><th>Name</th><th>Price</th><th>Link</th></tr></thead>'
        table_html += '<tbody>'
        table_html += ''.join(table_rows)
        table_html += '</tbody></table>'

        return table_html

    def generate_html_file(self):
        auction_data = self.scrape_auction_data()
        table_html = self.generate_table_html(auction_data)

        # Formatting the HTML using BeautifulSoup
        template_html = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Auction Table</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
        </head>
        <body>
            <div class="container">
                <h1>Auction Table</h1>
                {table_html}
            </div>

            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        </body>
        </html>
        '''

        # Saving the formatted HTML to the file
        soup = BeautifulSoup(template_html, 'html.parser')
        with open('../index.html', 'w', encoding='utf-8') as file:
            file.write(str(soup))

        print("HTML file 'index.html' has been generated.")

if __name__ == "__main__":
    url_list = [
        'https://allegro.pl/oferta/rust-pelna-wersja-steam-13857559260?reco_id=cd6da594-258f-11ee-8851-4e991bb352df&sid=7d57f5ef092032639969aa24b7a6e07a65c247015427a0fba01293aeed154791',
        'https://allegro.pl/oferta/rust-steam-nowa-gra-pelna-polska-wersja-pc-pl-13826923608?bi_s=ads&bi_m=showitem:desktop:top:active&bi_c=NjQ0Mjg4ZGMtOTQ5Zi00ZWVlLWJkMmEtMTc2YzNiMTFiODdmAA&bi_t=ape&referrer=proxy&emission_unit_id=8c158955-ddd9-4be6-acb2-6712d48ef981',
        'https://allegro.pl/oferta/hunt-showdown-steam-nowa-gra-pelna-wersja-pc-pl-11106874677?bi_s=ads&bi_m=showitem:desktop:top:active&bi_c=NjQ0Mjg4ZGMtOTQ5Zi00ZWVlLWJkMmEtMTc2YzNiMTFiODdmAA&bi_t=ape&referrer=proxy&emission_unit_id=68c898a2-7a16-4b74-ac5a-1b5ac24db8e5'
    ]

    html_generator = HtmlGenerator(url_list)
    html_generator.generate_html_file()

