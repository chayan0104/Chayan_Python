import mysql.connector

connection = " "
try:
    # Establish the connection
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234242",
        database="home_builder"
    )

    if connection.is_connected():
        print("Successfully connected to the database")

    # Define the query
    # query = "SELECT * FROM labours_table ORDER BY wages DESC"
    # query = "SELECT COUNT(*) FROM labours_table;"
    # query = "INSERT INTO labours_table (name, role, wages) VALUES ('John', 'labour', 600);"
    # query = "UPDATE labours_table SET wages = 550 WHERE name = 'Mahesh'"
    query = "SELECT * FROM labours_table WHERE wages BETWEEN 400 AND 2000;"

    # Use the cursor as a context manager
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        print(rows)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection and connection.is_connected():
        connection.close()
