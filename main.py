from habits import new_habit
from rewards import new_reward

def main():
    program_active = 0
    command_names = ["exit", "qexit", "habits", "add",]
    name_list = []
    habit_list = []
    reward_list = []
    total_points = "NYI"
    print("\nWelcome to the habit tracker!")
    while program_active == 0:
        print(f"\nYou currently have {total_points} points.\n")
        print("Type a habit name to complete, edit, or delete the habit.")
        print("Type a reward name to buy, edit, or delete the reward.")
        print("Type 'habits' to list your current habits and rewards.")
        print("Type 'add' to create a new habit or reward.")
        print("Type 'exit' to save and close the program, or qexit to close without saving\n")
        response = input("Please select an option:\n")
        response = str.lower(response)
        if response == "exit":
            print("\nSaving not implemented, exiting program.\n")
            program_active = 1
        elif response == "qexit":
            program_active = 1
        elif response == "habits":
            print("\nNot Yet Implemented")
        elif response == "add":
            active = 0
            while active == 0:
                add_response = input("\nWould you like to add a new 'habit', or 'reward'? Type 0 to return.\n")
                if isinstance(add_response, str):
                    add_response = str.lower(add_response)
                if add_response == "habit":
                    active = 1
                    new_habit(name_list, habit_list, command_names)
                elif add_response == "reward":
                    active = 1
                    new_reward(name_list, reward_list, command_names)
                elif add_response == "0":
                    active = 1
                else:
                    print(f"{add_response} is not a valid response, please try again.\n")


if __name__ == "__main__":
    main()
