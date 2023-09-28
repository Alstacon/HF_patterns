from chapter_2.displays import CurrentConditionDisplay, StatisticDisplay
from chapter_2.weather_station import WeatherStation


def run_weather_station() -> None:
    weather_station = WeatherStation()
    CurrentConditionDisplay(weather_station)
    StatisticDisplay(weather_station)

    weather_station.measurements_changed(78, 70, 34.1)
    weather_station.measurements_changed(90, 70, 30.1)


if __name__ == '__main__':
    run_weather_station()
