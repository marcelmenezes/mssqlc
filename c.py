import pyodbc

server = 'localhost,1433'
database = 'master'
username = 'sa'
password = 'YourStrongPassw0rd'

conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("SELECT @@VERSION")
    row = cursor.fetchone()
    print("SQL Server version:")
    print(row[0])
    cursor.close()
    conn.close()
except pyodbc.Error as e:
    print(f"Error connecting to SQL Server: {e}")