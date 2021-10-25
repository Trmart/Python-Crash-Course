# 8-6. City Names: Write a function called city_country() that takes in the name 
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value 
# that’s returned.


def city_country(city_name,country_name):
    full_name = str(city_name + ", " + country_name).title()
    print(full_name)
def main():
    print("This program will take user inputted city name and country name. Then return the full name of a location".title())
    city_name = input("Please enter the name of a city: ".title())
    country_name = input("Please enter the name of a country ".title())
    city_country(city_name,country_name)
    city_country('tokyo','japan')
    city_country('paris','france')
if(__name__ == '__main__'):
    main()