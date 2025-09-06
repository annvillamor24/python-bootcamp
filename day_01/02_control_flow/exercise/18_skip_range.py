from unittest import skipIf

for item in range(100):
    # TODO: Change code to skip printing numbers 20 to 80.
    print(item)
for item in range(100):
    if 20<item<80: continue
    print(item)