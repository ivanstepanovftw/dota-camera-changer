# dota-camchanger

#### English description:
Change and adjust camera distance in Dota 2 (rerun after each update).

#### Russian описание:
Это полностью легальный чит для дота 2, делает камеру подальше. Запускать каждый раз после обновления доты.
Переведи страницу и следуй инструкциям.

<p align="center">
<img src="https://i.imgur.com/oX3cl9t.jpg">
</p>
  

# Windows
### Install
Download and install Python 3 from [offical website](https://www.python.org/downloads/).
<br><br>
[Download](https://github.com/ivanstepanovftw/dota-camera-changer/archive/master.zip) this repository and unpack files
to `<path to Steam>\steamapps\common\dota 2 beta\game\dota\bin\win<your system architecture>\ ` <br>
*By default*: `C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\game\dota\bin\win64\ `
<br><br>
Create shortcut by moving `camchanger.py` with <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Mouse 1</kbd> to your Desktop.

### Launching
Just launch `camchanger - Shortcut` at your Desktop and ask the questions.

### Troubleshooting Windows
> Script is not running via link on Desktop, but runs in place with `client.dll`

Ensure that you pressed <kbd>Shift</kbd> while making link. If trouble exists, make shortcut to `\win64\ ` directory. 

# Linux
Required Python 3.x
```bash
# Debian/Ubuntu/Linux Mint:
sudo apt-get install python3

# Arch Linux/Manjaro
sudo pacman -S python3
```

### Download
**Do not download with sudo!**
```bash
git clone https://github.com/ivanstepanovftw/dota-camera-changer.git
```

### Installing
Modify `path_to_dota`:
```bash
path_to_dota="~/.steam/steam/steamapps/common/dota\ 2\ beta"
```

Move `camchanger.py` in place with `libclient.so`:
```bash
cp ./dota-camera-changer/camchanger.py ${path_to_dota}/game/dota/bin/linuxsteamrt64/camchanger.py
```

Make bash script at your home `~/` folder:
```bash
cd ~
echo "cd ${path_to_dota}/game/dota/bin/linuxsteamrt64/ && python3 camchanger.py && chmod +rwx libclient.so" > ~/dotacamchanger.sh
chmod +x ~/dotacamchanger.sh
```

### Launching
If you made bash script, you can easily just launch terminal (<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>) after each dota 2 update, type `./dotac`, press <kbd>Tab</kbd> (you will see `./dotacamchanger `) and hit <kbd>Enter</kbd>(<kbd>Return</kbd>).


# Showcase
## Output example
With `16:9` monitor, I am prefer `1700` distance. But lets make `1234` distance:
```
Would you like to backup "libclient.so"? [Y/n]: 
Enter pitch max [current="1700", default="1134"]: 1234
Done!
```

## Screenshots
### 16:4 with 1666 camera pitch
<img src="https://i.imgur.com/Mge0u4e.jpg">

### 5:4 with 1666 camera pitch
<img src="https://i.imgur.com/84hgaLz.jpg">
