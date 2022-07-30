from pathlib import Path

infolder = "testfolder"
value1 = "*.txt"

#【関数：　ファイルリストを作成する】
def listfiles(infolder, ext):
    msg = ""
    filelist = []
    for p in Path(infolder).rglob(ext):
        filelist.append(str(p))
    for filename in sorted(filelist):
        msg += f"{filename}\n"
    msg = f"ファイル数 = {str(len(filelist))}\n{msg}"
    return msg

#【関数を実行】
msg = listfiles(infolder, value1)
print(msg)
