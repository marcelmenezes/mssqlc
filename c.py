import pyodbc

# Connection parameters
server = 'localhost,1433'
database = 'master'  # You can change this to your specific database
username = 'sa'
password = 'YourStrongPassw0rd'  # Use the password you set when creating the container

# Create the connection string
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    # Establish the connection
    conn = pyodbc.connect(conn_str)
    
    # Create a cursor
    cursor = conn.cursor()
    
    # Execute a test query
    cursor.execute("SELECT @@VERSION")
    
    # Fetch the result
    row = cursor.fetchone()
    
    # Print the result
    print("SQL Server version:")
    print(row[0])
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error connecting to SQL Server: {e}")