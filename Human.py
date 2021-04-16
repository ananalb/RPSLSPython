# Human

class Human:
    def main(self):
        print("Main Choice: Choose 1 of 5 choices")
        print("Choose 1 for Rock")
        print("Choose 2 for Paper")
        print("Choose 3 for Scissors")
        print("Choose 4 for Lizard")
        print("Choose 5 for Spock")

        choice = int(input("Please make a choice: "))

        if choice == "1":
            print("You chose Rock")
        elif choice == "2":
            print("You chose Paper")
        elif choice == "3":
            print("You chose Scissors")
        elif choice == "4":
            print("You chose Lizard ")
        elif choice == "5":
            print("You chose Spock")
        else:
            print("I don't understand your choice.")


