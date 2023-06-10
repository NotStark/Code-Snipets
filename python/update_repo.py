import subprocess

def update_repo(path : str, git_token : str, git_username : str, repo_name : str):
    try : 
        subprocess.check_output(f'cd {path}', shell=True)
        subprocess.check_output(f'git pull https://{git_token}@github.com/{git_username}/{repo_name}.git', shell=True)
        print("Sucess! Updated the Repo")
    except Exception as e:
        return str(e)
