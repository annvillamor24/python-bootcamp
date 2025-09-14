
    """
    Converts an integer into its English word representation.
    Example: 42 → "forty-two"

    Note: Only handle from 0 to 999,999
    """

ones = ["zero", "one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine"]

teens = ["ten", "eleven", "twelve", "thirteen", "fourteen",
         "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens = ["ten", "twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"]

parts = []

    hundreds = num // 100
    remainder = num % 100


def number_to_words(n: int) -> str:
