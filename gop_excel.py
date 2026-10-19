
from pathlib import Path
import pandas as pd

print("=== CONG CU GOP FILE EXCEL ===")

folder = input("Nhap duong dan thu muc chua cac file Excel: ").strip().strip('"')
folder_path = Path(folder)

if not folder_path.is_dir():
    print("Loi: Thu muc khong ton tai.")
else:
    files = [
        f for f in folder_path.glob("*.xlsx")
        if not f.name.startswith("~$")
        and f.name != "Ket_qua_gop.xlsx"
    ]

    if not files:
        print("Khong tim thay file Excel .xlsx trong thu muc.")
    else:
        tables = []

        for file in files:
            try:
                df = pd.read_excel(file)
                tables.append(df)
                print(f"Da doc: {file.name}")
            except Exception as e:
                print(f"Khong doc duoc {file.name}: {e}")

        if tables:
            result = pd.concat(tables, ignore_index=True)
            result = result.drop_duplicates()

            output = folder_path / "Ket_qua_gop.xlsx"
            result.to_excel(output, index=False)

            print(f"\nDa gop xong {len(tables)} file.")
            print(f"So dong ket qua: {len(result)}")
            print(f"File ket qua: {output}")

input("\nNhan Enter de dong chuong trinh...")
