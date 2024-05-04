from pathlib import Path
from asyncio import run
from datetime import datetime
from core.service import get_waterlevel, save_xlsx


async def main():
    current_file_path = Path(__file__).resolve()
    current_dir = current_file_path.parent
    file_path = current_dir / "基础表格.xlsx"
    source_filename = str(file_path)
    print("读取路径: ", source_filename)
    
    savefilename = f"{datetime.now().strftime("%Y年%m月%d日_鸠江区三线水位测站记录表")}.xlsx"
    save_path = current_dir.parent / savefilename
    target_filename = str(save_path)
    print("保存路径: ", target_filename)

    stations = await get_waterlevel()
    await save_xlsx(source_filename, target_filename, stations)


if __name__ == "__main__":
    run(main())
