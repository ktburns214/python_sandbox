# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
people = ["John", "Paul", "George", "Ringo"]

# simple for loop
for person in people:
    print(f"Current person: {person}")

# break--stops the loop
for person in people:
    if person == "Paul":
        break
    print(f"Current person: {person}")

# continue--skips the value
for person in people:
    if person == "Paul":
        continue
    print(f"Current person: {person}")

# range--prints each value
for i in range(len(people)):
    print(people[i])

for i in range (0, 11):
    print(f"number: {i}")


# While loops execute a set of statements as long as a condition is true.
count = 0
while count <= 10:
    print(f"count: {count}")
    count += 1