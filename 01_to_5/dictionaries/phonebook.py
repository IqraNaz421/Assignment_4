def main():
    phonebook = {}

    while True:
        name = input("Name (or Enter to stop): ")
        if not name:
            break
        phonebook[name] = input("Number: ")

    for name, number in phonebook.items():
        print(f"{name} -> {number}")

    while True:
        lookup = input("\nLookup name (or Enter to stop): ")
        if not lookup:
            break
        print(phonebook.get(lookup, f"{lookup} not found."))

if __name__ == '__main__':
    main()
