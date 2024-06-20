# C# Features
--

# C# 2.0 Features

## Generics

- Allows to create type-safe data structures.
- You can create the generic interfaces, classes, methods, events, delegates.

```csharp
List<int> numbers = new List<int>(); // Collection to contain only integers
numbers.Add(123);
numbers.Add("some string"); // compile time error
```

## Partial Class

- Allows to split a class definition across multiple files.
- Mostly used with automatically generated source code (like EF generated files) to extend it.

```csharp
// File: Student.cs
public partial class Student {
    private string Name = "Adarsh Kumar";
    public string GetName() {
        return Name;
    }
}
// File: StudentExtended.cs
public partial class Student {
    private int Age = 40;
    public int GetAge() {
        return Age;
    }
}
```

# C# 3.0 Features

## LINQ: Language Integrated Query

- Allows to query various data sources like C# collection, SQL, XML like data using common query syntax.

```csharp
var numbers = new List<int>();
var evenNumbers = numbers.Where(n => n % 2 == 0);
var firstEvenNumber = numbers.FirstOrDefault(n => n % 2 == 0);

// LINQ to SQL to query database
var activeUsers = _dbContext.Users.Select(user => user.IsActive);
```

## Lambda Expressions

- Provides a concise way to write inline expressions or anonymous methods.

```csharp
List<User> users = new List<User>() {
    new User (101, "Adarsh Kumar", true),
    new User (102, "Sulekha More", false)
};
IEnumerable<User> activeUser = users.Where(user => user.IsActive);
```

## Extension Methods

- Allows to add methods or extend functionality of existing class without modifying them or if you don't have permission.

```csharp
public static class StringExtension {
    public static string RemoveSpecialCharacter(this string input) {
        // Implementation
    }
}

var dirtyInput = "A@#dar!h K)^u&mar";
var name = dirtyInput.RemoveSpecialCharacter();
```

# C# 4.0 Features

## Dynamic Type

- It defers type checking from compile time to runtime.
- If the method is not supported by underlying data type, it will throw runtime exception but not compile time.

```csharp
dynamic dynamicData = "Adarsh Kumar";
dynamic numbers = new List<int>() { 1, 2, 3};

numbers.FindMyNumber(); // Throws runtime exception
```

# C# 5.0 Features

## Async/Await

- Allows to write asynchronous code used for non-blocking UI and server applications.

```csharp
public static async Task<string> Welcome(string name) {
    return await Task.FromResult($"Welcome {name}");
}
Console.WriteLine(Welcome(dynamicData).GetAwaiter().GetResult());
```

# C# 6.0 Features

## String Interpolation

- Allows to embed expressions and variables directly within string literal.

```csharp
var name = "Adarsh Kumar";
var message = $"Welcome {name}";
```

## Expression-Bodied Members

- Allows to write concise one-liner methods, properties using lambda-like syntax.

```csharp
public int Add(int first, int second) => first + second;
```

## Auto-Property Initializers

- It is a way to initialize value of an auto-implemented property directly within property declaration.

```csharp
public string UserServiceHost { get; set; } = "http://default-user-service.com";
```

# C# 7.0 Features

## Tuples and Deconstruction

- Allows to work with set of values without creating class for them.

```csharp
var nameAge = (Name: "Adarsh Kumar", Age: 40);
Console.WriteLine($"Name: {nameAge.Name}");

// Deconstruction
var (userName, userAge) = nameAge; // values are assigned to variables as per tuple order
Console.WriteLine($"Name: {userName}");
```

## Pattern Matching

- Allows you to check the shape of structure of a value directly in code.

```csharp
object message = "Welcome Adarsh";
if(message is string greeting) {
    Console.WriteLine($"Greeting: {greeting}");
}
```

# C# 8.0 Features

## Nullable Reference Types

- Help developers write more rebust and safe code by adding annotations to the type system to indicate whether a reference type can be null or not.

```csharp
string? message = null;
if (message != null) {
    Console.WriteLine(message);
}
```

## Default Interface Methods

- Allows you to provide a default implementation for methods in an interface.
- Helps maintain backward compatibility when introducing new methods to interface without requiring implementing classes to provide an implementation.

```csharp
public interface IRunnable {
    int DistanceRun { get; set; }
    void Run();
    bool IsRunning() => DistanceRun > 0;
}

public class Human : IRunnable {
    public int DistanceRun { get; set; }
    public void Run() {
        DistanceRun += 10;
    }
}

IRunnable human = new Human();
human.Run();
Console.WriteLine($"Is Human Running: {human.IsRunning()}");
```

## Switch Expression

```csharp
var (op1, op2, op) = (12, 4, "*");
var value = op switch {
    "+" => op1 + op2,
    "-" => op1 - op2,
    "*" => op1 * op2,
    _ => 0
};

var (op1, op2, op) = (12, 5, "*");
var value = op switch {
    _ when op == "+" => op1 + op2,
    _ when op == "-" => op1 - op2,
    _ when op == "*" => op1 * op2,
    _ => 0
};
```

# C# 9.0 Features

## Record Types

- Provide concise way to declare **immutable** types.
- Simplifies the process of creating and working with immutable classes by automatically generating common methods like Equals, GetHashCode, and ToString.
- Useful for modeling DTO and other types where immutability and value equality are essential.

```csharp
public record User(string Name, int Age);

var user = new User("Adarsh Kumar", 40);
var updatedUser = user with { Age = 60 };

// user.Age = 18; // Throws compile time error
```

## Top-Level Statements

- Allows you to write simpler C# programs by omitting the traditional Main method and placing the program logic directly at the top level of the file.
- Simplifies the structure of simple programs by reducing boilerplate code.

```csharp
using System;

Console.WriteLine("Welcome, Adarsh");

int sum = Add(23, 4);
Console.WriteLine($"23 + 4 = {sum}");

int Add(int first, int second) => first + second;
```

# C# 10.0 Features

## Global Using Directives

- Allows you to specify a set of using directives that will be applied globally to all files in a project without need to include them explicitly in every file.

```csharp
// In a GlobalUsing.cs file
global using System;
global using System.Collections.Generic;

// Code in program.cs file to access global using directives directly
List<int> numbers = new List<int> { 10, 11, 12 };
```

# C# 11.0 Features

## List Pattern

- Used to match elements of a list or array succinctly and expressively.

```csharp
var numbers = new [] { 1, 2, 3 };
if (numbers is [1, 2, 3]) {
    Console.WriteLine("Numbers matching !!");
}
```

## Required Members

- Enforce certain members to be initialized in the constructor.

```csharp
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

var user1 = new User("Adarsh Kumar", 40);
var user2 = new User() { Name = "Adarsh", Age = 40 };
// var user3 = new User(); // compile time error
```

# C# 12.0 Features

## Collection Expressions

- Simplifies the process of creating and intializing collections.

```csharp
var numbersOldWay = new int[] { 1, 2, 3 };
var namesOldWay = new List<string> { "Adarsh", "Sukanya" };

// Collection expression does not support var
int [] numbersNewWay = [ 1, 2, 3 ];
List<string> namesNewWay = ["Adarsh", "Sukanya" ];
```

