from pathlib import Path
import csv

infile = "namelist.csv"
f = Path(infile).open(encoding="UTF-8")
dataReader = csv.reader(f)
for row in dataReader:
    for value in row:
        print(value)
