def count_vowels(string: str) -> int:
    """Return the number of vowels in the given string"""

    return sum(1 for char in string if char in "aeiouAEIOU")


print(count_vowels("welcome to programming"))


