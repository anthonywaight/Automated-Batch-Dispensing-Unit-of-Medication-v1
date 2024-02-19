
def get_cpu_temperature():
    try:
        #open file containing CPU temp
        with open("/sys/class/thermal/thermal_zone0/temp","r") as file:
            #read temp value (in millidegres celsius)
            temp_str=file.readline().strip()
            #convert temp to deg celsius
            temp_celsius = int(temp_str) / 1000.0
            return temp_celsius
    except IOError as e:
        print(f'Error reading CPU temperature: {e}')
        return None
