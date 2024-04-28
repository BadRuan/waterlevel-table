import asyncio
from dao.waterlevel import today8_waterlevel, lastweek8_waterlevel

from config.settings import STATIONS
import csv


async def main():
    today8 = await today8_waterlevel()
    lastweek8 = await lastweek8_waterlevel()
    for station in STATIONS:
        for today in today8:
            if station.stcd == today.stcd:
                station.today_8 = today.current
        for lastweek in lastweek8:
            if station.stcd == lastweek.stcd:
                station.lastweek_8 = lastweek.current

    filename = "目标水位.csv"
    with open(filename, "w", encoding="utf-8") as file:
        csv_write = csv.writer(file)
        for station in STATIONS:
            csv_write.writerow((station.today_8, station.lastweek_8))


if __name__ == "__main__":
    asyncio.run(main())
