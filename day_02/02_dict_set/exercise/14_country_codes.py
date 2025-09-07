# TODO: Add more country codes
country_codes = {
    "PH": "Philippines",
    "US": "United States",
    "CA": "Canada",
    "UK": "United Kingdom",
    "JP": "Japan",
}
while True: #  if you don't want to end
    country_code = input("Enter country code: ")
    if country_code in country_codes:
        print(country_codes[country_code])
country_code = input("Please enter country codes: ")
print(f"country_codes: {country_codes[country_code]}")
