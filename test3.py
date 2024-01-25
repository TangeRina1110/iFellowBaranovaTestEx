class BaseConverter:
    @staticmethod
    def convert (celsius, syst):
        if syst == 'kelvin':
            return celsius + 273.15
        elif syst == 'fahrenheit':
            return (celsius * 1.8) + 32
            
celsius = float(input("Еnter the temperature in celsius: "))
syst = input("Сonvert to kelvin or fahrenheit? ")
converter = BaseConverter().convert(celsius, syst)

print(converter, syst)
