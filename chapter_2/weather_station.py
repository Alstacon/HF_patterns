from chapter_2.interfaces import Subject, Observer


class WeatherData:
    _temperature: float
    _humidity: float
    _pressure: float

    @property
    def temperature(self) -> float:
        return self._temperature

    @temperature.setter
    def temperature(self, value: float) -> None:
        self._temperature = value

    @property
    def humidity(self) -> float:
        return self._humidity

    @humidity.setter
    def humidity(self, value: float) -> None:
        self._humidity = value

    @property
    def pressure(self) -> float:
        return self._pressure

    @pressure.setter
    def pressure(self, value: float) -> None:
        self._pressure = value


class WeatherStation(Subject):
    def __init__(self):
        self.observers = []
        self.weather_data = WeatherData()

    def register_observer(self, observer: Observer) -> None:
        self.observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def notify(self) -> None:
        for observer in self.observers:
            observer.update()

    def measurements_changed(self, temperature: float, humidity: float, pressure: float) -> None:
        self.weather_data.temperature = temperature
        self.weather_data.humidity = humidity
        self.weather_data.pressure = pressure
        self.notify()
