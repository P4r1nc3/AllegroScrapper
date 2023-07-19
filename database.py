import mysql.connector

class DatabaseManager:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin12345',
            database='auction_db'
        )
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def insert_auction_data(self, name, price, url):
        insert_query = "INSERT INTO auctions (name, price, url) VALUES (%s, %s, %s)"
        data = (name, price, url)
        self.cursor.execute(insert_query, data)
        self.conn.commit()

    def get_all_auction_data(self):
        select_query = "SELECT name, price, url FROM auctions"
        self.cursor.execute(select_query)
        auction_data = [{'name': name, 'price': price, 'url': url} for (name, price, url) in self.cursor]
        return auction_data