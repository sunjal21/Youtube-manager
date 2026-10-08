# YouTube Manager

A simple and practical **console-based YouTube Manager** built with Python. This project demonstrates how to build a menu-driven application with **CRUD operations** and persistent data storage using JSON.

## Features

* **List Videos** — View all saved YouTube videos with their names and durations.
* **Add Video** — Add a new video with its name and duration.
* **Update Video** — Modify the details of an existing video.
* **Delete Video** — Remove a selected video from the collection.
* **Persistent Storage** — Video data is stored in a `youtube.txt` file using JSON.
* **Simple CLI** — Easy-to-use command-line menu for managing videos.

## Technologies Used

* **Python**
* **JSON**
* **File Handling**
* **CRUD Operations**
* **Pattern Matching (`match-case`)**

## Project Structure

```text
YouTube-Manager/
│
├── youtube_manager.py
├── youtube.txt
└── README.md
```

## How It Works

The application starts by loading existing video data from the JSON file. Users can then select an operation from the menu:

```text
1. List all YouTube videos
2. Add a YouTube video
3. Update a YouTube video
4. Delete a YouTube video
5. Exit the app
```

Whenever a video is added, updated, or deleted, the changes are automatically saved to the data file.

## How to Run

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Navigate to the project

```bash
cd YouTube-Manager
```

### 3. Run the application

```bash
python youtube_manager.py
```

## Example

```text
Youtube Manager | choose an option

1. List all youtube videos
2. Add a youtube video
3. Update a youtube video details
4. Delete a youtube video
5. Exit the app

Enter your choice:
```

## Learning Outcomes

Through this project, I practiced:

* Python functions and control flow
* Lists and dictionaries
* File handling
* JSON data serialization
* CRUD operations
* Exception handling
* `match-case` statements
* Building a simple real-world CLI application

## Future Improvements

Possible improvements include:

* Add video URLs and categories
* Add search functionality
* Improve input validation
* Replace JSON file storage with SQLite/MySQL
* Build a web version using Flask or FastAPI

## Author

**Sunjal Sammal**

BCA Student | Python Developer | Aspiring AI & Agentic AI Engineer

---

⭐ If you find this project useful, consider giving the repository a star!
