from pathlib import Path

infile = "test.txt"
try:
    p = Path(infile)
    text = p.read_text(encoding="UTF-8")
    print(text)
except:
    print("失敗しました。")
