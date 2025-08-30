# Smart Team Builder - Week 1 / Sprint 1
# Basic program structure with quit function

def main():
    """
    Main program loop for Smart Team Builder
    Sprint 1 Goal:
    - Display welcome message
    - Allow quit (case-insensitive)
    - Handle invalid commands
    """
    # Data structure for storing teams (to be used in future sprints)
    teams = {}

    # Welcome message
    print("--- Welcome to Smart Team Builder! ---")
    print("Options: [quit]")

    while True:
        # Get user input (case-insensitive)
        command = input("\nEnter your command: ").lower()

        if command == "quit":
            print("--- Thank you for using Smart Team Builder! ---")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
