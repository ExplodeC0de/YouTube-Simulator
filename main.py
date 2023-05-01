import random
from colorama import Fore
import time as delayer
import webbrowser

print(Fore.LIGHTGREEN_EX + "Welcome to ExplodeCode's YouTuber Simulator!")
print(Fore.LIGHTGREEN_EX + "In this game, you will be creating videos and trying to grow your channel.")
print(Fore.LIGHTGREEN_EX + "Let's get started!")
channel_name = input(Fore.BLUE + "What would you like to name your channel? ")
subscribers = 0
videos = []
money = 0

while True:
    # Display current status
    print("\nYour channel, " + channel_name + ", has " + str(subscribers) + " subscribers and $" + str(
        money) + " in the bank.")
    if len(videos) > 0:
        print("You have " + str(len(videos)) + " videos uploaded.")
        print(
            "Your most recent video, \"" + videos[-1] + "\", has " + str(random.randint(100, 1000)) + " views so far.")
    else:
        print("You haven't uploaded any videos yet.")

    # Ask player action :)
    action = input(
        "\nWhat would you like to do? Type 'upload' to create a new video, 'promote' to promote your channel, or 'quit' to end the game. ")

    # creates the videos :)
    if action == "upload":
        title = input("What would you like to name your video? ")
        category = input("What category does your video belong to? ")
        video_length = int(input("How long is your video (in minutes)? "))
        views = random.randint(100, 1000) * (video_length / 10)  # Views based on video length
        subscribers_gained = random.randint(1, 10) * (views / 1000)  # Subscribers gained based on views
        money_earned = random.randint(1, 5) * (views / 1000)  # Money earned based on views
        subscribers += int(subscribers_gained)
        money += int(money_earned)
        videos.append(title)
        print("Your video, \"" + title + "\", has been uploaded and has received " + str(int(views)) + " views!")
        print("You gained " + str(int(subscribers_gained)) + " subscribers and earned $" + str(
            int(money_earned)) + " from this video.")

    # Promote your channel :D
    elif action == "promote":
        promotion_cost = random.randint(10, 50)
        if money >= promotion_cost:
            money -= promotion_cost
            subscribers += random.randint(10, 100)
            print("You paid $" + str(promotion_cost) + " to promote your channel and gained " + str(
                int(subscribers_gained)) + " subscribers!")
        else:
            print("You don't have enough money to promote your channel.")

    elif action == "watch something":
        print("An Advertisement has appeared")
        skipornah = input(
            "\nWhat would you like to do? Type 'skip' to skip to the video, 'quit' to end the game, or 'watch' to wath the advert. ")
        if skipornah == "skip":
            print("Video will start playing now...")
            for i in range(5, 0, -1):
                print(Fore.LIGHTYELLOW_EX + str(i))
                print("\n")
                delayer.sleep(1)
            delayer.sleep(1)
            video_url = "https://youtu.be/25fsJs2g0f0"  # replace with the URL of the YouTube video you want to open
            webbrowser.open_new_tab(video_url)


    # Quit the game (please play for eternity :\  )
    elif action == "quit":
        print(Fore.RED + "Thanks for playing!")
        break

    # Invalid input :(
    else:
        print("Invalid input. Try again.")
