from pathlib import Path

filepath = "test1.txt"
p = Path(filepath)
print(f"ファイルパス　　　 = {str(p)}")
print(f"ファイル名　　　　 = {p.name}")
print(f"ファイル拡張子　　 = {p.suffix}")
print(f"ファイル拡張子以外 = {p.stem}")
print(f"フォルダ名　　　　 = {p.parent.name}")
print(f"ファイルサイズ　　 = {str(p.stat().st_size)}バイト")
