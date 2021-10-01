import os

import upload
import download
import json
def main():
    while True:
        a=input('What do you wanna do?(D(download)/U(upload)/Q(quit))')
        a=a.lower()
        if a=='u':
            path=input('Enter path.')
            raw_path=input('Enter raw_path.')
            token=input('Enter token.')
            map=upload.upload(path,raw_path,token)
            print('uploading done.')
            map_path=input('Enter directory path in which to place .map file.')
            map_path=os.path.join(map_path,map[4])+'.map'
            with open(map_path,'w') as file:
                string=json.dumps(map)
                file.write(string)
            print(f'.map file created at {map_path}')
            print(f'Upload process is done and .map file is created at {map_path}')
            print(f'please take care of deleting files in {raw_path}')
        elif a=='d':
            path=input('Enter path to .map file.')
            with open(path,'r') as file:
                map=json.loads(file.read())
            download_path=input('Enter Download path.')
            destination_path=input('Enter destination dir.')
            download.download(map,download_path,destination_path)
            print(f'download process is done and files have been re-created at {destination_path}.')
            print(f'please take care of deleting files in {download_path}')
        elif a=='q':
            quit()
        else:
            raise ValueError('Wrong input')



main()