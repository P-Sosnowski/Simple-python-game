import random

games_played = 0
games_won = 0
games_lost = 0
nickname = ""

levels = {
    1: {"attempts": 10, "range": 30},
    2: {"attempts": 8, "range": 50},
    3: {"attempts": 6, "range": 100}
}

def save_stats():
    global filename
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Player statistics: {nickname}\n")
        file.write(f"Games played: {games_played}\n")
        file.write(f"Games won: {games_won}\n")
        file.write(f"Games lost: {games_lost}\n")
        if games_played > 0:
            percentage = (games_won / games_played) * 100
            file.write(f"Win rate: {percentage:.1f}%\n")

def choose_nickname():
    global nickname
    nickname = input("Choose your nickname: ").strip()
    if not nickname:
        nickname = "Player"
    print(f"Welcome {nickname}")

def show_stats():
    print()
    print(f"STATS for player {nickname}")
    print(f"Games played: {games_played}")
    print(f"Games won: {games_won}")
    print(f"Games lost: {games_lost}")
    if games_played > 0:
        percentage = (games_won / games_played) * 100
        print(f"Win rate: {percentage:.1f} %\n")

def show_rules():
    print("Welcome to the game, choose difficulty level: \n")
    print("Easy - 1, number range: 1-30, attempts: 10")
    print("Medium - 2, number range: 1-50, attempts: 8")
    print("Hard - 3, number range: 1-100, attempts: 6\n")

def choose_level():
    while True:
        try:
            choice = int(input("Choose difficulty level: "))
            if 1 <= choice <= 3:
                return choice, levels[choice]
            else:
                print("Please enter a valid number")
        except ValueError:
            print("That's not a number, try again")

def play_game():
    global games_played, games_won, games_lost

    print("\n--- Let's start the game! ---\n")

    level, settings = choose_level()
    attempts = settings["attempts"]
    number_range = settings["range"]
    shots = 0
    secret_number = random.randint(1, number_range)
    games_played += 1

    while shots < attempts:
        try:
            guess = int(input(f"\nAttempt {shots + 1}/{attempts} - Enter your guess: "))
            if guess == secret_number:
                print(f"Congratulations! You guessed in {shots + 1} tries.")
                games_won += 1
                break
            hint = "Too low" if guess < secret_number else "Too high"
            shots += 1
            print(f"{hint}, remaining attempts: {attempts - shots}")
        except ValueError:
            print("That's not a number, try again")
    else:
        print(f"You lost! The number was {secret_number}")
        games_lost += 1

def ask_to_continue():
    print(f"{nickname}, do you want to play again? Answer 'yes' or 'no'")
    while True:
        answer = input("Your answer: ").strip().lower()
        if answer == "yes":
            print("Let's go again!")
            return True
        elif answer == "no":
            print("Game over")
            return False
        else:
            print("Please type 'yes' or 'no'")

def load_stats():
    global games_played, games_won, games_lost, filename
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                if "Games played" in line:
                    games_played = int(line.split(":")[1].strip())
                elif "Games won" in line:
                    games_won = int(line.split(":")[1].strip())
                elif "Games lost" in line:
                    games_lost = int(line.split(":")[1].strip())
    except FileNotFoundError:
        games_played = 0
        games_won = 0
        games_lost = 0

# GAME START
choose_nickname()
filename = f"stats_{nickname}.txt"
load_stats()
show_rules()

while True:
    play_game()
    show_stats()
    save_stats()
    if not ask_to_continue():
        break
    print("\n" + "=" * 30 + "\n")