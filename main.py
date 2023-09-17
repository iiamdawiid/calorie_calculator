import functions as f

# main
while True:

    obj = f.CalMacCalc()
    print("CALORIE + MACRO CALCULATOR".center(65, '-'))
    user_input = input("Look up existing item (E)\nAdd new item (A)\nDelete item (D)\nQuit (Q)\nEnter choice: ")
    user_input = user_input.upper()

    while user_input not in {'E', 'A', 'D', 'Q'}:
        print(">>> INVALID INPUT <<<")
        user_input = input("Enter 'E', 'A', 'D', or 'Q': ")
        user_input = user_input.upper()

    if user_input == 'E':
        print("CHOOSE A FOOD".center(65, '-'))
        obj.print_stored_items()
        target_item = input("Enter item name: ")
        obj.get_food_item(target_item)

    elif user_input == 'A':
        print("ADD ITEM".center(65, '-'))
        obj.add_food_item()

    elif user_input == 'D':
        # not finished
        print("DELETE ITEM".center(65, '-'))
        obj.print_stored_items()
        delete_target = input("Enter item to delete: ")
        while delete_target.isdigit():
            print(">>> INVALID INPUT <<<")
            delete_target = input("Enter item to delete: ")
        
        obj.delete_food_item(delete_target)

    else:
        break