from chapter_2.interfaces import Observer, DisplayElement
from chapter_2.weather_station import WeatherStation


class CurrentConditionDisplay(Observer, DisplayElement):
    _temperature: float
    _humidity: float

    def __init__(self, weather_station: WeatherStation):
        self.weather_station = weather_station
        self.weather_station.register_observer(self)

    def update(self) -> None:
        self._temperature = self.weather_station.weather_data.temperature
        self._humidity = self.weather_station.weather_data.humidity
        self.display()

    def display(self) -> None:
        print(f'''
        Current conditions:
        temperature: {self._temperature}
        humidity: {self._humidity}.
        ''')


class StatisticDisplay(Observer, DisplayElement):

    def __init__(self, weather_station: WeatherStation):
        self._days_passed = 0
        self._min_temperature = float('inf')
        self._max_temperature = -float('inf')

        self.weather_station = weather_station
        self.weather_station.register_observer(self)

    def update(self):
        self._days_passed += 1

        self._max_temperature = max(self._max_temperature, self.weather_station.weather_data.temperature)
        self._min_temperature = min(self._min_temperature, self.weather_station.weather_data.temperature)

        self.display()

    def display(self):
        print(f'''
        Statistic for last {self._days_passed} days:
        Average temperature = {(self._min_temperature + self._max_temperature) / self._days_passed},
        Max temperature = {self._max_temperature},
        Min temperature = {self._min_temperature}.
        ''')


class ForecastDisplay(Observer, DisplayElement):
    def update(self):
        ...

    def display(self):
        ...


class ThirdPartyDisplay(Observer, DisplayElement):
    def update(self):
        ...

    def display(self):
        ...
