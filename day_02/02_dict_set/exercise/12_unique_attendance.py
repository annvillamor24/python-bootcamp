attendee_names = set()

attendee_count = int(input("Attendee count: "))

# TODO: For every attendee expected:
# attendee_name = input("Attendee name: ")
# TODO: Add attendee_name to attendee_names

print(attendee_names)
for count in range(attendee_count):
    attendee_name = input("Attendee name: ")
    attendee_names.add(attendee_name)
    print(count)
print(attendee_names)

