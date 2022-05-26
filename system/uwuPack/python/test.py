def get_cpu_temp():
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = tempFile.read()
    tempFile.close()
    return round(float(cpu_temp)/1000, 2)

    while True:
        print(cpu_temp)
        print("test")
get_cpu_temp()