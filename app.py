from flask import Flask, render_template, request
from auction import AuctionScraper
from database import DatabaseManager

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    auction_data = []
    sort_option = 'id_asc'  # Default sorting option

    sort_options = [
        ('id_asc', 'ID Ascending'),
        ('id_desc', 'ID Descending'),
        ('name_az', 'Name A-Z'),
        ('name_za', 'Name Z-A'),
        ('price_low_high', 'Price Low-High'),
        ('price_high_low', 'Price High-Low'),
    ]

    if request.method == 'POST':
        url = request.form['url']
        sort_option = request.form['sort_option']  # Update sort_option here
        if url:
            scraper = AuctionScraper()
            name, price = scraper.get_auction_data(url)
            if name and price:
                db_manager = DatabaseManager()
                db_manager.insert_auction_data(name, price, url)

    db_manager = DatabaseManager()
    auction_data = db_manager.get_all_auction_data(sort_option)

    return render_template('index.html', auction_data=auction_data, sort_options=sort_options, current_sort=sort_option)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
