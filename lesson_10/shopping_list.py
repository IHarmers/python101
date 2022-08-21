import json
import sys
from enum import Enum

ROOT_NAME = "shopping_list"  # Root name used for the JSON structure


class Action(Enum):
    '''
    Represents the different things
    the user can do.
    '''
    ADD = 1
    DELETE = 2
    SAVE = 3
    QUIT = 4


def print_list(list):
    '''
    Print the contents of the current shopping list
    to the screen.
    '''
    if len(list) == 0:
        print("Your shopping list is empty")
    else:
        print("Shopping list:")
        counter = 1
        for item in list:
            print("{}. {} ({})".format(
                counter, item["name"], item["quantity"]))
            counter = counter + 1


def ask_for_action():
    '''
    Asks the user do something. It displays
    a options menu where the user must choose
    an action. The function will return an
    Action enum with the user choice.
    '''
    print("These are your options:")
    print("[1] Add an item")
    print("[2] Delete an item")
    print("[3] Save list")
    print("[4] Quit")
    answer = input("What would you like to do?:")
    action = Action(int(answer))
    return action


def load(path):
    '''
    Load a shipping list form the given file.
    '''
    global ROOT_NAME
    with open(path, 'r') as input_file:
        data = json.load(input_file)
        return data[ROOT_NAME]


def try_load(path):
    '''
    Try loading a shopping list form a given file.
    The function will return an empty list when
    the file doesn't exists.
    '''
    try:
        return load(path)
    except FileNotFoundError:
        return []


def save(path, shopping_list):
    '''
    Save the given shopping list to the
    given configuration file. The configuration
    file will be created if it does not exists.
    '''
    global ROOT_NAME
    data = {ROOT_NAME: shopping_list}
    with open(path, 'w') as out_file:
        json.dump(data, out_file, indent=4)


def main():
    '''
    Main function of the Shopping List program
    '''
    file_name = "shopping_list.json"
    try:
        shopping_list = try_load(file_name)
    except json.JSONDecodeError:
        print("Failed to load {}. The file contains an invalid JSON structure".format(
            file_name))
        sys.exit(1)

    while True:
        print_list(shopping_list)
        print("")

        try:
            action = ask_for_action()
        except ValueError:
            print("Error: Please provide a valid answer")
            continue

        if action is Action.ADD:
            name = input("Item name: ")
            if len(name) == 0:
                print("Error: The name cannot be empty")
            else:
                quantity_str = input("Quantity: ")
                try:
                    quantity = int(quantity_str)
                    shopping_list.append({"name": name, "quantity": quantity})
                except ValueError:
                    print("Error: Quantity must be a number")
        elif action is Action.DELETE:
            item_number_str = input(
                "What item number would you like to delete:")
            try:
                item_number = int(item_number_str)
                index = item_number - 1
                del shopping_list[index]
            except ValueError:
                print("Error: please supply a number")
            except IndexError:
                print("Error: no item with this number")
        elif action is Action.QUIT:
            print("Good bye!")
            sys.exit()
        elif action is Action.SAVE:
            print("Saving list...")
            try:
                save(file_name, shopping_list)
            except PermissionError:
                print("Error: no permission to create and write to save file")
                print("Shopping list has not been saved!")
            print("Shopping list saved as {}".format(file_name))


if __name__ == "__main__":
    main()
