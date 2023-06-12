def forecast(*args):
    forecast_dict = {}
    result = []
    for city, forecast in args:
        forecast_dict[city] = forecast
    sorted_forecast_dict = sorted(forecast_dict.items(), key=lambda x: (x[1] != 'Sunny', x[1] != 'Cloudy', x[1] != 'Rainy', x[0]))
    for key, value in sorted_forecast_dict:
        result.append(f'{key} - {value}')
    return '\n'.join(result)


# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))

# print(forecast(
#     ("Beijing", "Sunny"),
#     ("Hong Kong", "Rainy"),
#     ("Tokyo", "Sunny"),
#     ("Sofia", "Cloudy"),
#     ("Peru", "Sunny"),
#     ("Florence", "Cloudy"),
#     ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
