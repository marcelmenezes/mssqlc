import pyodbc

# Connection parameters
server = 'localhost,1433'
database = 'SampleDB'  # The database we created
username = 'sa'
password = 'YourStrongPassw0rd'  # Replace with your actual password

# Create the connection string
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

def execute_query(query):
    try:
        with pyodbc.connect(conn_str) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            
            # If the query is a SELECT statement, fetch and print results
            if query.strip().upper().startswith('SELECT'):
                rows = cursor.fetchall()
                if not rows:
                    print("No results found.")
                else:
                    # Print column names
                    print(" | ".join([column[0] for column in cursor.description]))
                    print("-" * 50)
                    # Print rows
                    for row in rows:
                        print(" | ".join(str(value) for value in row))
            else:
                # For non-SELECT queries, print the number of affected rows
                print(f"Query executed successfully. Rows affected: {cursor.rowcount}")
            
            # Commit changes for non-SELECT queries
            if not query.strip().upper().startswith('SELECT'):
                conn.commit()
    
    except pyodbc.Error as e:
        print(f"Error executing query: {e}")

print("Welcome to the SQL query prompt. Type 'exit' to quit.")

while True:
    query = input("Enter your SQL query: ")
    if query.lower() == 'exit':
        break
    execute_query(query)
    print()  # Print a blank line for readability

print("Goodbye!")