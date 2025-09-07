attendee_names = []

attendee_count = int(input("Attendee count: "))

# TODO: For every attendee expected:
# attendee_name = input("Attendee name: ")
# TODO: Add attendee_name to attendee_names

# TODO: Remove your name in attendees (if it’s there)

# TODO: Remove and print the late attendee (last attendee)
for count in range(attendee_count):
    attendee_name = input("Attendee name: ")
    attendee_names.append(attendee_name)
print(attendee_names)

remove_name = input("Remove name: ")
if remove_name in attendee_names:
    attendee_names.remove(remove_name)
print(remove_name)
print(attendee_names.pop(-1))               #remove last in the list
print(attendee_names)