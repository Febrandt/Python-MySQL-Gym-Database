
# Python MySQL Gym Database

Python cli for Gym MySQL Database.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



## Database Tables


members 
|id|name|email|cpf|telephone|registration_date|
| :--------- | :--------- | :--------------------- | :-----------|:---------------|:-------------|
| `int` | `string` | `string`|`string`|`string`|`Date`|

payments 
|id|member_id|month|year|payment_status|
| :--------- | :--------- | :--------------------- | :-----------|:---------------|
| `int` | ` FOREIGN KEY` `int` | `int`|`int`|`bool`|



## Functionalities

- Add and Remove Members
- Add and Remove Payments
- Check for Member Payment



## Used for retrieving Data
- DTO - Data Transfer Object
- DAO - Data Abstract Object


## Console App Commands
- Add Member
- Remove Member
- Add Member Payment
- Remove Member Payment
- Check Member payment for the month
## What I learned

It was possible to understand MySQL commands as well as their integration into Python.
The ideas of connecting to the database, cursor, etc, were learned.
