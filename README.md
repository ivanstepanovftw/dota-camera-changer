# linux-dota-camchanger
Changes fixed camera distance in Dota 2 (before launch).

## Download
### Do not download with sudo!
```bash
git clone https://github.com/AshFTW/linux-dota-camchanger.git
cd ./linux-dota-camchanger
```

## Installing
Required Python 3.x
```bash
sudo apt-get install python3
```

Move `camchanger.py` in place with `libclient.so`:
```bash
cp ./camchanger.py ~/.steam/steam/steamapps/common/dota\ 2\ beta/game/dota/bin/linuxsteamrt64/camchanger.py
```

Make bash script at your home folder:
```bash
echo "cd ~/.steam/steam/steamapps/common/dota\ 2\ beta/game/dota/bin/linuxsteamrt64/ && python3 camchanger.py && chmod +rwx libclient.so" >> dotacamchanger.sh
chmod +x dotacamchanger.sh
```

## Launching
If you made bash script, you can easily just launch terminal (<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>) after each dota 2 update, type `./dota`, press <kbd>Tab</kbd> (you will see `./dotacamchanger `) and hit <kbd>Enter</kbd>(<kbd>Return</kbd>).


## Output example
I am prefer `1666` distance with `16:9` monitor.
```
Would you like to backup "libclient.so"? [Y/n]: 
Enter pitch max [current="1666", default="1134"]: 1234
Replacing " dota_camera_pitch_max 1666" to " dota_camera_pitch_max 1234".
Done!
```
