for i in range(1, 21):
    print(i)

numbers = list(range(1, 1000001))
for number in numbers:
    print(number)

numbers = list(range(1, 1000001))
print("Min:", min(numbers))  # 1
print("Max:", max(numbers))  # 1000000
print("Sum:", sum(numbers))  # 500000500000

odd_numbers = list(range(1, 21, 2))
for number in odd_numbers:
    print(number)

multiples_of_three = list(range(3, 31, 3))
for number in multiples_of_three:
    print(number)

cubes = []
for i in range(1, 11):
    cubes.append(i ** 3)
for cube in cubes:
    print(cube)

cubes = [i ** 3 for i in range(1, 11)]
print(cubes)