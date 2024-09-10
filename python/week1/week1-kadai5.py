places = ["Maldives", "Bali", "Great Barrier Reef", "Hawaii", "Amalfi Coast"]

print("Original List:", places)

print("Sorted List:", sorted(places))

print("Reversed List:", sorted(places, reverse=True))

places.reverse()
print("Reversed List:", places)

places.reverse()
print("List restored to original order:", places)

places.sort()
print("List sorted alphabetically:", places)

places.sort(reverse=True)
print("List sorted reverse alphabetically:", places)
