import psycopg2


def insert_drone_data(drone):
    conn = None
    try:
        # try to connect to the DataBase
        print("Connecting to DB")
        # set host, port, db name and credential to access the db
        conn = psycopg2.connect(
            host="192.168.104.150",
            port="5432",
            database="iotdb",
            user="iot",
            password="iot")
        cursor = conn.cursor()
        cursor.execute("INSERT")  # query
        print("Data successfully inserted in the DB")
        conn.commit()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        # print the error in the console
        print(error)
