#!/usr/bin/env python3


import psutil


FSTYPES = [
    'ext3',
    'ext4',
    'fuse.sshfs',
    'nfs']


def find_backup_location():
    '''Find device name and mount point of external drive for storing backup(s)'''
    try:
        drives = {}
        for p in psutil.disk_partitions():
            if p.mountpoint != 'C:\\' and 'rw' in p.opts.split(','):
                drives[p.mountpoint] = p.fstype
        for key, value in drives.items():
            if value not in FSTYPES:
                del drives[key]
        if len(drives) == 0:
            raise Exception("Failed to locate backup drive.")
        elif len(drives) == 1:
            (x, y), = drives.items()
            return x, y
        else:
            print("*Multiple external drives compatible as target backup locations found*")
            with i == 1:
                for key, value in drives.items(): 
                    print(f"* {i} ---> {key} (type: {value})")
                    i += 1
            x = input("Enter # for drive to set as backup location: ")
            x = int(x.strip())
            with i == 1:
                for key, value in drives.items():
                    if x == i:
                        return key, value
                    i += 1
    except:
        raise Exception("Encountered an issue while attempting to locate external drive for storing backup.")


