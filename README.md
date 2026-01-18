# Employee Management System (EMS)

A simple Employee Management System built with Python and MySQL, designed to run with XAMPP for easy local database management.

## Features

- Add, display, update, promote, remove, and search employee records
- Input validation for email and phone number
- Command-line interface

## Requirements

- Python 3.x
- XAMPP (for MySQL server)
- `mysql-connector-python` package

## Setup Instructions

### 1. Install XAMPP and Start MySQL

- Download and install [XAMPP](https://www.apachefriends.org/index.html).
- Open the XAMPP Control Panel and start the **MySQL** service.

### 2. Create the Database and Table

- Open **phpMyAdmin** (usually at [http://localhost/phpmyadmin](http://localhost/phpmyadmin)).
- Create a new database named `employee`.
- Run the following SQL to create the `empdata` table:

    ```sql
    CREATE TABLE empdata (
        Id INT PRIMARY KEY,
        Name VARCHAR(100),
        Email_Id VARCHAR(100),
        Phone_no VARCHAR(15),
        Address VARCHAR(255),
        Post VARCHAR(100),
        Salary INT
    );
    ```

### 3. Install Python Dependencies

Open a terminal and run:

```sh
pip install mysql-connector-python
```

### 4. Configure Database Connection

- The connection in `Employee.py` is set to:
  - host: `localhost`
  - user: `root`
  - password: (empty by default in XAMPP)
  - database: `employee`
- If you set a password for MySQL, update the `password` field in the code.

### 5. Run the Application

```sh
python Employee.py
```

Follow the menu to manage employee records.

## File Structure

- `Employee.py` — Main application file
- `create table.py` — Example script to create the database
- `README.md` — This file

## Notes

- Make sure MySQL is running in XAMPP before starting the application.
- All data is stored locally in your XAMPP MySQL server.

## License

For educational use only.
