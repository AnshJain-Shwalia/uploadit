import os
import cr_dir
import recreate

def download(map, download_path, recreation_path):
    for elem in map[5]:
        stat = os.system(f'cd {download_path}; git clone {elem}')
    cr_dir.cr_dir(map, recreation_path)
    recreate.recreate(map, download_path, recreation_path)
