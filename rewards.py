from enum import Enum

class RewardType(Enum):
    TREAT = 1
    VACATION = 2
    OTHER = 3

class Reward:
    def __init__(self, name, cost, type):
        self.name = name
        self.cost = cost
        self.type = type

def check_reward_type(type_str):
    if type_str == "1" or type_str == "treat":
        return RewardType.TREAT
    if type_str == "2" or type_str == "vacation":
        return RewardType.VACATION
    if type_str == "3" or type_str == "other":
        return RewardType.OTHER
    raise Exception

def get_type_str(type):
    match type:
        case RewardType.TREAT:
            return "treat"
        case RewardType.VACATION:
            return "vacation"
        case RewardType.OTHER:
            return "other"
        case _:
            return "Error: Reward Type Not Found"


def new_reward(name_list, reward_list, command_names):
    print("Creating a new reward, type 'cancel' to return.")
    reward_name = input("\nWhat is the rewards name?\n")
    reward_name = str.lower(reward_name)
    if reward_name == "cancel":
        return
    reward_cost_str = input("\nHow many points will it cost?\n")
    valid_cost = 1
    while valid_cost == 1:
        reward_cost_str = str.lower(reward_cost_str)
        if reward_cost_str == "cancel":
            return
        try:
            reward_cost = int(reward_cost_str)
            valid_cost = 0
        except Exception:
            reward_cost_str = input(f"{reward_cost_str} is not a valid whole number, please enter a valid value:\n")
    reward_type_valid = 1
    while reward_type_valid == 1:
        reward_type_str = input("\nWhat type of reward is it?\n1. Treat\n2. Vacation\n3. Other\n")
        reward_type_str = str.lower(reward_type_str)
        if reward_type_str == "cancel":
            return
        try:
            reward_type = check_reward_type(reward_type_str)
            reward_type_valid = 0
        except Exception:
            print(f"{reward_type_str} is not a valid reward type.\nPlease enter the number or name of the reward type.\n")
    existing_name = 1
    while existing_name == 1:
        if reward_name in command_names:
            reward_name = input(f"\n{reward_name} is already the name of a command, please enter a new name:\n")
            reward_name = str.lower(reward_name)
            if reward_name == "cancel":
                return
        elif reward_name in name_list:
            reward_name = input(f"\n{reward_name} is already the name of an existing habit or reward, please enter a new name:\n")
            reward_name = str.lower(reward_name)
            if reward_name == "cancel":
                return
        else:
            existing_name = 0
    name_list.append(reward_name)
    reward_list.append(Reward(reward_name, reward_cost, reward_type))
    print(f"\nThe reward '{reward_name}', costing '{reward_cost}' points, with the '{get_type_str(reward_type)}' type has been added.\n")
    return