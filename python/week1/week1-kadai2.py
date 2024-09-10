def output(names):
    for name in names:
        print(f"dear {name}, I would like to invite you to a dinner party at my house. Please let me know if you can make it.")


guests = ["Maine", "Lucy", "Rebecca"]

unavailable_guests = "Maine"

print(f"Unfortunately, {unavailable_guests} can't make it to the dinner party.")

new_guests = "David"

guests[guests.index(unavailable_guests)] = new_guests

output(guests)
