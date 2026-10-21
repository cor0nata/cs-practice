from pathlib import Path
from tablestats import read_rows, count_types, total_minutes, to_csv
def main():
    filename = input().strip()
    table_path = Path(filename)
    with table_path.open(encoding="utf-8") as table:
        rows = read_rows(table)
    counts = count_types(rows)
    print(len(rows))
    print(len(counts))
    print(f"{total_minutes(rows, 'ошибка'):.1f}")
    summary_path = Path(__file__).resolve().parent / "summary.csv"
    with summary_path.open("w", encoding="utf-8", newline="") as out:
        out.write(to_csv(counts))
if __name__ == "__main__":
    main()
