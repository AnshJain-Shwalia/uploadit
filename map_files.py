import os
def sub_map_files(map,path):
    if not (os.path.isdir(path)):
        raise ValueError('Path must be dir.')
    else:
        sub_dir=os.listdir(path)
        for i in range(len(sub_dir)):
            dir_path=os.path.join(path,sub_dir[i])
            sub_dir[i]=dir_path
            if os.path.isdir(dir_path):
                sub_map_files(map,dir_path)
            else:
                map[1].append(dir_path)



def map_files(map,path):
    sub_map_files(map,path)
    '''
    thing = path.split('/')
    replacement = thing[-1]
    for i in range(len(map[1])):
        map[1][i] = map[1][i].replace(path, replacement)'''



if __name__ == "__main__":
    map=[[],[]]
    map_files(map,'/home/ansh/Downloads')
    print(map)