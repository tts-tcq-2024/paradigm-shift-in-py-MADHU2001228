from battery_warning_messages import check_warning

def is_within_range(value, min_value, max_value, parameter_name):
    if value < min_value or value > max_value:
        print(f"{parameter_name} out of range!")
        return False
    return True

def is_BatteryTemperature_Ok(temperature):
    max_temp = 45
    tolerance = 0.05 * max_temp
    check_warning(temperature, 0, max_temp, tolerance, "Temperature Approaching Low", "Temperature Approaching High", "Temperature")
    return is_within_range(temperature, 0, max_temp, "Temperature")

def is_BatterySoc_Ok(soc):
    max_soc = 80
    tolerance = 0.05 * max_soc
    check_warning(soc, 20, max_soc, tolerance, "Approaching discharge", "Approaching charge-peak", "State of Charge")
    return is_within_range(soc, 20, max_soc, "State of Charge")

def is_BatteryChargeRate_Ok(chargeRate):
    max_charge_rate = 0.8
    tolerance = 0.05 * max_charge_rate
    check_warning(chargeRate, 0, max_charge_rate, tolerance, "Charge Rate Approaching Low", "Charge Rate Approaching High", "Charge Rate")
    if chargeRate > max_charge_rate:
        print("Charge Rate out of range!")
        return False
    return True
