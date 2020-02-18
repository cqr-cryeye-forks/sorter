# sorter
This tool can sort dirs and files for make wordlist for fuzzing.

Download copy of site -> sort -> fuzz -> profit


How to use:

For dirs
```
python3 sort.py d WordPress/
```

For files
```
python3 sort.py f WordPress/
```

Output
```
python3 found.py d WordPress/
.git/
.git/hooks/
.git/info/
.git/logs/
.git/logs/refs/heads/
.git/logs/refs/remotes/origin/
.git/objects/pack/
.git/refs/heads/
...


python3 found.py f WordPress/
.git/HEAD
.git/config
.git/description
.git/hooks/applypatch-msg.sample
.git/hooks/commit-msg.sample
.git/hooks/fsmonitor-watchman.sample
.git/hooks/post-update.sample
...
```

