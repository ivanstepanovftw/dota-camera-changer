import os
import re

cam_default = "1134"
cam_len = len(cam_default)

if os.name == "nt":
    # if windows
    lib = "client.dll"
    to_find = b'(?<=\x00)\d{4}(?=\x00\x00\x00\x00dota_camera_distance\x00)'
    pass
else:
    lib = "libclient.so"
    to_find = b'(?<=\x00dota_camera_pitch_max\x00)\d{4}(?=\x00)'


def main():
    if not os.access(lib, os.R_OK) or os.stat(lib).st_size == 0:
        print('File "'+lib+'" is empty or not exists.')
        if not os.access(lib+'.bak', os.R_OK) or os.stat(lib+'.bak').st_size == 0:
            print('Error: Restore file "'+lib+'.bak" missing or corrupt.')
            return 1
        else:
            is_restore = (input('Would you like to restore "'+lib+'" from "'+lib+'.bak"? [Y/n]: ') or 'y')[0].lower()
            if is_restore == 'y':
                if os.access(lib, os.R_OK):
                    print('Removing "'+lib+'"...')
                    os.remove(lib)
                print('Renaming "'+lib+'.bak" to "'+lib+'"...')
                os.rename(lib+'.bak', lib)
            else:
                print('Error: "'+lib+'" missing.')
                return 1
    with open(lib, 'rb') as fd:
        content = fd.read()

    cam_re = re.search(to_find, content)
    if cam_re is None:
        print("Error: Could not find pattern. to_find:", to_find, ", lib:", lib)
        return 1
    cam_curr = cam_re.group(0).decode("ascii")
    is_backup = (input('Would you like to backup "'+lib+'"? [Y/n]: ') or 'y')[0].lower()
    cam_new = input('Enter camera distance [current="'+cam_curr+'", default="'+cam_default+'"]: ') or cam_default
    cam_new = (cam_new[:cam_len]).zfill(cam_len).encode("ascii")
    content = re.sub(to_find, cam_new, content)

    if is_backup == 'y':
        if os.access(lib+'.bak', os.R_OK):
            os.remove(lib+'.bak')
        os.rename(lib, lib+'.bak')
    with open(lib, 'wb') as fd:
        fd.write(content)
    print('Done!')
    return 0


if __name__ == '__main__':
    exit(main())
