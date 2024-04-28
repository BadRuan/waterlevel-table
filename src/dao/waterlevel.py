from typing import List
from config.settings import STATIONS
from model.waterlevel import WaterLevel, Station
from util.tdengine import TDengineTool


# 查询当前最新水位
async def select_cruuent_waterlevel() -> List[WaterLevel]:
    with TDengineTool() as td:
        SQL = "SELECT LAST_ROW(ts) as tm, `current`, `stcd`, `name` FROM waterlevel GROUP BY `stcd`"
        result = td.query(SQL)
        return [
            WaterLevel(
                tm=row[0][:-7],
                current=row[1],
                stcd=row[2],
                name=row[3],
            )
            for row in result
        ]


# 查询当前三线水位信息
async def select_threeline_waterlevel() -> List[Station]:
    cruuent_waterlevel_data = await select_cruuent_waterlevel()
    for station in STATIONS:
        for waterlevel in cruuent_waterlevel_data:
            if station.stcd == waterlevel.stcd:
                station.current = waterlevel.current
                station.station_name = waterlevel.name
    return STATIONS
