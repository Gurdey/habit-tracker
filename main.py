from tkinter import *
from tkinter import font

root = Tk()
root.title("Habit Tracker")
root.geometry("600x325")

myLabel1 = Label(root, text="First Label")
myLabel2 = Label(root, text="Second Long Label")
myLabel3 = Label(root, text="Third Label")
myLabel4 = Label(root, width=20)
# myFrame1 = Frame(root, width=30, height=25, bg="lightgreen")
# myFrame2 = Frame(root, width=30, height=25, bg="lightgreen")
# myFrame3 = Frame(root, width=30, height=25, bg="lightgreen")
# myFrame4 = Frame(root, width=30, height=25, bg="lightgreen")
# myFrame5 = Frame(root, width=30, height=25, bg="lightgreen")
# myFrame6 = Frame(root, width=30, height=25, bg="lightgreen")
# myFrame7 = Frame(root, width=30, height=25, bg="lightgreen")
# myFrame8 = Frame(root, width=30, height=25, bg="lightgreen")
# myFrame9 = Frame(root, width=30, height=25, bg="lightgreen")
# myFrame10 = Frame(root, width=30, height=25, bg="lightgreen")
myFrameTest = Frame(root, width=600, height=25, bg="lightgreen")
myFrameTest2 = Frame(root, width=30, height=325, bg="lightgreen")

#myLabel1.grid(row=1, column=0)
#myLabel2.grid(row=2, column=0)
#myLabel3.grid(row=1, column=2)
#myLabel4.grid(row=1, column=1)
# myFrame1.grid(row=0, column=0)
# myFrame2.grid(row=0, column=1)
# myFrame3.grid(row=0, column=2)
# myFrame4.grid(row=0, column=3)
# myFrame5.grid(row=0, column=4)
# myFrame6.grid(row=0, column=5)
# myFrame7.grid(row=0, column=6)
# myFrame8.grid(row=0, column=7)
# myFrame9.grid(row=0, column=8)
# myFrame10.grid(row=0, column=9)
myFrameTest.grid(row=0, columnspan=20, sticky='n')
myFrameTest2.grid(row=1, rowspan=12, column=0, padx=0, sticky='w')
#myLabel1.grid(row=1, column=4, sticky='nw')
#myLabel2.grid(row=1, column=10, sticky='w')

root.mainloop()


#Old text-based code
"""
from habits import new_habit
from rewards import new_reward

def main():
    
    program_active = 0
    command_names = ["exit", "qexit", "habits", "add",]
    name_dict = []
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
        if response in command_names:
            if response == "exit":
                print("\nSaving not implemented, exiting program.\n")
                program_active = 1
            elif response == "qexit":
                program_active = 1
            elif response == "habits":
                print("\nHabits List")
                print("Habit    Points  Type")
                for habit in habit_list:
                    print(habit)
                print("\nRewards List")
                print("Reward   Cost    Type")
                for reward in reward_list:
                    print(reward)
            elif response == "add":
                active = 0
                while active == 0:
                    add_response = input("\nWould you like to add a new 'habit', or 'reward'? Type 0 to return.\n")
                    if isinstance(add_response, str):
                        add_response = str.lower(add_response)
                    if add_response == "habit":
                        active = 1
                        new_habit(name_dict, habit_list, command_names)
                    elif add_response == "reward":
                        active = 1
                        new_reward(name_dict, reward_list, command_names)
                    elif add_response == "0":
                        active = 1
                    else:
                        print(f"{add_response} is not a valid response, please try again.\n")
        elif response in name_dict:
            if name_dict[response] == "h":
                for habit in habit_list:
                    if habit.name == response:
                        print("Habit Found: NYI")
            elif name_dict[response] == "r":
                for reward in reward_list:
                    if reward.name == response:
                        print("Reward Found: NYI")

if __name__ == "__main__":
    main()
"""