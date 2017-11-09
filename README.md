### **renaming_tool.py** ##

- useful for renaming many files and/or folders
- risk of wheel-re-invention

```bash

$ python3 renaming_tool.py -h
usage: renaming_tool.py [-h] [--files] [--folders] -p path [-d depth] [-l] [-U] [-r old new]

renaming multiple folders and/or files at once

optional arguments:
  -h, --help  show this help message and exit
  --files     run for files
  --folders   run for folders
  -p path     root path (required)
  -d depth    specify the depth to traverse, default is 0
  -l          makes all characters lowercase
  -U          makes all characters uppercase
  -r old new  replaces substring old with new

phase 1: preview changes
phase 2: make changes

```
### **sleep.py**

``` bash
python sleep.py -h
usage: sleep.py [-h] [-m minutes] [-s mseconds]

puts computer to sleep

optional arguments:
  -h, --help   show this help message and exit
  -m minutes   type how many minutes to wait before sleep
  -s mseconds  type how many seconds to wait before sleep
```

----------
