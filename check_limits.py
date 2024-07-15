def is_BatteryTemperature_Ok(temperature):
    if temperature < 0 or temperature > 45:
        print("Temperature out of range!")
        return False
    return True

def is_BatterySoc_Ok(soc): #state of charge
    if soc < 20 or soc > 80:
        print("State of Charge out of range!")
        return False
    return True

def is_BatteryChargeRate_Ok(chargeRate):
    if chargeRate > 0.8:
        print("Charge Rate out of range!")
        return False
    return True

def battery_Is_Ok(temperature, soc, chargeRate):
    return is_BatteryTemperature_Ok(temperature) and is_BatterySoc_Ok(soc) and is_BatteryChargeRate_Ok(chargeRate)

if __name__ == '__main__':
    assert battery_Is_Ok(25, 70, 0.7) == True
    assert battery_Is_Ok(50, 85, 0) == False

