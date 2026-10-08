# YouTube Manager

A menu-driven, command-line application for managing a list of YouTube videos, built three ways: with a plain JSON file, with SQLite3, and with MongoDB.

The project demonstrates Python programming, CRUD operations, and database connectivity. It uses three different storage approaches: file-based storage, relational (SQL) storage, and document-based (NoSQL) storage.

---

## Project Overview

YouTube Manager is a console application that lets a user keep a record of YouTube videos, each with a name and a time (duration) value. The same application is implemented three times, and each version stores its data differently.

- The user interacts with the app through a numbered text menu in the terminal.
- Videos are entries typed in by the user. The project does not connect to YouTube or the YouTube API.
- The user can list, add, update, and delete video records.
- Each version keeps its data between runs, so records are still there the next time the program starts.
- Multiple implementations exist so the same CRUD logic can be compared across a JSON file, a relational database (SQLite3), and a NoSQL database (MongoDB).

---

## Project Objective

The purpose of this project is to practice building the same small application with different storage technologies and to understand how each one works.

Concepts demonstrated by the code in this repository:

- Python programming with functions, loops, and user input
- CRUD operations (Create, Read, Update, Delete)
- File handling and JSON serialization
- Database connectivity
- SQLite3 and SQL queries (relational approach)
- MongoDB and PyMongo (NoSQL, document-based approach)
- Loading configuration from environment variables with a `.env` file
- Git and GitHub for version control, including a `.gitignore` to keep secrets and local files out of the repository

---

## Key Features

- Menu-driven command-line interface with five options: list, add, update, delete, and exit
- Three separate implementations of the same application (JSON file, SQLite3, MongoDB)
- Persistent storage in all three versions
- Invalid menu choices are handled with a message, and the menu is shown again
- Python version: if the data file does not exist, the program starts with an empty list instead of crashing
- Python version: update and delete check that the selected video number is within range
- SQLite3 version: creates the `videos` table automatically if it does not exist
- SQLite3 version: uses parameterized SQL queries (`?` placeholders)
- MongoDB version: reads the connection string from an environment variable (`MONGODB_URI`) instead of hardcoding it
- MongoDB version: shows a message when the video list is empty
- MongoDB version: includes a separate script (`test.py`) to check the database connection

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main programming language for all three versions |
| json (standard library) | Reads and writes video data in the Python version |
| sqlite3 (standard library) | Connects to and queries the SQLite database |
| SQLite | File-based relational database used in the SQLite3 version |
| MongoDB | NoSQL document database used in the MongoDB version |
| PyMongo | Python driver used to connect to and operate on MongoDB |
| bson (included with PyMongo) | Provides `ObjectId` to look up MongoDB documents by `_id` |
| python-dotenv | Loads `MONGODB_URI` from a `.env` file |
| Git and GitHub | Version control and hosting of the project |

---

## Project Versions

### Python Version

Folder: `Youtube Manager using pyhton`

**How it stores data**

- Videos are kept in a Python list of dictionaries while the program runs.
- After every add, update, or delete, the full list is written to a file named `youtube.txt` in JSON format.
- Data is persistent. It is saved to disk and loaded again the next time the program starts.

Example of the stored structure:

```json
[{"name": "Example Video", "time": "10"}]
```

**Important functions** (no classes are used in this version)

| Function | Purpose |
|----------|---------|
| `load_data()` | Reads `youtube.txt` and returns the list; returns an empty list if the file is not found |
| `save_data_helper(videos)` | Writes the list to `youtube.txt` using `json.dump` |
| `list_all_videos(videos)` | Prints numbered videos with name and duration |
| `add_videos(videos)` | Asks for a name and time, appends a new entry, and saves |
| `update_videos(videos)` | Shows the list, asks for a video number, replaces that entry, and saves |
| `delete_videos(videos)` | Shows the list, asks for a video number, deletes that entry, and saves |
| `main()` | Runs the menu loop; uses a `match-case` statement to handle the user's choice |

**How CRUD works**

