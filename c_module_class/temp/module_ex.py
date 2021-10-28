import fah_converter as fah
print ("Enter a celsius value: ")
celsius = float(input()) # celsius = 100
fahrenheit = fah.covert_c_to_f(celsius) #fahrenheit = 212.0
print ("That's ", fahrenheit, " degrees Fahrenheit")
