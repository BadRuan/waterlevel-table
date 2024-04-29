import asyncio
from dao.waterlevel import (
    today8_waterlevel,
    yesterday8_waterlevel,
    lastweek8_waterlevel,
)

from config.settings import STATIONS
import csv


async def main():
    today8 = await today8_waterlevel()
    print("成功获取今天 8:00 水位数据")
    yesterday_8 = await yesterday8_waterlevel()
    print("成功获取昨天 8:00 水位数据")
    lastweek8 = await lastweek8_waterlevel()
    print("成功获取上周 8:00 水位数据")
    for station in STATIONS:
        for today in today8:
            if station.stcd == today.stcd:
                station.today_8 = today.current
        for yesterday in yesterday_8:
            if station.stcd == yesterday.stcd:
                station.yesterday_8 = yesterday.current
        for lastweek in lastweek8:
            if station.stcd == lastweek.stcd:
                station.lastweek_8 = lastweek.current

    filename = "今天、昨天、上周8点水位.csv"
    with open(filename, "w", encoding="utf-8") as file:
        csv_write = csv.writer(file)
        for station in STATIONS:
            csv_write.writerow(
                (station.today_8, station.yesterday_8, station.lastweek_8)
            )


if __name__ == "__main__":
    asyncio.run(main())
