# Agenda
- Overview
- Basic 
	- Database Diagram
	- Relationship
	- Constraint
	- Data type
- Query
	- Insert
	- Select
	- Update
	- Delete

# I. Overview
- Common database
	- Many types of database

	- SQL and NoSQL
		- SQL: SQL Server, MySQL, Oracle, Sqlite (Mobile - FE), Postgres SQL
		- NoSQL: MongoDB, ...

- Relational database
	- Postgres

- Compare with data structure:
	- https://www.geeksforgeeks.org/difference-between-database-and-data-structure/

# II. Basic 
## 1. ERD & Database diagram 
- https://app.moqups.com/hvcaMbCu0i/edit/page/aeb26a055
	
## 2. Relationship
- One to One
- One to Many
- Many to One
- Many to Many
	
## 3. Constraint:
- PK
- FK
- Unique
- Not NULL

## 4. Data type
- string: varchar, char
- number: int2, int4, int8
- boolean
- datetime: timestamp, timestamp with timezone

# III. Query
- Five types of SQL commands: DDL, DML, DCL, TCL, DQL
	- https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/
- Focus on DQL

## 1. Insert
- https://www.postgresqltutorial.com/postgresql-insert/
```sql
INSERT INTO table_name(column1, column2, …)
VALUES (value1, value2, …);
```

## 2. Select
- https://www.postgresqltutorial.com/postgresql-select/
```sql
SELECT
   select_list
FROM
   table_name;
```
## 3. Update
- https://www.postgresqltutorial.com/postgresql-update/
```sql
UPDATE table_name
SET column1 = value1,
    column2 = value2,
    ...
WHERE condition;
```

## 4. Delete
- https://www.postgresqltutorial.com/postgresql-delete/

```sql
DELETE FROM table_name
WHERE condition;
```

# IV. Summary
- Basic 
	- Database Diagram
	- Relationship
	- Constraint
	- Data type
- Query
	- Insert
	- Select
	- Update
	- Delete

## Open:
- NoSQL: MongoDB
