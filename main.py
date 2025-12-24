import io

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serialized_car = CarSerializer(car)
    return JSONRenderer().render(serialized_car.data)


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serialized_car = CarSerializer(data=data)
    serialized_car.is_valid(raise_exception=True)
    return serialized_car.save()
