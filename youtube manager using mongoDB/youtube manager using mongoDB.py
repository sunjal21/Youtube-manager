import os
from dotenv import load_dotenv
from pymongo import MongoClient
from bson import ObjectId

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))

# Not a good idea to include id and password in code files
#  tlsAllowInvalidCertificates=True - Not a good way to handle ssl

print(client)

db = client["youtube_manager"]
video_collection = db["videos"]

# print(video_collection)


def add_video(name, time):
    video_collection.insert_one({
        "name": name,
        "time": time
    })


def list_videos():
    videos = list(video_collection.find())

    if not videos:
        print("\n VIDEO LIST IS EMPTY.")
        return

    for video in videos:
        print(
            f"ID: {video['_id']}, "
            f"Name: {video['name']} and "
            f"Time: {video['time']}"
        )


def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {"_id": ObjectId(video_id)},
        {
            "$set": {
                "name": new_name,
                "time": new_time
            }
        }
    )


def delete_video(video_id):
    video_collection.delete_one(
        {"_id": ObjectId(video_id)}
    )


def main():
    while True:
        print("\nYoutube Manager App")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()

        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)

        elif choice == "3":
            video_id = input("Enter the video ID to update: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated video time: ")
            update_video(video_id, name, time)

        elif choice == "4":
            video_id = input("Enter the video ID to delete: ")
            delete_video(video_id)

        elif choice == "5":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()