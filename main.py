import sys

def f_conversion():
    f = input("Enter your temperature in Farenheit: ")
    f_int = int(f)

    celsius_conversion = ((f_int - 32) * 5) / 9
    c_round = round(celcius_conversion, 2)
    kelvin_conversion = f_int + 457.87

    print("Your temperature in Fahrenheit is: " + str(f))
    print("The conversion to Celsius is: " + str(c_round))
    print("The conversion to Kelvin is: " + str(kelvin_conversion))
    
    sys.exit()
    
def c_conversion():
    c = input("Enter your temperature in Celsius: ")
    c_int = int(c)
    
    farenheit_conversion = ((9 / 5) * c_int) + 32
    f_round = round(farenheit_conversion, 2)
    kelvin_conversion = c_int + 273
    
    print("Your temperature in Celsius is: " + c)
    print("Your temperature in Farenheit is: " + str(f_round))
    print("Your temperature in Kelvin is: " + str(kelvin_conversion))
    
    sys.exit()
    
def k_conversion():
    k = input("Enter your temperature in Kelvin: ")
    f_int = int(k)
    
    farenheit_conversion = k - 457.87
    celsius_conversion = k - 273
    
    print("Your temperature in Kelvin is: " + k)
    print("Your temperature in Farenheit is: " + str(farenheit_conversion))
    print("Your temperature in Celcius is: " + str(celsius_conversion))
    
    sys.exit()
    
def conversion_type():
    request_f = input("Is your known temperature in Farenheit? (Y/N): ")
    if request_f == "Y":
        f_conversion()
        
    request_c = input("Is your known temperature in Celsius? (Y/N): ")
    if request_c == "Y":
        c_conversion()
        
    request_k = input("Is your known temperature in Kelvin? (Y/N): ")
    if request_k == "Y":
        k_conversion()
    else:
        conversion_type()
        
conversion_type()
