import os
from github import Github

def to_github(map,raw_path,token,):
    g=Github(token)
    user=g.get_user()
    username=user.login
    origin_path_sub = f'https://{username}:{token}@github.com/{username}/'
    base=map[4]
    for elem in os.listdir(raw_path):
        new = os.path.join(raw_path, elem)
        stat = os.system(f'cd {new}')
        if stat != 0:
            raise Exception(f"Couldn't change directories to {new}.")
        # initialising repo in {new}
        stat = os.system(f'cd {new}; git init')
        print(f'Initialised repo in {new}')
        print(base)
        print(elem)
        repo_name = base + '_' + elem
        # Creating repo
        repo = g.get_user().create_repo(repo_name)
        print(f"Created github repo")
        # Adding repo_link to map
        repo_link = f'https://github.com/{username}/{repo_name}.git'
        map[5].append(repo_link)
        # adding remote origin
        origin_path = origin_path_sub + repo_name + '.git'
        stat2 = os.popen(f'cd {new};git remote add origin {origin_path}')
        print(f'origin added at {origin_path}')
        # adding file to staging area
        stat = os.system(f'cd {new}; git add -A')
        print('Files added to staging area')
        # setting up config info
        stat = os.system(f'cd {new}; git config user.name "ligma"')
        stat = os.system(f'cd {new}; git config user.email ligma@balls.bitch')
        print('User config added')
        # commiting files
        stat = os.popen(f'cd {new}; git commit -a -m "here."')
        print(f'Files in {new} commited')
        # pushing commits
        stat = os.popen(f'cd {new}; git push -u origin master')
        print(f'Files in {new} pushed to origin')
        print(stat.read())
        print(f'done with {new}')