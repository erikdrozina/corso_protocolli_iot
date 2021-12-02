import psycopg2

def insert_drone_data(drone):
    conn = None
    try:
        print("Connecting to DB")
        conn = psycopg2.connect(
            host="192.168.104.150",
            port="5432",
            database="iotdb",
            user="iot",
            password="iot")
        cursor = conn.cursor()
        cursor.execute("INSERT")  # query
        print("inserted")
        conn.commit()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)