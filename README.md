# wp_avto_bruteforcer
This tool can sort dirs and files for make wordlist for fuzzing.
Download copy of site -> sort -> fuzz -> profit



How to use:
For dirs
```
python3 found.py d WordPress
```

For files
```
python3 found.py f WordPress
```

Output
```
python3 found.py d WordPress
WordPress/
WordPress/.git/
WordPress/.git/hooks/
WordPress/.git/info/
WordPress/.git/logs/
WordPress/.git/logs/refs/heads/
WordPress/.git/logs/refs/remotes/origin/
WordPress/.git/objects/pack/
WordPress/.git/refs/heads/
...


python3 found.py f WordPress
WordPress/.git/HEAD
WordPress/.git/config
WordPress/.git/description
WordPress/.git/hooks/applypatch-msg.sample
WordPress/.git/hooks/commit-msg.sample
WordPress/.git/hooks/fsmonitor-watchman.sample
WordPress/.git/hooks/post-update.sample
...
```

