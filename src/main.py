import asyncio
from core.service import get_waterlevel, save_csv
from core.settings import STATIONS


async def main():
    stations = await get_waterlevel(STATIONS)
    filename = "今天、昨天、上周、去年同期8点水位.csv"
    save_csv(filename, stations)


if __name__ == "__main__":
    asyncio.run(main())
