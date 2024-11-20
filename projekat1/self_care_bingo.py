import random
import json
import os


with open("hobbies.json", "r") as file:
    hobbies = json.load(file)


if not os.path.exists("used_categories.json"):
    with open("used_categories.json", "w") as file:
        json.dump({"excluded_categories": []}, file)


with open("used_categories.json", "r") as file:
    data = json.load(file)
    excluded_categories = data["excluded_categories"]

def choose_hobby():
    available_categories = [category for category in hobbies if category not in excluded_categories]

    if not available_categories:
        print("No more categories left.")
        return

    selected_category = random.choice(available_categories)

    selected_hobby = random.choice(hobbies[selected_category])

    excluded_categories.append(selected_category)

    with open("used_categories.json", "w") as file:
        json.dump({"excluded_categories": excluded_categories}, file)

    print(f"Selected hobby: {selected_hobby} from category: {selected_category}")

choose_hobby()