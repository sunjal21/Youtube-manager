import sqlite3

conn = sqlite3.connect("youtube_manager.db")
cursor = conn.cursor()


cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
"""
)


def list_videos():
  cursor.execute("SELECT * FROM videos")
  for row in cursor.fetchall():
    print(f"{row[0]}. | {row[1]} | {row[2]}")


def add_video(name, time):
  cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
  conn.commit()


def update_video(video_id, new_name, new_time):
  cursor.execute(
      "UPDATE videos SET name = ?, time = ? WHERE id = ?",
      (new_name, new_time, video_id),
  )
  conn.commit()


def delete_video(video_id):
  cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
  conn.commit()


def main():
  while True:
    print("\nYoutube Manager | choose an option")
    print("1. List all videos")
    print("2. Add a video")
    print("3. Update a video")
    print("4. Delete a video")
    print("5. Exit app")
    choice = input("Enter your choice: ")

    if choice == "1":
      list_videos()
    elif choice == "2":
      name = input("Enter video name: ")
      time = input("Enter video duration/time: ")
      add_video(name, time)
    elif choice == "3":
      video_id = input("Enter video ID to update: ")
      name = input("Enter updated video name: ")
      time = input("Enter updated video duration/time: ")
      update_video(video_id, name, time)
    elif choice == "4":
      video_id = input("Enter video ID to delete: ")
      delete_video(video_id)
    elif choice == "5":
      break
    else:
      print("Invalid choice. Please try again.")

  conn.close()


if __name__ == "__main__":
  main()
