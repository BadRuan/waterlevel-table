from typing import List
from config.settings import STATIONS
from datetime import datetime, timedelta
from model.waterlevel import WaterLevel
from util.tdengine import TDengineTool


async def select_waterlevel(sql: str) -> List[WaterLevel]:
    with TDengineTool() as td:
        result = td.query(sql)
        return [
            WaterLevel(
                tm=row[0][:-7],
                current=row[1],
                stcd=row[2],
                name=row[3],
            )
            for row in result
        ]

# 查询今天8点水位
async def today8_waterlevel() -> List[WaterLevel]:
    date_now = datetime.now()
    SQL = f"SELECT `ts`, `current`, `stcd`, `name` FROM waterlevel WHERE `ts`='{date_now.strftime("%Y-%m-%d")} 08:00:00'"
    return await select_waterlevel(SQL)

# 查询昨天8点水位
async def yesterday8_waterlevel() -> List[WaterLevel]:
    yesterday = datetime.now() - timedelta(days=1)
    SQL = f"SELECT `ts`, `current`, `stcd`, `name` FROM waterlevel WHERE `ts`='{yesterday.strftime("%Y-%m-%d")} 08:00:00'"
    return await select_waterlevel(SQL)

# 查询上周8点水位
async def lastweek8_waterlevel() -> List[WaterLevel]:
    one_week_ago = datetime.now() - timedelta(weeks=1)
    SQL = f"SELECT `ts`, `current`, `stcd`, `name` FROM waterlevel WHERE `ts`='{one_week_ago.strftime("%Y-%m-%d")} 08:00:00'"
    return await select_waterlevel(SQL)
