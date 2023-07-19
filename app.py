from flask import Flask, render_template, request
from auction import AuctionScraper
from database import DatabaseManager

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    auction_data = []

    if request.method == 'POST':
        url = request.form['url']
        if url:
            scraper = AuctionScraper()
            name, price = scraper.get_auction_data(url)
            if name and price:
                db_manager = DatabaseManager()
                db_manager.insert_auction_data(name, price, url)

    db_manager = DatabaseManager()
    auction_data = db_manager.get_all_auction_data()

    return render_template('index.html', auction_data=auction_data)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
