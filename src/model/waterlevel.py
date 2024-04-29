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
    today_8: Optional[float] = 0
    yesterday_8: Optional[float] = 0
    lastweek_8: Optional[float] = 0
