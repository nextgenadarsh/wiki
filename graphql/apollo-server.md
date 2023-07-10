# Apollo Server Introduction

- Apollo Server is an `open-source`, `spec-compliant` GraphQL `server` that's compatible with any GraphQL client, including Apollo Client.
- A stand-alone GraphQL server, including in a serverless environment

## Quick start

Refer [Getting started guide](https://www.apollographql.com/docs/apollo-server/getting-started/)

# Fundamental Concepts

## Defining GraphQL schema

### Schema

`Schema` describes the shape of your available data. It defines a hierarcy of types with fields that are populated from your backend data stores. It also defines which `queries` and `mutations` are available for the clients to execute.

### Schema Definition Language (SDL)

The GraphQL specification defines a human-readable schema definition language (or SDL) that you `use to define your schema` and store it as a string.

```
type Employee {
    name: String            # returns string
    manager: Employee       # returns employee
    department: Department  # returns department
}

Type Department {
    name: String!               # can not return null
    employees: [Employee!]!     # employee list or its item can not be null
}
```

### Data Types

#### Scalar

    Similar to primitive types. They resolve to concerete data.

- **Int**: Signed 32-bit integer
- **Float**: Signed double-precision floating-point value
- **String**: UTF8 character sequence
- **Boolean**: `true` / `false`
- **ID (serialized as String)**: Unique identifier often used to fetch and object or as cache key

#### Object types

    An object types contains the `collection of fields`, `each with its own type`.
```
type Employee {
    id: ID
    name: String
    salary: Int
    isActive: Boolean
    manager: Employee
}
```

> `__typename` field returns object type's name

#### Query type

`special type` which defines all of the `top-level entry points` for queries that cliets execute against your server `to read data`.

```
"""
Here we are declaring the root collections for each type
Server invokes these queries to get the data and combine as required
"""
type Query {
    employees: [Employee]
    departments: [Department]
    employeeByName(
        "Name of employee"
        name: String
    ): Employee[]

}

# Query structure

{
    query GetEmployeesAndManagers {
        employee {
            name
            salary
            manager {
                name
            }
        }
    }

    query GetEmployeeByName {
        employeeByName(name: "Sujaat")
    }
}
```

#### Mutation type

`special type` which defines all of the `top-level entry points` for queries that cliets execute against your server `to write data`.

```
type Mutation {
    postEmployee(name: String, salary: Int, isActive: Boolean): Employee
}

# Mutation structure

mutation CreateEmployee {
    postEmployee(name: "Adarsh Kumar", salary: 72345, isActive: true) {
        name
        salary
        isActive
        manager {
            name
            salary
        }
    }
}
```

#### Input types

`special object types` that allow you to provide hierarchical data as `arguments` to fields (as opposed to providing only flat scalar arguments). It is similar to an object type's, but it uses the input keyword.

```
input Employee {
    name: String
    salary: Int
}
```
#### Enum

An enum is similar to a scalar type, but its legal values are defined in the schema. It allows the user to pick from the list of options.
```
enum MediaFormat {
    IMAGE
    VIDEO
}
```

#### Input

#### Union

#### Interface

