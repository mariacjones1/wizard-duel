import random


def welcome_message():
    """
    Prints welcome message and game instructions
    """
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


def start_game():
    """
    Ask if user wants to initiate the game
    """
    while True:
        user_start = input("Y/N\n").upper()

        if user_start == "Y":
            break
        elif user_start == "N":
            print("Maybe next time!")
            exit()
        else:
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
                raise TypeError
            elif len(username) < 3:
                raise ValueError
        except TypeError:
            print("Username should use numbers and letters only.")
        except ValueError:
            print("Username must be at least 3 characters.")
        else:
            break

    return username


class Score:
    """
    A class to represent user or computer scores
    """
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def show_score(self):
        """
        Shows score
        """
        return self.name + " score: " + str(self.score)


def cast_spells():
    """
    Gets user to input a spell and generates a random one for the computer
    """
    spells = ["A", "D", "S"]

    while True:
        user_spell = input("Choose your spell: A, D or S: ").upper()

        try:
            if user_spell not in spells:
                raise ValueError
            else:
                break
        except ValueError:
            print(f"Invalid spell: {user_spell}. Please try again.")

    cpu_spell = random.choice(spells)
    return user_spell, cpu_spell


def declare_round_winner(user_spell, cpu_spell):
    """
    Calculate and declare the winner for each round
    """
    if user_spell == "A":
        if cpu_spell == "A":
            result = "draw"
        if cpu_spell == "D":
            result = "cpu_win"
        if cpu_spell == "S":
            result = "user_win"

    if user_spell == "D":
        if cpu_spell == "A":
            result = "user_win"
        if cpu_spell == "D":
            result = "draw"
        if cpu_spell == "S":
            result = "cpu_win"

    if user_spell == "S":
        if cpu_spell == "A":
            result = "cpu_win"
        if cpu_spell == "D":
            result = "user_win"
        if cpu_spell == "S":
            result = "draw"

    return result


def main():
    """
    Run main game functions
    """
    welcome_message()

    while True:
        start_game()
        username = create_user()
        print(f"Hello {username}! Let's duel")
        cpu_score = Score("Computer", 5)
        user_score = Score(username, 5)

        while user_score.score > 0 and cpu_score.score > 0:
            print(cpu_score.show_score())
            print(user_score.show_score())
            user_spell, cpu_spell = cast_spells()
            print(f"You cast: {user_spell}!")
            print(f"Computer cast: {cpu_spell}!")

            if declare_round_winner(user_spell, cpu_spell) == "draw":
                print("Draw! Cast a new spell\n")
            elif declare_round_winner(user_spell, cpu_spell) == "user_win":
                print("You win!\n")
                cpu_score.score -= 1
            elif declare_round_winner(user_spell, cpu_spell) == "cpu_win":
                print("Computer wins!\n")
                user_score.score -= 1

        if user_score.score == 0:
            print("Computer wins!\n")
        elif cpu_score.score == 0:
            print("You win!")

        print("Would you like to play again?")


main()
