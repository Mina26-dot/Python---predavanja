from methods import load_file, save_file, delete_file, empty_file

data = load_file("data/user.json")


print(data)

data.append({
    "name" : "Test"
})

save_file("data/user.json", data)

delete_file("data/test.json")

empty_file("data/user.json")