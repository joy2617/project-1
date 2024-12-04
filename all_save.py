


def save_all(contacts):
    with open("contacts.csv", "w") as fp:
        for name, details in contacts.items():
            line = f"Name= '{name}', Number= '{details['number']}', Email= '{details['Email']}', Address= '{details['address']}'\n"
            fp.write(line)




