import mysql.connector

# Set up connection with MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin12345',
    'database': 'auction_db'
}

def add_sample_data_to_database():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        insert_query = "INSERT INTO auctions (name, price, url) VALUES (%s, %s, %s)"
        data = ("Example Auction", 10.99, "https://example.com")

        cursor.execute(insert_query, data)
        connection.commit()

        cursor.close()
        connection.close()

        print("Sample data added to the database.")
    except mysql.connector.Error as error:
        print("Error while connecting to MySQL:", error)

if __name__ == '__main__':
    add_sample_data_to_database()