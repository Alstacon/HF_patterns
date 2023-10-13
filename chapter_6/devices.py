class DefaultDeviceFuncs:
    """
    Default device interface
    """

    def __init__(self):
        self.is_on: bool = False

    def on(self) -> None:
        self.is_on = True

    def off(self) -> None:
        self.is_on = False

    def __repr__(self):
        return self.__class__.__name__


class GarageLight(DefaultDeviceFuncs):
    def __init__(self) -> None:
        super().__init__()
        self.location = 'Garage'


class BedroomLight(DefaultDeviceFuncs):
    def __init__(self) -> None:
        super().__init__()
        self.location = 'Bedroom'


garage_light = GarageLight()
bedroom_light = BedroomLight()

