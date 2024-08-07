using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Starting SQL Server operations...");
        
        SqlServerOperations.RunDatabaseOperations();
        
        Console.WriteLine("\nPress any key to exit...");
        Console.ReadKey();
    }
}