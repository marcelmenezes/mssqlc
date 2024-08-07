import pyodbc

# Connection parameters
server = 'localhost,1433'
database = 'master'
username = 'sa'
password = 'YourStrongPassw0rd'

# Create the connection string
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'


drivers = pyodbc.drivers()
print("Available ODBC drivers:")
for driver in drivers:
    print(driver)


try:
    # Establish the connection
    conn = pyodbc.connect(conn_str)
    
    # Create a cursor
    cursor = conn.cursor()
    
    # Create a new table
    cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Employees' AND xtype='U')
    CREATE TABLE Employees (
        ID INT PRIMARY KEY IDENTITY(1,1),
        Name NVARCHAR(100),
        Department NVARCHAR(50),
        Salary DECIMAL(10, 2)
    )
    """)
    
    # Insert some data
    cursor.execute("""
    INSERT INTO Employees (Name, Department, Salary)
    VALUES 
    ('John Doe', 'IT', 75000.00),
    ('Jane Smith', 'HR', 65000.00),
    ('Mike Johnson', 'Sales', 80000.00)
    """)
    
    # Commit the transaction
    conn.commit()
    
    # Retrieve and display the data
    cursor.execute("SELECT * FROM Employees")
    
    rows = cursor.fetchall()
    print("Employees:")
    for row in rows:
        print(f"ID: {row.ID}, Name: {row.Name}, Department: {row.Department}, Salary: ${row.Salary:.2f}")
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
except pyodbc.Error as e:
    print(f"Error: {e}")