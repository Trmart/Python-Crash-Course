# 8-5. Cities: Write a function called describe_city() that accepts the name of 
# a city and its country. The function should print a simple sentence, such as 
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the 
# default country.

def describe_city(city_name, country_name = 'United States'):
    print(str(city_name).title() + " is a city in ".title() + country_name )
    
def main():
    describe_city(city_name='CDA')
    describe_city(city_name='Kona')
    describe_city(city_name='Tokyo',country_name='Japan')

if(__name__ == '__main__'):
    main()