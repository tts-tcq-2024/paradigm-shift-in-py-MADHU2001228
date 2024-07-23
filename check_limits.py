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
    assert battery_Is_Ok(25, 70, 0.7) == True #  all parameters are within the normal range
    assert battery_Is_Ok(50, 70, 0.7) == False  # Temperature out of range (high)
    assert battery_Is_Ok(-1, 70, 0.7) == False  # Temperature out of range (low)
    assert battery_Is_Ok(25, 85, 0.7) == False  # SoC out of range (high)
    assert battery_Is_Ok(25, 10, 0.7) == False  # SoC out of range (low)
    assert battery_Is_Ok(25, 70, 0.9) == False  # Charge Rate out of range (high)
    assert battery_Is_Ok(50, 85, 0.7) == False  # Temperature and SoC out of range (high)
    assert battery_Is_Ok(-1, 10, 0.7) == False  # Temperature and SoC out of range (low)
    assert battery_Is_Ok(25, 85, 0.9) == False  # SoC and Charge Rate out of range (high)
    assert battery_Is_Ok(50, 70, 0.9) == False  # Temperature and Charge Rate out of range (high)
    assert battery_Is_Ok(-1, 70, 0.9) == False  # Temperature out of range (too low) and Charge Rate out of range (high)
    assert battery_Is_Ok(50, 85, 0.9) == False  # All parameters out of range (high)
    assert battery_Is_Ok(-1, 10, 0.9) == False  # All parameters out of range (low except Charge Rate)
    assert battery_Is_Ok(0, 20, 0.8) == True   # On the edge, should be valid
    assert battery_Is_Ok(45, 80, 0.8) == True  # On the edge, should be valid
    assert battery_Is_Ok(0, 19, 0.8) == False  # SOC just below the valid range
    assert battery_Is_Ok(45, 81, 0.8) == False # SOC just above the valid range
    assert battery_Is_Ok(0, 20, 0.81) == False # Charge rate just above the valid range

    print("All test cases passed!")


