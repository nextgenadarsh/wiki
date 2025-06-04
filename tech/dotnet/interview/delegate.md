# Delegate
---



```csharp
public delegate void DisplayMessage(string message);

DisplayMessage display = delegate(string message) // Anonymous method
{
    Console.WriteLine(message);
};

display("Hello, Anonymous method!");
```

## Singlecast Delegates

- Reference a `single method` with a matching signature.
- When the delegate is invoked, it calls the referenced method.

```csharp
public delegate void DisplayMessage(string message);

static void ShowMessage(string message)
{
    Console.WriteLine(message);
}

DisplayMessage display = ShowMessage;
display("Hello, Singlecast delegate!");
````

## Multicast Delegates

- Reference `multiple methods` with a matching signature.
- When the delegate is invoked, it calls all the referenced methods in the order they were added.
- Multicast delegates are created using the += or -= operators.

```csharp
public delegate void DisplayMessage(string message);

static void ShowMessage1(string message)
{
    Console.WriteLine("Message 1: " + message);
}

static void ShowMessage2(string message)
{
    Console.WriteLine("Message 2: " + message);
}

DisplayMessage display = ShowMessage1;
display += ShowMessage2;
display("Hello, Multicast delegate!");
```

## Generic Delegates

- Use generic type parameters, allowing them to work with multiple types without casting or boxing/unboxing.
- C# provides three built-in generic delegates.

### Func<TResult>

- A delegate that represents a function with a return type.

```csharp
Func<int, int, int> add = (x, y) => x + y;

int sum = add(10, 20);
```

### Action

    - A delegate that represents a void-returning method with no parameters.

```csharp
Action<string> display = message => Console.WriteLine(message);

display($"Sum: {sum}");
```

### Predicate<T>
        
- A delegate that represents a method that takes an input parameter and returns a boolean.

