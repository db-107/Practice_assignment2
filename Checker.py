import re
from password import Password

class PasswordChecker:
    def __init__(self, history_file="history.txt"):
        # File where passwords will be saved
        self.history_file = history_file

    def check(self, password: Password) -> dict:
        # Extract the raw password text
        raw = password.raw

        # Each rule uses regex or length checks
        rules = {
            "length >= 8": len(raw) >= 8,
            "uppercase letter": bool(re.search(r"[A-Z]", raw)),
            "lowercase letter": bool(re.search(r"[a-z]", raw)),
            "digit": bool(re.search(r"\d", raw)),
            "symbol": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", raw)),
        }

        return rules

    def score(self, rules: dict) -> int:
        # Count how many rules passed (True = 1)
        return sum(rules.values())

    def strength_label(self, score: int) -> str:
        # Convert score (0–5) into a human-friendly label
        if score <= 2:
            return "Weak"
        elif score == 3 or score == 4:
            return "Medium"
        else:
            return "Strong"

    def save_to_history(self, password: Password):
        # Append the password to a text file
        with open(self.history_file, "a") as f:
            f.write(password.raw + "\n")

    def view_history(self):
        # Read and display all saved passwords
        try:
            with open(self.history_file, "r") as f:
                lines = f.readlines()

                if not lines:
                    print("History is empty.")
                else:
                    print("\nPassword History:")
                    for line in lines:
                        print(line.strip())

        except FileNotFoundError:
            print("No history file found.")

    def pretty_print(self, rules: dict):
        # Display each rule and whether it passed
        print("\nPassword Check Results:")
        for rule, passed in rules.items():
            print(f"{rule}: {passed}")
