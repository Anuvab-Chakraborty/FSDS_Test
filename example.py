import os
from pathlib import Path

path = "dir1/dir2/dir3"
print(path)
path = os.path.join("dir1", "dir2", "dir3")
print(type(path))
path = Path(f"dir1/dir2/dir3/{path}")
print(type(path))
[1 0 0
1 1 1]