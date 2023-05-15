# Database Operations Using Python 3

## Why Use Python to Access SQLite?

SQLite is a lightweight disk-based database, meaning data is stored ona hard drive or other type of local storage. This is useful for prototyping applications that can then be transferred to a larger database such as Oracle or PostgreSQL.

Python can make use of SQLite through the `sqlite3` module. 

## Connecting to SQLite in Python

Once `sqlite3` has been imported, a *connection* needs to be established. If the database does not exist at the time of the connection being made, it will create a *new* blank database.

With a connection established, a *cursor* needs to be created to enable querying between the application and the database file.

All of the above is shown in the following code snippet.

```py
import sqlite3

"""
Change database name according to the appropriate location
"""
connection_object = sqlite3.connect("Database_Operations\\databases\\notes_database.db")

cursor_object = sqlite3.cursor()
```

## Executing SQL Queries in Python Using `.execute()`

A table can be created in the database using the cursor object defined previously. This is done through the `CREATE TABLE` command as shown below.

```py
"""
Creating a passengers table
"""
cursor_object.execute("""
                      CREATE TABLE passengers (
                        id INTEGER,
                        first_name TEXT,
                        last_name TEXT,
                        age INTEGER
                      )
                      """)
```

Data can be inserted into an existing table also using the cursor object. This is done through the `INSERT INTO` command as shown below.

```py
"""
Inserting a passenger into the passengers table
"""
cursor_object.execute("""
                      INSERT INTO passengers VALUES (
                        123456,
                        "Brian",
                        "Dobs",
                        27
                      )
                      """)
```

## Inserting Multiple Rows with `.executemany()`

To insert multiple rows into a table at once, there must be a list of tuples that contain the data needing to be inserted. Once this has been satisfied, the wildcard operator of SQL `?` can be used to account for arbitrary data types and allow the query to execute smoothly as shown below.

```py
new_passengers = [(123, "Bob", "Francis", 21), (456, "Simon", "Fry", 35), (789, "Alice", "Hally", 19)]

cursor_object.executemany("""
                          INSERT INTO passengers VALUES (
                            ?,
                            ?,
                            ?,
                            ?
                          )
                          """, new_passengers)
```

## Retrieving Data

There are three `fetch` methods:
- `fetchone()` which returns the first value that satisfies the query;
- `fetchmany(number)` which returns a specific number of values that satisfy the query;
- `fetchall()` which returns all values that satisfy the query.

For example:

```py
"""
Return all data for passengers who are over the age of 18
"""
cursor_object.execute("""
                      SELECT * FROM passengers
                      WHERE age > 18;
                      """).fetchall()
```

## Using Loops with SQLite

Loops can be used to perform aggregate operations and other meaningful data manipulation techniques on retrieved data. For example:

```py
ages = cursor_object.execute("""
                             SELECT age FROM passengers;
                             """).fetchall()

number_of_under_18s = 0

for age in ages:
    if age[0] < 18:
        number_of_under_18s += 1

print(number_of_under_18s)
```

## Committing and Closing a Database Connection

After manipulating the database, the changes need to be *committed* and the connection *closed* to prevent data leaks. This is done using the following commands.

```py

# Commit the changes to the database
connection_object.commit()

# Close the connection between the application and the database
connection_object.close()
```