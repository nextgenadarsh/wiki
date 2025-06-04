- [MongoDB Overview](#mongodb-overview)
  - [Key Features](#key-features)
  - [Terminologies](#terminologies)
    - [Document Database](#document-database)
    - [Database](#database)
    - [Collection](#collection)
    - [Document (BSON)](#document-bson)
    - [Views](#views)
    - [On-Demand Materialized Views](#on-demand-materialized-views)
- [Working with MongoDb](#working-with-mongodb)
  - [Basic](#basic)
    - [Show active/current database](#show-activecurrent-database)
    - [Switch active/current database](#switch-activecurrent-database)
    - [Creating database](#creating-database)
    - [Creating collection](#creating-collection)
      - [Creating collection index](#creating-collection-index)
      - [Creating views](#creating-views)
  - [RDBMS Vs MongoDB](#rdbms-vs-mongodb)
  - [MongoDB Architecture](#mongodb-architecture)
  - [Mongo Database- create, drop](#mongo-database--create-drop)
  - [Database Collection- create, view, drop, insert, find &](#database-collection--create-view-drop-insert-find-)
  - [Datatypes](#datatypes)
  - [Limit, Skip, Sort, findOne methods](#limit-skip-sort-findone-methods)
  - [Selection Relational & Logical Operator](#selection-relational--logical-operator)
  - [Update, Save & Delete documents](#update-save--delete-documents)

# MongoDB Overview

- Cross platform
- `Document database`
- Designed for ease of application development and `scaling`.
- Server  >  Databases(files)  >  Collections(Tables)  >  Documents  >  Key/Value pairs

## Key Features

- High Performance
  - Support for embedded data models `reduces I/O activity` on database system.
  - `Indexes` support faster queries and can include keys from embedded documents and arrays.
- Rich Query Language
  - MongoDB supports a rich query language to support read and write operations (CRUD) as well as:
    - Data Aggregation
    - Text Search and Geospatial Queries
- High Availability
  - MongoDB's replication facility, called replica set, provides:
    - automatic failover
    - data redundancy
  - A `replica set` is a group of MongoDB servers that maintain the same data set, providing `redundancy` and increasing data `availability`
- Horizontal Scalability
  - Sharding `distributes data` across a cluster of machines.
  - Starting in 3.4, MongoDB supports creating zones of data based on the shard key. In a balanced cluster, MongoDB directs reads and writes covered by a zone only to those shards inside the zone.
- Support for Multiple Storage Engines
  - `WiredTiger Storage Engine` (including support for Encryption at Rest)
  - `In-Memory` Storage Engine
  - MongoDB provides `pluggable storage engine API` that allows third parties to develop storage engines for MongoDB
  - 

## Terminologies

### Document Database

- A record in MongoDB is a document similar to JSON object.
- It is a data structure composed of key and value pairs.
- The values of fields may include other documents, arrays, and arrays of documents.
- Advantages:
  - Documents (i.e. objects) correspond to `native data types` in many programming languages.
  - Embedded documents and arrays `reduce need for expensive joins`
  - Dynamic schema supports `fluent polymorphism`

### Database

- Holds one or more collections of documents

### Collection

- MongoDB stores documents in collections.
- Collections are similar to tables in relational databases.
- Be default, a collection does not require its documents to have the same schema
- Optionally, MongoDB does support schema validation
- In addition to collections, MongoDB supports:
  - Read-only Views (Starting in MongoDB 3.4)
  - On-Demand Materialized Views (Starting in MongoDB 4.2).
- Collections are assigned an immutable UUID. The collection UUID remains the same across all members of a replica set and shards in a sharded cluster.

### Document (BSON)

- MongoDB stores data records as BSON documents
- Similar to JSON object
- The maximum BSON document size is 16 megabytes.
- Sample document:
```
{
    firstName: "Adarsh",
    lastName: "Kumar",
    hobbies: ["Blogging", "Listening Music", "Movies"]
}
```

### Views

- A queryable object whose contents are defined by an aggregation pipeline on other collections or views
- Does not persist the contents to disk
- Content is `computed on-demand` when a client queries the view
- MongoDB can require clients to have permission to query the view
- Views are read-only; write operations on views will error
- MongoDB does not support write operations against views
- Why need views?
  - To hide some sensitive data for general query
  - To add computed fields in response
  - To generate combined data using JOINs and hide complexity from applications

### On-Demand Materialized Views

- 

# Working with MongoDb

## Basic

### Show active/current database

`db`

### Switch active/current database

`use <<database_name>>`

### Creating database

There are different ways you can create a database:

- If a database does not exist, MongoDB creates the database when you first store data for that database. As such, you can switch to a non-existent database and perform the operation in mongosh.
  - `use nonExistentDb`
  - `db.myNewCollection.insertOne( { key: 10001 } )`


### Creating collection

- If a collection does not exist, MongoDB creates the collection when you first store data for that collection
  - `db.myNewCollection.insertOne( { key: 10001 } )`
- You can explicitly create collection using `db.createCollection(<<db_name>>, <<options>>)`

#### Creating collection index

- ``

#### Creating views

Views can be created in different ways:

- Using `db.createCollection`

```
db.createCollection(
  "<view_name>",
  {
    "viewOn" : "<source>",
    "pipeline" : [<pipeline>],
    "collation" : { <collation> }
  }
)
```

- Using `db.createView`

```
db.createView(
  "<view_name>",
  "<source>",
  [<pipeline>],
  {
    "collation" : { <collation> }
  }
)
```


## RDBMS Vs MongoDB



## MongoDB Architecture

## Mongo Database- create, drop

## Database Collection- create, view, drop, insert, find &  

## Datatypes

## Limit, Skip, Sort, findOne methods

## Selection Relational & Logical Operator

## Update, Save & Delete documents
