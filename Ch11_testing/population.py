# 11-2. Population: Modify your function so it requires a third parameter, 
# population. It should now return a single string of the form City, Country – 
# population xxx, such as Santiago, Chile – population 5000000. Run 
# test_cities.py again. Make sure test_city_country() fails this time.
# Modify the function so the population parameter is optional. Run 
# test_cities.py again, and make sure test_city_country() passes again.
# Write a second test called test_city_country_population() that verifies 
# you can call your function with the values 'santiago', 'chile', and 
# 'population=5000000'. Run test_cities.py again, and make sure this new test 
# passes.

def city_country(city_name,country_name,population=''):
    """Function takes city, country name, and optional pop
        returning them in one formatted string"""
    if(population):
        city_country = str(city_name + "," + country_name + ' population:' + population)
    else:
        city_country = str(city_name + "," + country_name)
    return city_country.title()
