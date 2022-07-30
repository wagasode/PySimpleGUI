from pathlib import Path
import csv

infile = "namelist.csv"
try:
    f = Path(infile).open(encoding="UTF-8")
    dataReader = csv.reader(f)
    for row in dataReader:
        for value in row:
            print(value)
except:
    print("失敗しました。")
