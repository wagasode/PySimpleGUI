from pathlib import Path

infolder = "testfolder"
value1 = "test"

#【関数：　フォルダ内のファイル名で検索文字が含まれているものがあるかを調べる】
def findfilename(infolder, findword):
    cnt = 0
    msg = ""
    filelist = []
    for p in Path(infolder).rglob("*.*"):
        if p.name[0] != ".":
            filelist.append(str(p))
    for filename in sorted(filelist):
        if filename.count(findword) > 0:
            msg += f"{filename}\n"
            cnt += 1
    msg = f"ファイル数 = {str(cnt)}\n{msg}"
    return msg

#【関数を実行】
msg = findfilename(infolder, value1)
print(msg)
