import mysql.connector
from csv import reader

def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(user='dylan',
                                            password='boomss',
                                            host='localhost',
                                            port='3306',
                                            database='ticket_sales')
    except Exception as error:
        print("Error while connecting to database for job tracker", error)
    return connection

def load_third_party(connection, file_path_csv):
    cursor = connection.cursor()
    # [Iterate through the CSV file and execute insert statement]
    with open(file_path_csv, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        for row in csv_reader:
            row[0]=int(row[0])
            row[2]=int(row[2])
            row[7] = int(row[7])
            row[8] = float(row[8])
            row[9] = int(row[9])
            statement = "INSERT INTO tickets (ticket_id, trans_date," \
                        " event_id, event_name, event_date, event_type," \
                        " event_city, customer_id, price, num_tickets)" \
                        " VALUES (%s, \'%s\', %s, \'%s\', \'%s\', \'%s\', \'%s\', %s, %s, %s);" \
                        ""%(row[0], row[1], row[2], row[3], row[4], row[5],
                            row[6], row[7], row[8], row[9],)
            print(statement)
            cursor.execute(statement)
    connection.commit()
    cursor.close()
    return


def query_popular_tickets(connection):
    # Get the most popular ticket in the past month
    sql_statement = "SELECT event_name FROM tickets ORDER BY num_tickets DESC LIMIT 3"
    cursor = connection.cursor()
    cursor.execute(sql_statement)
    records = cursor.fetchall()
    cursor.close()
    return records

connected = get_db_connection()
load_third_party(connected, 'third_party_sales_1.csv')
top_3 = query_popular_tickets(connected)
print("The three most popular shows in the last month were:")
for i in top_3:
    print(i)