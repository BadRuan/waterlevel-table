from typing import List
from core.model import Database, Station


DATABASE_DEV = Database(
    url="127.0.0.1", port=6041, user="root", password="123456", database="water"
)


STATIONS: List[Station] = [
    Station(stcd=62904500, name="无为大堤"),
    Station(stcd=60115400, name="城北圩"),
    Station(stcd=62900700, name="江北（沈巷）长江堤"),
    Station(stcd=62906500, name="万春圈堤"),
    Station(stcd=62900700, name="裕溪口江堤"),
    Station(stcd=62900600, name="裕溪河堤"),
    Station(stcd=62905100, name="牛屯河堤"),
    Station(stcd=62904500, name="惠生连圩堤"),
    Station(stcd=62904500, name="永定大圩堤"),
    Station(stcd=62904500, name="黑沙洲、天然洲圩"),
]
