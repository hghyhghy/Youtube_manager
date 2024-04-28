
import pymongo
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://youtubepy:youtubepy@cluster0.ax0dpye.mongodb.net/",tlsAllowInvalidCertificates=True)

db= client["ytmanager"]

video_collection = db["video"]

print(client)


def add_video(name,time):

    video_collection.insert_one({"name":name,"time":time})

def list_videos():

     for video in video_collection.find():
         
         print(f"ID:{video["_id"]}, Name:{video['name']} and  Time:{video['time']}")

def update_video(video_id,name,time):

    video_collection.update_one({'_id':ObjectId(video_id)},{"$set":{"name":name,"time":time}})

def delete_video(video_id):

    video_collection.delete_one({"_id":video_id})

def main():

    while True:

        print("\n youtube manager app")
        print("1. List All Videos")
        print("2. Add a new videos")
        print("3. Update a videos")
        print("4. Delete a videos")
        print("5. Exit the app")

        choice = input("Enter your choice: ")

        if choice == "1":

            list_videos()

        elif choice == '2':

            name = input("Enter name of the video: ")
            time = input("Enter time of the video: ")
            add_video(name, time)

        elif choice == '3':

            video_id = input("Enter the video id to update: ")
            name = input("Enter updated name of the video: ")
            time = input("Enter updated time of the video: ")
            update_video(video_id, name, time)


        elif choice == '4':
            video_id = input("Enter the video id to delete: ")
            delete_video(video_id)

        elif choice == '5':

            break

        else:

            print("Invalid choice")


if __name__ =="__main__":

    main()