- Videos are identified by their position in the list (starting from 1).
- The video number is checked against the list length before an update or delete.

---

### SQLite3 Version

Folder: `Youtube manager using sqlite3`

**Database used**

- SQLite, accessed through Python's built-in `sqlite3` module.
- The database file is `youtube_manager.db`, created automatically in the folder the script is run from.
- Data is persistent because it is stored in the database file.

**Table structure** (from the `CREATE TABLE IF NOT EXISTS` statement in the code)

Table name: `videos`

| Column | Type | Constraints |
|--------|------|-------------|
| `id` | INTEGER | PRIMARY KEY AUTOINCREMENT |
| `name` | TEXT | NOT NULL |
| `time` | TEXT | NOT NULL |

**Important functions**

| Function | SQL used |
|----------|----------|
| `list_videos()` | `SELECT * FROM videos` |
| `add_video(name, time)` | `INSERT INTO videos (name, time) VALUES (?, ?)` |
| `update_video(video_id, new_name, new_time)` | `UPDATE videos SET name = ?, time = ? WHERE id = ?` |
| `delete_video(video_id)` | `DELETE FROM videos WHERE id = ?` |
| `main()` | Runs the menu loop and closes the connection when the user exits |

**Implementation details**

- A connection (`conn`) and cursor are created once at the top of the script.
- Add, update, and delete call `conn.commit()` to save changes.
- Values are passed as query parameters (`?`) rather than being inserted into the SQL string.
- Videos are identified by their `id` column.

---

### MongoDB Version

Folder: `youtube manager using mongoDB`

**Database and collection structure**

- Database name: `youtube_manager`
- Collection name: `videos`
- Data is persistent because it is stored in the MongoDB database.

**Document structure**

Each video is stored as a document with a `name` and a `time` field. MongoDB adds the `_id` field automatically when a document is inserted.

```json
{
  "_id": "ObjectId generated by MongoDB",
  "name": "Example Video",
  "time": "10"
}
```

**Connection method**

- `python-dotenv` loads the `.env` file with `load_dotenv()`.
- The connection string is read with `os.getenv("MONGODB_URI")` and passed to `MongoClient`.
- The database and collection are selected with `client["youtube_manager"]` and `db["videos"]`.
- The connection string is not written in the code.

**Important functions**

| Function | PyMongo operation |
|----------|-------------------|
| `add_video(name, time)` | `insert_one({"name": name, "time": time})` |
| `list_videos()` | `find()`; prints a message if the list is empty |
| `update_video(video_id, new_name, new_time)` | `update_one({"_id": ObjectId(video_id)}, {"$set": {...}})` |
| `delete_video(video_id)` | `delete_one({"_id": ObjectId(video_id)})` |
| `main()` | Runs the menu loop |

**Other implementation details**

- Videos are identified by their MongoDB `_id`. The user copies the ID shown in the list and pastes it when updating or deleting.
- The script prints the `MongoClient` object to the console when it starts.
- `test.py` is a separate script that only checks the connection. It raises an error if `MONGODB_URI` is missing, sends a `ping` command to the server, and prints a success or failure message.

---

## Project Structure

```text
Youtube-manager/
│
├── .gitignore
├── README.md
│
├── Youtube Manager using pyhton/
│   ├── youtube_manager.py
│   ├── youtube.txt
│   └── readme.md
│
├── Youtube manager using sqlite3/
│   ├── youtube manager using sqlite3.py
│   └── readme.md
│
└── youtube manager using mongoDB/
    ├── youtube manager using mongoDB.py
    ├── test.py
    ├── .gitignore
    └── readme.md
```

Files created locally when you use the project (not part of the repository):

- `youtube_manager.db`: created by the SQLite3 version on first run
- `.env`: created by you inside the MongoDB folder; excluded from Git by `.gitignore`

---

## Database Comparison

