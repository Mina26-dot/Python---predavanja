from users import Users

def main():
    users = Users("users")

    # users.insert("Marija", "Arsenijevic", 20)
    # users.fetch_all()
    # users.update("Ivana", "Ivic", 56, 20)
    # users.fetch_all()
    # users.delete(2)
    users.fetch_all()

if __name__ == "__main__":
    main()