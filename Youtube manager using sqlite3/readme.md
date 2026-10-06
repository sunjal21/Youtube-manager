# YouTube Manager - SQLite

A simple command-line YouTube Manager application built with Python and SQLite3. The application allows users to store and manage video information using basic CRUD (Create, Read, Update, Delete) operations.

---

## Project Overview

YouTube Manager is a Python-based command-line application designed to manage a collection of YouTube videos.

The application stores video information in a local SQLite database and provides a menu-driven interface for performing common database operations.

Users can:

* View all stored videos
* Add new videos
* Update existing videos
* Delete videos
* Exit the application

The project demonstrates how Python can be connected with a relational database and used to perform SQL operations.

---

## Key Features

### Video Management

* Add new videos with name and duration
* Display all stored videos
* Update video details using the video ID
* Delete videos using the video ID

### Database Management

* Uses SQLite3 for persistent data storage
* Automatically creates the database table if it does not exist
* Uses auto-incrementing IDs for videos
* Commits database changes after insert, update, and delete operations

### Command-Line Interface

* Simple menu-driven interface
* Easy-to-understand user interaction
* Continuous menu loop until the user chooses to exit

---

## Technologies Used

| Technology   | Purpose                             |
| ------------ | ----------------------------------- |
| Python 3     | Application development             |
| SQLite3      | Database management                 |
| SQL          | Database queries                    |
| Git & GitHub | Version control and project hosting |

---

## Concepts Demonstrated

This project demonstrates the following programming and database concepts:

* Python functions
* Conditional statements
* While loops
* User input
* SQL queries
* CRUD operations
* Database connections
* SQLite database management
* Parameterized SQL queries
* Database transactions
* Auto-incrementing primary keys

---

## Project Structure

```text
YouTube Manager/
│
├── youtube manager using sqlite3.py
├── youtube_manager.db
└── README.md
```

### File Description

| File                               | Description                                     |
| ---------------------------------- | ----------------------------------------------- |
| `youtube manager using sqlite3.py` | Main Python application                         |
| `youtube_manager.db`               | SQLite database used to store video information |
| `README.md`                        | Project documentation                           |

> The SQLite database file can be generated automatically when the application is executed.

---

## Database Structure

The application uses a table named `videos`.

```sql
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    time TEXT NOT NULL
);
```

### Columns

| Column | Data Type | Description                   |
| ------ | --------- | ----------------------------- |
| `id`   | INTEGER   | Unique ID for each video      |
| `name` | TEXT      | Name of the video             |
| `time` | TEXT      | Duration or time of the video |

The `id` column uses `AUTOINCREMENT`, allowing SQLite to automatically assign a unique ID to each new video.

---

# Installation and Setup

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

Navigate to the project directory:

```bash
cd your-repository-name
```

---

## 2. Verify Python Installation

Check whether Python is installed:

```bash
python --version
```

or:

```bash
python3 --version
```

The project uses Python's built-in `sqlite3` module, so no additional database package is required.

---

## 3. Run the Application

Run the Python file:

```bash
python "youtube manager using sqlite3.py"
```

On systems where `python3` is required:

```bash
python3 "youtube manager using sqlite3.py"
```

---

# How to Use

After starting the application, the following menu will be displayed:

```text
Youtube Manager | choose an option

1. List all videos
2. Add a video
3. Update a video
4. Delete a video
5. Exit app

Enter your choice:
```

---

## 1. List All Videos

Select option:

```text
1
```

The application retrieves all videos from the database and displays them.

Example:

```text
1. | Python Tutorial | 10:30
2. | HTML Tutorial | 15:20
3. | CSS Tutorial | 20:15
```

The application uses the following SQL query:

```sql
SELECT * FROM videos;
```

---

## 2. Add a Video

Select option:

```text
2
```

Enter the video information:

```text
Enter video name: Python Tutorial
Enter video duration/time: 10:30
```

The application stores the information in the database using an `INSERT` query.

```sql
INSERT INTO videos (name, time)
VALUES (?, ?);
```

The changes are then saved using:

```python
conn.commit()
```

---

## 3. Update a Video

Select option:

```text
3
```

Enter the ID of the video you want to update:

```text
Enter video ID to update: 1
Enter updated video name: Advanced Python Tutorial
Enter updated video duration/time: 18:45
```

The application updates the selected record using:

```sql
UPDATE videos
SET name = ?, time = ?
WHERE id = ?;
```

---

## 4. Delete a Video

Select option:

```text
4
```

Enter the ID of the video you want to delete:

```text
Enter video ID to delete: 2
```

The application removes the selected video using:

```sql
DELETE FROM videos
WHERE id = ?;
```

The database is then updated using:

```python
conn.commit()
```

---

## 5. Exit the Application

Select option:

```text
5
```

The application exits the loop and closes the database connection.

```python
conn.close()
```

---

# CRUD Operations

The project implements the four fundamental database operations:

| Operation | Function         | SQL Operation |
| --------- | ---------------- | ------------- |
| Create    | `add_video()`    | `INSERT`      |
| Read      | `list_videos()`  | `SELECT`      |
| Update    | `update_video()` | `UPDATE`      |
| Delete    | `delete_video()` | `DELETE`      |

This makes the project a practical example of implementing CRUD functionality using Python and SQLite.

---

# Application Workflow

```text
Start Application
       |
       v
Connect to SQLite Database
       |
       v
Create videos Table if Required
       |
       v
Display Menu
       |
       +----> 1. List Videos
       |
       +----> 2. Add Video
       |
       +----> 3. Update Video
       |
       +----> 4. Delete Video
       |
       +----> 5. Exit
                    |
                    v
             Close Database
                    |
                    v
              End Application
```

---

# SQL Queries Used

### Create Table

```sql
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    time TEXT NOT NULL
);
```

### Read Videos

```sql
SELECT * FROM videos;
```

### Insert Video

```sql
INSERT INTO videos (name, time)
VALUES (?, ?);
```

### Update Video

```sql
UPDATE videos
SET name = ?, time = ?
WHERE id = ?;
```

### Delete Video

```sql
DELETE FROM videos
WHERE id = ?;
```

---

# Security Considerations

The application uses parameterized SQL queries with placeholders such as `?`.

For example:

```python
cursor.execute(
    "INSERT INTO videos (name, time) VALUES (?, ?)",
    (name, time)
)
```

Parameterized queries are preferable to directly inserting user input into SQL statements because they help protect against SQL injection.

---

# Learning Outcomes

Through this project, I gained practical experience with:

* Python programming
* SQLite database integration
* SQL commands
* CRUD operations
* Database connections
* Functions and modular programming
* User input handling
* Database transactions
* Parameterized queries
* Command-line application development

---

# Future Improvements

The project can be extended with additional features such as:

* Search videos by name
* Store YouTube video URLs
* Add video categories
* Add upload dates
* Add video descriptions
* Add input validation
* Improve error handling
* Add user authentication
* Build a graphical user interface
* Convert the application into a Flask web application
* Add automated testing
* Add video statistics

---

# Project Purpose

The main purpose of this project is to understand how a Python application communicates with a database and performs CRUD operations.

The basic application flow is:

```text
User Input
    |
    v
Python Application
    |
    v
SQL Query
    |
    v
SQLite Database
    |
    v
Stored / Retrieved Data
    |
    v
Application Output
```

---

# Author

**Sunjal Sammal**

BCA Student | Python and Web Development Enthusiast

### Technologies

`Python` `SQLite` `SQL` `Git` `GitHub`

---

# License

This project is created for educational and learning purposes.
