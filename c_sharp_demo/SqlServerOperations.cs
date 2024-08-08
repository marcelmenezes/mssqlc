// SqlServerOperations.cs
using System;
using System.Data.SqlClient;

public class SqlServerOperations
{
    private static readonly string connectionString = "Server=localhost,1433;Database=SampleDB;User Id=sa;Password=YourStrongPassw0rd;";

    public static void RunDatabaseOperations()
    {
        Console.WriteLine("Welcome to the SQL query prompt. Type 'exit' to quit.");

        while (true)
        {
            Console.Write("Enter your SQL query: ");
            string? query = Console.ReadLine();

            if (string.IsNullOrWhiteSpace(query))
            {
                Console.WriteLine("Query cannot be empty. Please try again.");
                continue;
            }

            if (query.ToLower() == "exit")
                break;

            ExecuteQuery(query);
            Console.WriteLine();
        }

        Console.WriteLine("Goodbye!");
    }

    private static void ExecuteQuery(string query)
    {
        try
        {
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                connection.Open();
                using (SqlCommand command = new SqlCommand(query, connection))
                {
                    if (query.Trim().ToUpper().StartsWith("SELECT"))
                    {
                        using (SqlDataReader reader = command.ExecuteReader())
                        {
                            if (!reader.HasRows)
                            {
                                Console.WriteLine("No results found.");
                                return;
                            }

                            // Print column names
                            for (int i = 0; i < reader.FieldCount; i++)
                            {
                                Console.Write(reader.GetName(i) + " | ");
                            }
                            Console.WriteLine();
                            Console.WriteLine(new string('-', 50));

                            // Print rows
                            while (reader.Read())
                            {
                                for (int i = 0; i < reader.FieldCount; i++)
                                {
                                    Console.Write(reader[i] + " | ");
                                }
                                Console.WriteLine();
                            }
                        }
                    }
                    else
                    {
                        int rowsAffected = command.ExecuteNonQuery();
                        Console.WriteLine($"Query executed successfully. Rows affected: {rowsAffected}");
                    }
                }
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error executing query: {ex.Message}");
        }
    }
}