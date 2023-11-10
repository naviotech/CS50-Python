'''
The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters that “show nutrition 
information for the 20 most frequently consumed raw fruits … in the United States. Retail stores are 
welcome to download the posters, print, display and/or distribute them to consumers in close proximity 
to the relevant foods in the stores.”

In a file called nutrition.py, implement a program that prompts consumers users to input a fruit 
(case-insensitively) and then outputs the number of calories in one portion of that fruit, per the 
FDA’s poster for fruits, which is also available as text. Capitalization aside, assume that users 
will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any 
input that isn’t a fruit.
'''
my_fruit = [{"Fruit": "apple", "Calories": 130},{"Fruit": "Avocado", "Calories": 50},{"Fruit": "Banana", "Calories": 110},{"Fruit": "Cantaloupe", "Calories": 50}, {"Fruit": "Grapefruit", "Calories": 60},{"Fruit": "Grapes", "Calories": 90},{"Fruit": "Honeydew Melon", "Calories": 50}, {"Fruit": "Kiwifruit", "Calories": 90}, {"Fruit": "Lemon", "Calories": 15}, {"Fruit": "Lime", "Calories": 20}, {"Fruit": "Nectarine", "Calories": 60}, {"Fruit": "Orange", "Calories": 80}, {"Fruit": "Peach", "Calories": 60}, {"Fruit": "pear", "Calories": 100}, {"Fruit": "Pineapple", "Calories": 50}, {"Fruit": "Plums", "Calories": 70}, {"Fruit": "Strawberries", "Calories": 50}, {"Fruit": "Sweet Cherries", "Calories": 100}, {"Fruit": "Tangerine", "Calories": 50}, {"Fruit": "Watermelon", "Calories": 80}]

fruit = input("Item: ")

for item in my_fruit:
    if item["Fruit"] == fruit:
        print("Calories:" ,item["Calories"])
        break
    else:
        continue