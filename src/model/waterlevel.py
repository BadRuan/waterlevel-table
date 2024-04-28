from pydantic import BaseModel
from typing import Optional


class WaterLevel(BaseModel):
    tm: str
    current: float
    stcd: int
    name: str


# 三线水位参数格式
class Station(BaseModel):
    stcd: int
    name: str
    station_name: Optional[str] = ""
    current: Optional[float] = 0
