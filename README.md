Python and SQL

This assignment focuses on implementing the database for Pizza Hat, a shop specializing in pizza-shaped hats. The assignment consists of three parts:

1. Creating and populating the database according to a configuration file.
2. Executing a list of orders, according to a second file.
3. Printing a summary in a third file.

## Requirements

- Python 3.6.9
- sqlite3

## Database Structure

The database will contain the following tables:

### hats

- `id` (INTEGER PRIMARY KEY)
- `topping` (STRING NOT NULL)
- `supplier` (INTEGER REFERENCES Supplier(id))
- `quantity` (INTEGER NOT NULL)

### suppliers

- `id` (INTEGER PRIMARY KEY)
- `name` (STRING NOT NULL)

### orders

- `id` (INTEGER PRIMARY KEY)
- `location` (STRING NOT NULL)
- `hat` (INTEGER REFERENCES hats(id))

## Configuration File

The configuration file has the following structure:

```
<#1>,<#2>
<hats>
<suppliers>
```

Where `<#1>` is the number of hat entries, and `<#2>` is the number of supplier entries. Each hat entry follows the format: `<id>,<topping>,<supplier>,<quantity>`, and each supplier entry follows the format: `<id>,<name>`.

## Orders File

The orders file has the following structure:

```
<location1>,<topping1>
<location2>,<topping2>
<location3>,<topping3>
<location4>,<topping4>
```

## Executing Orders

Each order will be executed, and the quantity of the corresponding hat in the database will be updated. If a hat topping has two or more suppliers, the inventory from the first supplier (ordered by id) will be used. If the quantity drops to zero, the entry should be removed from the database.

Executed orders will be inserted into the `orders` table, with a unique `id` starting from 1 and increasing by 1 for each order.

## Summary File

After each order, a line will be added to the summary file, with the following format:

```
<topping>,<supplier>,<location>
```

## Testing and Submission

The assignment will be tested automatically on the lab computers. You must use the exact specification provided for the output file and the database. Failing to do so will result in the automatic tests failing.

To test your assignment, run the following command:

```
python3 test_assignment.py ID1_ID2.zip config.txt orders.txt true_output.txt true_database.db
```

Your submission should include a `main.py` file, which will be used to run the assignment. You may add additional Python files, but everything should be zipped into `ID1_ID2.zip`.

Make sure to commit the changes to the database at the end of the code execution, as both the database and the output file will be checked.

**Note**: Do not use packages that are not available in the lab computers, as the testing is automatic, and your code will fail to run if a required package is missing.
