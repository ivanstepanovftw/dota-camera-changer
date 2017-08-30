# linux-dota-camchanger
Changes camera distance in Dota 2.

## Download
```bash
git clone https://github.com/AshFTW/linux-dota-camchanger.git
```

```bash
cd ./linux-dota-camchanger
```

## Installing
Required Python 3.x
```bash
sudo apt-get install python3
```

Move `camchanger.py` in `libclient.so` location:
```bash
cp ./camchanger.py ~/.steam/steam/steamapps/common/dota\ 2\ beta/game/dota/bin/linuxsteamrt64/camchanger.py
```

## Launching
```bash
python3 camchanger.py
```

## Usage example
```
Would you like to backup "libclient.so"? [Y/n]: 
Enter pitch max [current="1666", default="1134"]: 1234
Replacing " dota_camera_pitch_max 1666" to " dota_camera_pitch_max 1234".
Done!
```
I am prefer `1666` distance with `16:9` monitor.
