from password import Password
from checker import PasswordChecker

def main():
    checker = PasswordChecker()

    while True:
        print("\nPassword Checker Menu")
        print("1. Check a password")
        print("2. View password history")
        print("3. Quit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":

            # Explain the rules before asking for a password
            print("\nYour password must meet ALL of these rules:")
            print("- At least 8 characters long")
            print("- At least one uppercase letter")
            print("- At least one lowercase letter")
            print("- At least one digit")
            print("- At least one symbol")

            # Keep asking until the password meets all regex rules
            while True:
                pwd_input = input("\nEnter a password: ")
                pwd = Password(pwd_input)

                rules = checker.check(pwd)
                score = checker.score(rules)

                # If all rules pass, break out of the loop
                if score == 5:
                    print("\nPassword accepted!")
                    checker.pretty_print(rules)
                    break
                else:
                    # Show which rules failed
                    print("\nPassword does NOT meet the requirements:")
                    checker.pretty_print(rules)
                    print("\nPlease try again.")

            # Now that the password is valid, show strength label
            label = checker.strength_label(score)
            print(f"\nStrength score: {score}/5")
            print(f"Password strength: {label}")

            # Save to history
            checker.save_to_history(pwd)
            print("Password saved to history.txt")

        elif choice == "2":
            checker.view_history()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    Main()

