public class User {
    public required string Name { get; set; }
    public required int Age { get; set; }

    public User() { }

    [System.Diagnostics.CodeAnalysis.SetsRequiredMembersAttribute]
    public User(string name, int age)
    {
        Name = name;
        Age = age;
    }
}

public class Program
{
    private static void Main(string[] args)
    {
        var (op1, op2, op) = (12, 5, "*");
        var value = op switch {
            _ when op == "+" => op1 + op2,
            _ when op == "-" => op1 - op2,
            _ when op == "*" => op1 * op2,
            _ => 0
        };

        Console.WriteLine($"Operation Value: {value}");
    }
}

