from pathlib import Path
import csv

infile = "namelist.csv"
value1 = "outputfolder"

#【関数：　CSVからフォルダを作成する】
def makefolders(readfile, savefolder):
    msg = ""
    Path(savefolder).mkdir(exist_ok=True)
    f = Path(infile).open(encoding="UTF-8")
    csvdata = csv.reader(f)
    for row in csvdata:
        for foldername in row:
            newfolder = Path(savefolder).joinpath(foldername)
            newfolder.mkdir(exist_ok=True)
            msg += f"{savefolder}に{foldername}を作成しました。\n"
    return msg

#【関数を実行】
msg = makefolders(infile, value1)
print(msg)
