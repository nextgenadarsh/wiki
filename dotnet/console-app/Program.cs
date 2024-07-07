
public class Program
{
    public delegate void DisplayMessage(string message);
    private static void Main(string[] args)
    {
        DisplayMessage display = delegate(string message)
        {
            Console.WriteLine(message);
        };

        display("Hello, delegate with Anonymous method!");    
    }
}

