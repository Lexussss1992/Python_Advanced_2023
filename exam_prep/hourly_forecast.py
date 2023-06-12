def forecast(*args):
    forecast_dict = {}
    result = []
    for city, forecast in args:
        forecast_dict[city] = forecast
    sorted_forecast_dict = sorted(forecast_dict.items(), key=lambda item: -len(item[1]))
    for key, value in sorted_forecast_dict:
        result.append(f'{key} - {value}')
    return result


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
