import asyncio
from dao.waterlevel import select_threeline_waterlevel
import csv


async def main():
    results = await select_threeline_waterlevel()
    filename = "目标水位.csv"
    with open(filename, "w", encoding="utf-8") as file:
        csv_write = csv.writer(file)
        for station in results:
            csv_write.writerow((station.name, station.current))


if __name__ == "__main__":
    asyncio.run(main())