| Feature | Python | SQLite3 | MongoDB |
|---------|--------|---------|---------|
| Storage | JSON text file (`youtube.txt`) | Database file (`youtube_manager.db`) | MongoDB database (`youtube_manager`) |
| Database Type | None (flat file) | Relational (SQL) | NoSQL (document) |
| Persistence | Persistent (saved after each change) | Persistent (committed after each change) | Persistent (stored in MongoDB) |
| Data Structure | List of dictionaries with `name` and `time` | Table `videos` with `id`, `name`, `time` | Collection `videos` with documents (`_id`, `name`, `time`) |
| Python Library | `json` (standard library) | `sqlite3` (standard library) | `pymongo`, `python-dotenv` |
| Record Identifier | List position (1, 2, 3, ...) | Integer `id` | MongoDB `_id` (ObjectId) |
| Configuration | None | None | `MONGODB_URI` in a `.env` file |
| External Packages | None | None | `pymongo`, `python-dotenv` |

---

## Requirements

**Python**

- Python 3.10 or higher. The Python version uses a `match-case` statement, which was introduced in Python 3.10.

**Python version**

- No external packages. It uses the built-in `json` module.

**SQLite3 version**

- No external packages and no separate database installation.
- It uses the built-in `sqlite3` module that comes with standard Python installations.

**MongoDB version**

- External Python packages: `pymongo` and `python-dotenv`
- A MongoDB database that you can reach with a connection string. The project's `test.py` refers to MongoDB Atlas, and the connection string format used is the Atlas-style `mongodb+srv://` format.
- An internet connection when using MongoDB Atlas.
- A `.env` file containing `MONGODB_URI`.

The project does not include a `requirements.txt` file, so the packages are installed manually as shown below.

---

## Installation / Setup

**1. Clone the repository**

```bash
git clone https://github.com/sunjal21/Youtube-manager.git
cd Youtube-manager
```

**2. Check your Python version**

```bash
python --version
```

On macOS or Linux, use `python3` instead of `python` if `python` is not available.

**3. Create and activate a virtual environment (optional, recommended for the MongoDB version)**

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

**4. Install the packages (MongoDB version only)**

```bash
pip install pymongo python-dotenv
```

Do not install a separate package named `bson`. The `bson` module is already included with PyMongo, and a separate package can conflict with it.

The Python and SQLite3 versions need no installation step.

---

## How to Run

Run each command from the repository root folder (`Youtube-manager`). Each version must be started from inside its own folder, because the data file and the database file are created in the folder you run the script from.

**Python version**

```bash
cd "Youtube Manager using pyhton"
python youtube_manager.py
```

**SQLite3 version**

```bash
cd "Youtube manager using sqlite3"
python "youtube manager using sqlite3.py"
```

**MongoDB version**

Complete the MongoDB setup in the next section first, then run:

```bash
cd "youtube manager using mongoDB"
python test.py
python "youtube manager using mongoDB.py"
```

`test.py` is optional. It only checks that the connection works.

---

## MongoDB Setup

The MongoDB version needs a MongoDB database and a connection string.

