def output(names):
    for name in names:
        print(f"dear {name}, I would like to invite you to a dinner party at my house. Please let me know if you can make it.")


guests = ["Maine", "Lucy", "Rebecca"]

unavailable_guests = "Maine"

print(f"Unfortunately, {unavailable_guests} can't make it to the dinner party.")

new_guests = "David"

guests[guests.index(unavailable_guests)] = new_guests

output(guests)

print("I found a bigger table, so I can invite more people.")

guests.insert(0, "Pilar")

mid = len(guests) // 2
guests.insert(mid, "Falco")

guests.append("Gloria")

output(guests)

print("Unfortunately, due to shortage of ingredients, I can only invite two people to the dinner party.")

while len(guests) > 2:
    print(f"Dear {guests.pop()}, I'm sorry to inform you that I can no longer invite you to the dinner party.")

for guest in guests:
    print(f"Dear {guest}, you are still invited to the dinner party. Please let me know if you can make it.")

del guests[:]
print(guests)
