# this program will ask the user if they would like to store a new food item or look up an existing one
# if user adds new food item then store the serving size in grams, calories per serving, protein, fat, carbs in a file
# is user wants to look up existing food item then search for it in file and make the proper calculations for calories
# protein, fats, carbs for the amount of food in grams the user entered

# TO-DO: 

class CalMacCalc():

    def __init__(self):
        pass

    def add_food_item(self):
        # write info to file so it can be accessed later and used to calculate macros 
        self.item_name = input("Name of Item: ")
        self.serving_size = input("Serving Size (grams): ")
        self.calories = input("Amount of Calories: ")
        self.protein = input("Amount of Protein: ")
        self.fats = input("Amount of Fat: ")
        self.carbs = input("Amount of Carbs: ")
        print("".center(65, '-'))
        
        item_present = False
        with open("food_items.txt", "r") as file:
            for line in file:
                elements = line.strip().split(",")
                if self.item_name == elements[0]:
                    item_present = True
                    break

        if item_present:
            print(">>> ITEM ALREADY ADDED <<<\n")
        else:
            with open("food_items.txt", "a") as file:
                new_entry = f"\n{self.item_name},{self.serving_size},{self.calories},{self.protein},{self.fats},{self.carbs}"
                file.write(new_entry)


    def delete_food_item(self, target):
        # delete's unwanted items 
        lines_to_keep = []
        found = False
        with open("food_items.txt", "r") as file:
            for line in file:
                elements = line.strip().split(",")
                if elements[0].lower() != target.lower():
                    lines_to_keep.append(line)
                else:
                    found = True

        if found:
            permission = input(f"Are you sure you want to delete - {target.upper()} ? (Y/N): ")
            permission = permission.upper()
            while permission not in {'Y', 'N'}:
                print(">>> INVALID INPUT <<<")
                permission = input("Enter 'Y' or 'N': ")
                permission = permission.upper()

            if permission == 'Y':
                with open("food_items.txt", "w") as file:
                    file.writelines(lines_to_keep)
                print(f">>> {target.upper()} has been Deleted <<<\n")
            else:
                print(">>> Delete CANCELED <<<\n")


    def get_food_item(self, target_item):
        found = False
        with open("food_items.txt", "r") as file:
            for line in file:
                elements = line.strip().split(",")
                food_item = elements[0]

                if target_item.lower() in food_item.lower():
                    found = True
                    nutrition = {
                        "Item Name": food_item,
                        "Serving Size": elements[1],
                        "Calories": elements[2],
                        "Protein": elements[3],
                        "Fats": elements[4],
                        "Carbs": elements[5]
                    }
                    self.calculate_macros(nutrition)
                    break
        
        if not found:
            print(">>> ITEM NOT FOUND <<<")
       

    def calculate_macros(self, nutrition):
        # retrieves values from text file and calculate proper macros based on grams user entered of said food
        self.user_serving = input("Enter amount of grams: ")
        while self.user_serving.isalpha():
            print(">>> INVALID INPUT <<<")
            self.user_serving = input("Enter a number: ")
        self.user_serving = int(self.user_serving)
        # with open("food_items.txt", "r") as file:
        #     for line in file:
        #         elements = line.strip().split(",")
        
        calories_per_gram = float(nutrition["Calories"]) / float(nutrition["Serving Size"])
        protein_per_gram = float(nutrition["Protein"]) / float(nutrition["Serving Size"])
        fat_per_gram = float(nutrition["Fats"]) / float(nutrition["Serving Size"])
        carbs_per_gram = float(nutrition["Carbs"]) / float(nutrition["Serving Size"])

        self.calc_calories = calories_per_gram * self.user_serving
        self.calc_protein = protein_per_gram * self.user_serving
        self.calc_fat = fat_per_gram * self.user_serving
        self.calc_carbs = carbs_per_gram * self.user_serving

        self.print_macros(nutrition)


    def print_macros(self, nutrition):
        print("")
        print(f"MACROS FOR {self.user_serving}g of {nutrition['Item Name'].upper()}".center(65, '-'))
        print(f"CALORIES: {round(self.calc_calories)}")
        print(f"PROTEIN: {round(self.calc_protein)}g")
        print(f"FATS: {round(self.calc_fat)}g")
        print(f"CARBS: {round(self.calc_carbs)}g")
        print("".center(65, '-'))


    def print_stored_items(self):
        with open("food_items.txt", "r") as file:
            for line in file:
                elements = line.strip().split(",")
                print(elements[0].title())
            print("")