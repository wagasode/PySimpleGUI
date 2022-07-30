from pathlib import Path

infolder = "testfolder"
text = "*.txt"
filelist = []
for p in Path(infolder).rglob(text):
    filelist.append(str(p))
for filename in sorted(filelist):
    print(filename)
