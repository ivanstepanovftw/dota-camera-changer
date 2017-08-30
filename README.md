# linux-dota-camchanger
Changes camera distance in Dota 2.

## Download
```bash
git clone https://github.com/AshFTW/linux-dota-camchanger.git
cd ./linux-dota-camchanger
```

## Installing
Required Python 3.x
```bash
sudo apt-get install python3
```

Move `camchanger.py` to `libclient.so` location:
```bash
cp ./camchanger.py ~/.steam/steam/steamapps/common/dota\ 2\ beta/game/dota/bin/linuxsteamrt64/camchanger.py
```

Make bash script at your home folder:
```bash
echo "cd ~/.steam/steam/steamapps/common/dota\ 2\ beta/game/dota/bin/linuxsteamrt64/ && python3 camchanger.py" >> camchanger.sh
chmod +x camchanger.sh
```

Or make symbolic link of `linuxsteamrt64` folder:
```bash
ln -s ~/.steam/steam/steamapps/common/dota\ 2\ beta/game/dota/bin/linuxsteamrt64/ ~/linuxsteamrt64
```

## Launching
If you made `.sh` file, you can easily just launch terminal after each dota 2 update, type `./cam`, press <kbd>TAB</kbd> (you will see `./camchanger `) and hit <kbd>ENTER</kbd>.
<br>If you made link:
```bash
cd linuxsteamrt64
python3 camchanger.py
```

## Output example
I am prefer `1666` distance with `16:9` monitor.
```
Would you like to backup "libclient.so"? [Y/n]: 
Enter pitch max [current="1666", default="1134"]: 1234
Replacing " dota_camera_pitch_max 1666" to " dota_camera_pitch_max 1234".
Done!
```
