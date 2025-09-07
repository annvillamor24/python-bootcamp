# TODO: Add more country codes
country_codes = {
    "PH": "Philippines",
    "US": "United States",
    "CA": "Canada",
    "UK": "United Kingdom",
    "JP": "Japan",
}

# TODO: Print the country for the given country code

# TODO: # If the key is not found, print Unknown
while True: #  if you don't want to end
    country_code = input("Enter country code: ")
    if country_code in country_codes:
        print(country_codes[country_code])
        break

# TODO: Print all codes
print(country_codes.keys())

print(country_codes.items())

# TODO: Print all countries
print(country_codes[country_code])
print(country_codes.values())