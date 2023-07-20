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

    def get_all_auction_data(self, sort_option):
        sort_mapping = {
            'id_asc': 'ORDER BY id ASC',
            'id_desc': 'ORDER BY id DESC',
            'name_az': 'ORDER BY name ASC',
            'name_za': 'ORDER BY name DESC',
            'price_low_high': 'ORDER BY price ASC',
            'price_high_low': 'ORDER BY price DESC',
        }
        sort_clause = sort_mapping.get(sort_option, 'ORDER BY id ASC')

        select_query = f"SELECT id, name, price, url FROM auctions {sort_clause}"
        self.cursor.execute(select_query)
        auction_data = [{'id': id, 'name': name, 'price': price, 'url': url} for (id, name, price, url) in self.cursor]
        return auction_data

    def delete_auction(self, auction_id):
        delete_query = "DELETE FROM auctions WHERE id = %s"
        data = (auction_id,)
        self.cursor.execute(delete_query, data)
        self.conn.commit()