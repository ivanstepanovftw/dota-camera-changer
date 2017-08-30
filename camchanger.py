import os

cam_default = "1134"
lib = "libclient.so"
to_find = b'\x00dota_camera_pitch_max\x00'


if __name__ == '__main__':
    if not os.access(lib, os.R_OK) or os.stat(lib).st_size == 0:
        print('File "'+lib+'" is empty or not exists.')
        if not os.access(lib+'.bak', os.R_OK) or os.stat(lib+'.bak').st_size == 0:
            print('Error: Restore file "'+lib+'.bak" missing or corrupt.')
            exit(15)
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
                exit(10)
    fr = open(lib, 'rb')
    content = fr.read()
    fr.close()
    off = content.find(to_find)
    if off != -1:
        is_backup = (input('Would you like to backup "'+lib+'"? [Y/n]: ') or 'y')[0].lower()
        if is_backup == 'y':
            if os.access(lib+'.bak', os.R_OK):
                os.remove(lib+'.bak')
            os.rename(lib, lib+'.bak')
        cam_curr = content[off+len(to_find):off+len(to_find)+4].decode('ascii')
        camera_pitch = input('Enter pitch max [current="'+cam_curr+'", default="'+cam_default+'"]: ')[:4] or cam_default
        camera_pitch = '0'*(4-len(camera_pitch)) + camera_pitch
        print('Replacing "'+(to_find+bytes(cam_curr, 'ascii')).decode('ascii')+'" to "'+(to_find+bytes(camera_pitch, 'ascii')).decode('ascii')+'".')

        content = content.replace(to_find+bytes(cam_curr, "ascii"), to_find+bytes(camera_pitch, 'ascii'))
        fw = open(lib, 'wb')
        fw.write(content)
        print('Done!')
    else:
        print('Error: Cannot find "'+to_find+' in "'+lib+'".')
        exit(20)
