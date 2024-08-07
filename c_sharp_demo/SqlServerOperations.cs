using System;
using System.Data.SqlClient;

public class SqlServerOperations
{
    public static void RunDatabaseOperations()
    {
        string connectionString = "Server=localhost,1433;Database=master;User Id=sa;Password=YourStrongPassw0rd;";

        try
        {
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                connection.Open();
                Console.WriteLine("Connected to SQL Server.");

                // Create table
                string createTableQuery = @"
                IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Employees' AND xtype='U')
                CREATE TABLE Employees (
                    ID INT PRIMARY KEY IDENTITY(1,1),
                    Name NVARCHAR(100),
                    Department NVARCHAR(50),
                    Salary DECIMAL(10, 2)
                )";

                using (SqlCommand command = new SqlCommand(createTableQuery, connection))
                {
                    command.ExecuteNonQuery();
                    Console.WriteLine("Table 'Employees' created or already exists.");
                }

                // Insert data
                string insertDataQuery = @"
                INSERT INTO Employees (Name, Department, Salary)
                VALUES 
                ('John Doe', 'IT', 75000.00),
                ('Jane Smith', 'HR', 65000.00),
                ('Mike Johnson', 'Sales', 80000.00)";

                using (SqlCommand command = new SqlCommand(insertDataQuery, connection))
                {
                    int rowsAffected = command.ExecuteNonQuery();
                    Console.WriteLine($"{rowsAffected} row(s) inserted.");
                }

                // Select and display data
                string selectDataQuery = "SELECT * FROM Employees";

                using (SqlCommand command = new SqlCommand(selectDataQuery, connection))
                {
                    using (SqlDataReader reader = command.ExecuteReader())
                    {
                        Console.WriteLine("\nEmployees:");
                        while (reader.Read())
                        {
                            Console.WriteLine($"ID: {reader["ID"]}, Name: {reader["Name"]}, Department: {reader["Department"]}, Salary: ${reader["Salary"]:F2}");
                        }
                    }
                }
            }
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error: {e.Message}");
        }
    }
}