Multi-threading
---

# Locking Mechanism

## Lock keyword/Monitor

- Creates a basic code zone where only one thread can enter at the same time.
- This is precisely the same as using `Monitor.Enter/Exit` class.

## Mutex

- This is `similar to Monitor` but can be named and shared between processes and async code (which lock keyword cannot).

## SemaphoreSlim

- `Lightweight version of Semaphore` which works within the same application.
- Allows you to fine-tune the number of threads that can enter into the critical zone.

## ManualResetEvent/AutoResetEvent

- These classes can be shared among threads to allow precise control regarding when some code should wait and when it can execute.
- The major difference here is that the code is not restricted to a critical zone.

# Threadsafe Collections

- ConcurrentDictionary<T, S>
- ConcurrentBag<T>

# Async / Await

## `await AsyncMethod()` vs `AsyncMethod().Result`

- “await AsyncMethod()” is used for asynchronous programming, allowing the method to `pause execution` until the awaited task completes. 
- “AsyncMethod().Result” `blocks the main thread`, waiting for the task’s completion, which `can lead to potential deadlocks` in specific scenarios.
- Using “await” with asynchronous methods is essential to maintain the application’s responsiveness.

## Async vs Parallel Calls

- If we’re launching async code instructions and not awaiting them, then we’re effectively loading them in parallel.

```csharp
var task1 = DoTask1Async();
var task2 = DoTask2Async();
Task.WaitAll(new [] {task1, task2}); // Wait for above 2 tasks to complete
Var result = await DoTask3Async(task1.Result, task2.Result);
```

# Thread Pool

- System automatically manages the details of how and when tasks are assigned to threads in the thread pool.

```csharp
ThreadPool.QueueUserWorkItem(new WaitCallback(SomeMethod));
```

# Parallel.ForEach

- Runs upon multiple threads and processing takes place in a parallel way.
- Execution is faster than foreach in most of the cases.

```csharp
Parallel.ForEach(users, user =>
  {
      Console.WriteLine("User Name: {0}, Thread Id= {1}", user.Name, Thread.CurrentThread.ManagedThreadId);
  }
);
```