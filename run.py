def start_game():
    """
    Show game introduction and instructions to user and
    provide option to initiate game
    """
    while True:
        user_start = input("Y/N\n").upper()

        try:
            if user_start == "Y":
                break
            elif user_start == "N":
                print("Maybe next time!")
                exit()
            else:
                raise ValueError
        except ValueError:
            print(f"Invalid input: {user_start}. Please type 'Y' or 'N'")

    return user_start


def create_user():
    """
    Let's the user create a username for the game
    """
    print("Excellent! Before we get started, what should we call you?")

    while True:
        username = input("Enter username: ")

        try:
            if username.isalnum() is False:
                raise ValueError(
                    print(f"{username} not valid. Numbers and letters only")
                )
            elif len(username) < 3:
                raise ValueError(
                    print("Username must be at least 3 characters")
                )
        except ValueError:
            print("Invalid username, please try again")
        else:
            break

    return username


# def main():
#     """
#     Run main game functions
#     """
#     start_game()
#     print(start_game())


print("Hello and welcome to...\n")
print("WIZARD DUEL!\n")
print("Instructions:")
print("Test your wizarding skills against the computer.")
print("For each new round, you can choose to attack ('A'),")
print("defend ('D') or sneak ('S') by selecting the")
print("corresponding letter on your keyboard.")
print("Attacking beats sneaking, sneaking beats defending")
print("and defending beats attacking. Think rock, paper, scissors,")
print("only magical!\n")
print("Now that you know the rules, would you like to play?")

# main()
start_game()
print(f"Hello {create_user()}! Let's duel")
