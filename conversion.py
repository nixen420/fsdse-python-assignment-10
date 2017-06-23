def convert(celsius_data):
    list1=[]
    for value in celsius_data:
        fahrenheit = (value * 1.8) + 32
        list1.append(fahrenheit)
    return list1
#convert(celsius_data)
