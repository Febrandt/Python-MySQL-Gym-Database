
# Python CLI MySQL Gym Database

Python cli for Gym MySQL Database.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



## Database Explanation

Here's how the database was made.
```sql
CREATE DATABASE gym;
```


### members
|id|name|email|cpf|telephone|registration_date|
| :--------- | :--------- | :--------------------- | :-----------|:---------------|:-------------|
| `int` | `string` | `string`|`string`|`string`|`Date`|

```sql
CREATE TABLE `members` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `telephone` varchar(12) DEFAULT NULL,
  `registration_date` date DEFAULT current_timestamp()
)
```

### payments
|id|member_id|month|year|payment_status|
| :--------- | :--------- | :--------------------- | :-----------|:---------------|
| `int` | ` FOREIGN KEY` `int` | `int`|`int`|`bool`|

```sql
CREATE TABLE `payments` (
  `id` int(11) NOT NULL,
  `member_id` int(11) NOT NULL,
  `month` int(2) NOT NULL,
  `year` int(2) NOT NULL,
  `payment_status` tinyint(1) NOT NULL
)
```



## Brief Code Explanation

Here a simple and concise code explanation.

### main.py

- Handle database Connection
- Handle Members Table
- Handle Payments Table
- Run CLI

### CLI Commands
- Add Member
- Remove Member
- Add Member Payment
- Remove Member Payment
- Check Member payment for the month

### Used for receiving and retrieving data
- DTO - Data Transfer Object
- DAO - Data Abstract Object

## What I learned

It was possible to understand MySQL commands as well as their integration into Python.
The ideas of connecting to the database, cursor, etc, were learned.
