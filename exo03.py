#resolution avec une fonction conv_temp
def conv_temp(celsius):
    fahrenheit=(celsius* 9/5) + 32
    return str(fahrenheit) + ' F'

#resolution sans fonction 
celsius = int(input("Entrez la temperature"))
fahrenheit = (celsius * 9/5) + 32
print(str(fahrenheit) + ' F')