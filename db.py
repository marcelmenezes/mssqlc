import pyodbc

# Connection parameters
server = 'localhost,1433'
database = 'master'
username = 'sa'
password = 'YourStrongPassw0rd'  # Replace with your actual password

# Create the connection string
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    # Establish the connection
    conn = pyodbc.connect(conn_str, autocommit=True)
    
    # Create a cursor
    cursor = conn.cursor()
    
    # Create a new database
    new_database_name = 'SampleDB'
    cursor.execute(f"IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = '{new_database_name}') CREATE DATABASE {new_database_name}")
    print(f"Database '{new_database_name}' created successfully.")
    
    # Switch to the new database
    conn.close()
    database = new_database_name
    conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    
    # Create a simple table
    cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Users' AND type = 'U')
    CREATE TABLE Users (
        ID INT PRIMARY KEY IDENTITY(1,1),
        Username NVARCHAR(50) NOT NULL,
        Email NVARCHAR(100) NOT NULL,
        CreatedDate DATETIME DEFAULT GETDATE()
    )
    """)
    conn.commit()
    print("Table 'Users' created successfully.")
    
    # Insert a sample record
    cursor.execute("INSERT INTO Users (Username, Email) VALUES (?, ?)", 'JohnDoe', 'john.doe@example.com')
    conn.commit()
    print("Sample record inserted.")
    
    # Verify the insertion
    cursor.execute("SELECT * FROM Users")
    row = cursor.fetchone()
    print(f"Inserted record: ID: {row.ID}, Username: {row.Username}, Email: {row.Email}, Created: {row.CreatedDate}")
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")