from typing import Union


print('my_project')
print('new line!!!')
def some_function(number: Union[int, float]) -> None:
    pass

import requests
from dataclasses import dataclass, field


@dataclass
class Coordinates:
    latitude: float
    longitude: float

@dataclass
class IssRequest:
    message: str
    iss_position: field(default_factory = dict)
    timestamp: int

    def __post_init__(self):
        self.iss_position = Coordinates(*self.iss_position.values())



api_url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(api_url)
result = response.json()
if response.status_code == 200:
    iss = IssRequest(*result.values())
    print(iss.iss_position.longitude)
else:
    print(response.status_code)