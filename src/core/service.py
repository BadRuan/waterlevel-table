from typing import List
import csv
from core.model import Station
from core.dao import (
    today8_waterlevel,
    yesterday8_waterlevel,
    lastweek8_waterlevel,
    lastyear8_waterlevel,
)


# 获取目标水位
async def get_waterlevel(stations: List[Station]) -> List[Station]:
    today8 = await today8_waterlevel()
    yesterday_8 = await yesterday8_waterlevel()
    lastweek8 = await lastweek8_waterlevel()
    lastyear8 = await lastyear8_waterlevel()
    for station in stations:
        # 获取今天 8:00 水位
        for today in today8:
            if station.stcd == today.stcd:
                station.today_8 = today.current
        # 获取昨天 8:00 水位
        for yesterday in yesterday_8:
            if station.stcd == yesterday.stcd:
                station.yesterday_8 = yesterday.current
        # 获取上周 8:00 水位
        for lastweek in lastweek8:
            if station.stcd == lastweek.stcd:
                station.lastweek_8 = lastweek.current
        # 获取去年同期 8:00 水位
        for lastyear in lastyear8:
            if station.stcd == lastyear.stcd:
                station.lastyear_8 = lastyear.current
    return stations


# 保存为csv文件
def save_csv(file_name: str, stations: List[Station]):
    with open(file_name, "w", encoding="utf-8") as file:
        csv_write = csv.writer(file)
        for station in stations:
            csv_write.writerow(
                (
                    station.today_8,
                    station.yesterday_8,
                    station.lastweek_8,
                    station.lastyear_8,
                )
            )
