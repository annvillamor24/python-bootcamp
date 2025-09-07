attendee_names = []

attendee_count = int(input("Attendee count: "))

# TODO: For every attendee expected:
attendee_name = input("Attendee name: ")
# TODO: Add attendee_name to attendee_names

# TODO: Remove your name in attendees (if it’s there)
remove_name = input("Remove name: ")
if remove_name in attendee_names:
    attendee_names.remove(remove_name)
print(attendee_names)
print(remove_name)