1. Create a MongoDB Atlas account and a cluster (the project's `test.py` is written for Atlas).
2. Create a database user with a username and password.
3. In Atlas, allow your IP address to connect to the cluster.
4. Copy the connection string for your cluster from Atlas.
5. Inside the `youtube manager using mongoDB` folder, create a file named `.env` with this single line:

```text
MONGODB_URI=mongodb+srv://<username>:<password>@<cluster-host>/?<options>
```

6. Replace `<username>`, `<password>`, `<cluster-host>`, and `<options>` with the values from your own Atlas connection string. If your password contains special characters, URL-encode them.
7. Run `python test.py` to confirm that the connection works.

Notes:

- The connection string is configured only in the `.env` file. The Python code reads it from the `MONGODB_URI` variable.
- You do not need to create the `youtube_manager` database or the `videos` collection manually. The code does not create them explicitly, and MongoDB creates them when the first video is inserted.
- The code only reads the connection string from the environment, so the string decides where the program connects. A local MongoDB connection string is not covered by the project's own files and has not been tested here.

**Security warning**

- Never upload your real `.env` file or your password to GitHub.
- This repository's `.gitignore` files already list `.env`. Do not remove that entry.
- Do not paste the real connection string into the Python code, the README, or screenshots.
- If a password is ever exposed, change it in MongoDB Atlas immediately.

---

## Application Workflow

All three versions share the same menu loop. Only the startup step is different:

- Python version: loads the video list from `youtube.txt`
- SQLite3 version: connects to `youtube_manager.db` and creates the `videos` table if it does not exist
- MongoDB version: loads `MONGODB_URI` from `.env`, creates the client, and selects the `youtube_manager` database and `videos` collection

```text
Start
  ↓
Startup step (load file / connect to SQLite / connect to MongoDB)
  ↓
Display menu (options 1 to 5)
  ↓
User enters a choice
  ├── 1  List all videos
  ├── 2  Add a video (asks for name and time)
  ├── 3  Update a video (asks for the identifier, new name, and new time)
  ├── 4  Delete a video (asks for the identifier)
  ├── 5  Exit the app
  └── Anything else: "Invalid choice" message
  ↓
Data is saved to the file / database (for options 2, 3, and 4)
  ↓
Return to menu
  ↓
Exit (the SQLite3 version also closes its database connection)
```

---

## CRUD Operations

| Operation | Python version | SQLite3 version | MongoDB version |
|-----------|----------------|-----------------|-----------------|
| Create | `add_videos()` appends a dictionary to the list and saves the list to `youtube.txt` | `add_video()` runs `INSERT INTO videos` and commits | `add_video()` calls `insert_one()` |
| Read | `list_all_videos()` prints each video as a numbered line with name and duration | `list_videos()` runs `SELECT * FROM videos` and prints `id`, name, and time | `list_videos()` calls `find()` and prints `_id`, name, and time; shows a message if empty |
| Update | `update_videos()` asks for a list number, checks it is in range, replaces the entry, and saves | `update_video()` runs `UPDATE videos SET name = ?, time = ? WHERE id = ?` and commits | `update_video()` calls `update_one()` with `$set` on the matching `_id` |
| Delete | `delete_videos()` asks for a list number, checks it is in range, removes the entry with `del`, and saves | `delete_video()` runs `DELETE FROM videos WHERE id = ?` and commits | `delete_video()` calls `delete_one()` on the matching `_id` |

---

## What I Learned

- Writing Python programs with functions, loops, conditions, and user input
- Using `match-case` and `if/elif` for menu handling
- Working with lists and dictionaries
- File handling and JSON serialization with the `json` module
- Handling a missing file with `try/except FileNotFoundError`
- Implementing CRUD operations in three different ways
- Using SQLite3 with connections, cursors, and commits
- Writing SQL: `CREATE TABLE IF NOT EXISTS`, `INSERT`, `SELECT`, `UPDATE`, and `DELETE`
- Using parameterized queries instead of building SQL strings by hand
- Using MongoDB collections and documents through PyMongo (`insert_one`, `find`, `update_one`, `delete_one`)
- Using `ObjectId` to look up MongoDB documents by `_id`
- Connecting Python to a MongoDB database and testing the connection with a `ping` command
- Keeping credentials out of source code with environment variables and `python-dotenv`
- Understanding the difference between relational (SQL) and document (NoSQL) data storage
- Using Git and GitHub, including a `.gitignore` file to keep secrets and local files out of the repository

---

## Future Improvements

The items below are ideas for FUTURE work only. None of them exist in the current code.

- Input validation and error handling, for example for non-numeric video numbers and invalid MongoDB IDs
- Confirmation messages after add, update, and delete
- Search and sorting of videos
- Additional fields such as a video URL or category
- A `requirements.txt` file for easier installation
- Reducing repeated menu code across the three versions
- Unit tests
- A web interface using Flask or Django
- A REST API
- User authentication
- Pagination for long video lists
- Deployment of a web version

---

## Author

**Sunjal Singh Sammal**

BCA Student | Python / Full Stack Developer

GitHub: [https://github.com/sunjal21](https://github.com/sunjal21)

---

## License

This project is created for educational and learning purposes.
