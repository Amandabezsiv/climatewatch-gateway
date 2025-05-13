def check_alerts(forecast: list) -> list:
    alerts = []

    for hour in forecast[:6]:  # Example: only the next 6 hours
        if hour["precipitation_probability"] > 70:
            alerts.append("High probability of rain in the next few hours.")
        if hour["temperature_2m"] > 30:
            alerts.append("Very high temperature.")
        if hour["visibility"] < 1000:
            alerts.append("Low visibility.")
        if hour["relative_humidity_2m"] > 90:
            alerts.append("Relative humidity above 90%.")

    return list(set(alerts))  # Remover duplicatas
