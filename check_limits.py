def isTemperatureOk(temperature):
    if temperature < 0 or temperature > 45:
        print("Temperature out of range!")
        return 0
    return 1

def isSocOk(soc):
    if soc < 20 or soc > 80:
        print("State of Charge out of range!")
        return 0
    return 1

def isChargeRateOk(chargeRate):
    if chargeRate > 0.8:
        print("Charge Rate out of range!")
        return 0
    return 1

def batteryIsOk(temperature, soc, chargeRate):
    return isTemperatureOk(temperature) and isSocOk(soc) and isChargeRateOk(chargeRate)

if __name__ == '__main__':
    assert batteryIsOk(25, 70, 0.7) == 1
    assert batteryIsOk(50, 85, 0) == 0

