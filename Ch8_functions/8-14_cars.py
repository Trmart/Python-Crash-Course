# 8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It 
# should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a 
# color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was 
# stored correctly.

def make_car(manufacturer_name,model_name, **user_input):
    car_info = {}
    car_info['manufacturer'] = manufacturer_name
    car_info['model'] = model_name
    for key, val in user_input.items():
        car_info[key] = val
    return car_info

def main():
    car = make_car('subaru','outback', color = 'blue', tow_package = 'available')
    for key, val in car.items():
        print(str(key +':' +val).title())

if(__name__ == '__main__'):
    main()