def calculate_health(customer):
    usage = customer["usage"]
    failures = customer["failures"]

    score = usage - (failures * 10)

    if score >= 70:
        return "Healthy"
    elif score >= 40:
        return "Medium"
    else:
        return "Risky"
