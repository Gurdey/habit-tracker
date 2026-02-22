from enum import Enum

class HabitType(Enum):
    SELFCARE = 1
    CHORES = 2
    EXERCISE = 3
    WORK = 4
    LEARNING = 5
    OTHER = 6

class Habit:
    def __init__(self, name, points, type):
        self.name = name
        self.points = points
        self.type = type

    def __str__(self):
        return f"{self.name},   {self.points},     {self.type}"
    
    def __repr__(self):
        return f"{self.name}, {self.points}, {self.type}"

def check_habit_type(type_str):
    if type_str == "1" or type_str == "self-care":
        return HabitType.SELFCARE
    if type_str == "2" or type_str == "chores":
        return HabitType.CHORES
    if type_str == "3" or type_str == "exercise":
        return HabitType.EXERCISE
    if type_str == "4" or type_str == "work":
        return HabitType.WORK
    if type_str == "5" or type_str == "learning":
        return HabitType.LEARNING
    if type_str == "6" or type_str == "other":
        return HabitType.OTHER
    raise Exception

def get_type_str(type):
    match type:
        case HabitType.SELFCARE:
            return "self-care"
        case HabitType.CHORES:
            return "chores"
        case HabitType.EXERCISE:
            return "exercise"
        case HabitType.WORK:
            return "work"
        case HabitType.LEARNING:
            return "learning"
        case HabitType.OTHER:
            return "other"
        case _:
            return "Error: Habit Type Not Found"

def new_habit(name_dict, habit_list, command_names):
    print("Creating new habit, type 'cancel' to return.")
    habit_name = input("\nWhat is the habits name?\n")
    habit_name = str.lower(habit_name)
    if habit_name == "cancel":
        return
    habit_points_str = input("\nHow many points is it worth?\n")
    valid_points = 1
    while valid_points == 1:
        habit_points_str = str.lower(habit_points_str)
        if habit_points_str == "cancel":
            return
        try:
            habit_points = int(habit_points_str)
            valid_points = 0
        except Exception:
            habit_points_str = input(f"{habit_points_str} is not a valid whole number, please enter a valid value:\n")
    habit_type_valid = 1
    while habit_type_valid == 1:
        habit_type_str = input("\nWhat type of habit is it?\n1. Self-care\n2. Chores\n3. Exercise\n4. Work\n5. Learning\n6. Other\n")
        habit_type_str = str.lower(habit_type_str)
        if habit_type_str == "cancel":
            return
        try:
            habit_type = check_habit_type(habit_type_str)
            habit_type_valid = 0
        except Exception:
            print(f"{habit_type_str} is not a valid habit type.\nPlease enter the number or name of the habit type.\n")
    existing_name = 1
    while existing_name == 1:
        if habit_name in command_names:
            habit_name = input(f"\n{habit_name} is already the name of a command, please enter a new name:\n")
            habit_name = str.lower(habit_name)
            if habit_name == "cancel":
                return
        elif habit_name in name_dict:
            habit_name = input(f"\n{habit_name} is already the name of an existing habit or reward, please enter a new name:\n")
            habit_name = str.lower(habit_name)
            if habit_name == "cancel":
                return
        else:
            existing_name = 0
    name_dict[habit_name] = "h"
    habit_list.append(Habit(habit_name, habit_points, habit_type))
    print(f"\nThe habit '{habit_name}', worth '{habit_points}' points, with the '{get_type_str(habit_type)}' type has been added.\n")
    return