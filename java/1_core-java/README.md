- [Object Oriented Programming (OOPs)](#object-oriented-programming-oops)
  - [Basic Elements](#basic-elements)
    - [Access Modifiers](#access-modifiers)
      - [public: everywhere](#public-everywhere)
      - [protected: own package + subclass(es)](#protected-own-package--subclasses)
      - [private: within class](#private-within-class)
      - [default: own package](#default-own-package)
    - [Return Type](#return-type)
    - [Method Name](#method-name)
    - [Parameter List](#parameter-list)
    - [Exception List](#exception-list)
    - [Method Body](#method-body)
  - [OOPs Concetps](#oops-concetps)
    - [Method and method passing](#method-and-method-passing)
    - [Pillars](#pillars)
      - [Abstraction: process of identifying relevant details of an entity](#abstraction-process-of-identifying-relevant-details-of-an-entity)
      - [Encapsulation: binds/hide data and method together](#encapsulation-bindshide-data-and-method-together)
      - [Inheritance: inherits characteristics of other class](#inheritance-inherits-characteristics-of-other-class)
        - [Super Class](#super-class)
        - [Sub Class](#sub-class)
        - [Reusability](#reusability)
        - [Types](#types)
          - [Single inheritance](#single-inheritance)
          - [Multilevel inheritance](#multilevel-inheritance)
          - [Hierarchical inheritance](#hierarchical-inheritance)
          - [Multiple inheritance: via interfaces](#multiple-inheritance-via-interfaces)
      - [Polymorphism: ability to differentiate between entities with the same name](#polymorphism-ability-to-differentiate-between-entities-with-the-same-name)
        - [Overloading](#overloading)
        - [Overriding](#overriding)
        - [Compile-time/static: method/operator overloading](#compile-timestatic-methodoperator-overloading)
        - [Run-time/dynamic method dispatch: method overriding](#run-timedynamic-method-dispatch-method-overriding)
  - [Class | Object | Method | Package](#class--object--method--package)
    - [Class: a user defined blueprint](#class-a-user-defined-blueprint)
      - [Access Modifiers](#access-modifiers-1)
      - [Class Name](#class-name)
      - [Super Class: extends](#super-class-extends)
      - [Interfaces: implements](#interfaces-implements)
      - [Body](#body)
      - [Wrapper Classes: wraps primitive data types : AutoBoxing/Unboxing](#wrapper-classes-wraps-primitive-data-types--autoboxingunboxing)
      - [Constructor](#constructor)
        - [No-argument constructor](#no-argument-constructor)
        - [Parametrized constructor](#parametrized-constructor)
        - [Copy constructor](#copy-constructor)
        - [Constructor chaining: this()/super() as first line](#constructor-chaining-thissuper-as-first-line)
        - [Init block: {} before constructor](#init-block--before-constructor)
    - [Object: represents real life entity](#object-represents-real-life-entity)
      - [State: represented by attribute](#state-represented-by-attribute)
      - [Behavior: represented by method](#behavior-represented-by-method)
      - [Identity: unique name of object](#identity-unique-name-of-object)
      - [Method: allows us to reuse the code](#method-allows-us-to-reuse-the-code)
    - [Method](#method)
      - [Method declaration](#method-declaration)
        - [Modifier](#modifier)
        - [Return type](#return-type-1)
        - [Method name](#method-name-1)
        - [Parameter list](#parameter-list-1)
        - [Exception list](#exception-list-1)
        - [Method body](#method-body-1)
      - [Types of method](#types-of-method)
        - [Predefined: standard library method](#predefined-standard-library-method)
        - [User defined method](#user-defined-method)
      - [Method calling](#method-calling)
      - [Memory Allocation](#memory-allocation)
        - [Stack](#stack)
        - [Heap](#heap)
    - [Package](#package)
- [Exception Handling](#exception-handling)
  - [Types](#types-1)
    - [Built-in](#built-in)
      - [Checked: compile time](#checked-compile-time)
      - [Unchecked: run time](#unchecked-run-time)
    - [User defined](#user-defined)
  - [Control flow](#control-flow)
- [Collection](#collection)
  - [ArrayList: add/remove](#arraylist-addremove)
  - [LinkedList:](#linkedlist)
  - [Vector: Synchronized Array](#vector-synchronized-array)
  - [Stack](#stack-1)
  - [Queue](#queue)
  - [Set](#set)
  - [HashSet](#hashset)
  - [HashMap](#hashmap)
- [Multithreading](#multithreading)
  - [Process vs Thread](#process-vs-thread)
  - [Multiprocessing vs Multithreading](#multiprocessing-vs-multithreading)
  - [Thread Lifecycle](#thread-lifecycle)
    - [New: just created](#new-just-created)
    - [Runnable: start() method called](#runnable-start-method-called)
    - [Running](#running)
    - [Blocked](#blocked)
    - [Terminated](#terminated)
  - [Thread Implementation](#thread-implementation)
    - [Thread class](#thread-class)
    - [Runnable interface](#runnable-interface)
- [_](#_)

# Object Oriented Programming (OOPs)

## Basic Elements

### Access Modifiers

#### public: everywhere

#### protected: own package + subclass(es)

#### private: within class

#### default: own package

### Return Type

### Method Name

### Parameter List

### Exception List

### Method Body

## OOPs Concetps

### Method and method passing

### Pillars

#### Abstraction: process of identifying relevant details of an entity

#### Encapsulation: binds/hide data and method together

#### Inheritance: inherits characteristics of other class

##### Super Class

##### Sub Class

##### Reusability

##### Types

###### Single inheritance

`public class Manager extends Employee`

###### Multilevel inheritance

```
public class Manager extends Employee
public class Senior extends Manager
```

###### Hierarchical inheritance

```
public class Manager extends Employee
public class Manager extends Employee
```

###### Multiple inheritance: via interfaces

#### Polymorphism: ability to differentiate between entities with the same name

##### Overloading

##### Overriding

##### Compile-time/static: method/operator overloading

##### Run-time/dynamic method dispatch: method overriding

## Class | Object | Method | Package

### Class: a user defined blueprint

#### Access Modifiers

#### Class Name

#### Super Class: extends

#### Interfaces: implements

#### Body

#### Wrapper Classes: wraps primitive data types : AutoBoxing/Unboxing

- Converts primitive data types into object. To pass by ref
- java.util package handles only object
- Collection data structures supports object only
- An object is needed to support synchronization in multithreading

#### Constructor

##### No-argument constructor

##### Parametrized constructor

##### Copy constructor

##### Constructor chaining: this()/super() as first line

##### Init block: {} before constructor

### Object: represents real life entity

#### State: represented by attribute

#### Behavior: represented by method

#### Identity: unique name of object

#### Method: allows us to reuse the code

### Method

#### Method declaration

##### Modifier

##### Return type

##### Method name

##### Parameter list

##### Exception list

##### Method body

#### Types of method

##### Predefined: standard library method

##### User defined method

#### Method calling

#### Memory Allocation

##### Stack

##### Heap

### Package

# Exception Handling

## Types

### Built-in

#### Checked: compile time

#### Unchecked: run time

### User defined

## Control flow

```
try {
    // block of code to monitor for errors
    // the code you think can raise an exception
}
catch (ArithmeticException exOb) {
    // exception handler for ExceptionType1
}
catch (IllegalAccessException ex) {
    // exception handler for ExceptionType2
    throw ex; // rethrowing the exception
}
// optional
finally {
    // block of code to be executed after try block ends
}
```

# Collection

## ArrayList: add/remove

## LinkedList: 

## Vector: Synchronized Array

## Stack

## Queue

## Set

## HashSet

## HashMap

# Multithreading

## Process vs Thread

## Multiprocessing vs Multithreading

## Thread Lifecycle

### New: just created

### Runnable: start() method called

### Running

### Blocked

### Terminated

## Thread Implementation

### Thread class

```
    class MyThread1 extends Thread {
        public void run()
        {
            System.out.println("Thread1 is running");
        }
    }

    public static void main(String[] args)
    {
        MyThread1 obj1 = new MyThread1();
        MyThread2 obj2 = new MyThread2();

        obj1.start();
        obj2.start();
    }
```

### Runnable interface

```
    class MyThread1 implements Runnable {
        public void run()
        {
            // Iterating to get more execution of threads
            for (int i = 0; i < 5; i++) {   
                System.out.println("Thread1");
                try {
                    Thread.sleep(1000);
                }
    
                // Catch block to handle the exceptions
                catch (Exception e) {
                }
            }
        }
    }

    public static void main(String[] args)
    {
        Runnable obj1 = new MyThread1();
        Runnable obj2 = new MyThread2();

        Thread t1 = new Thread(obj1);
        Thread t2 = new Thread(obj2);

        t1.start();
        t2.start();
    }    
```


# _