import src
import src.main

if __name__ == '__main__':
    # Task: find the latest plan in a directory
    # find all files in path
    # sort by created time,
    # assuming latest created time equals the latest plan
    files=src.main.search(dir='./temporal_plans_dir',sort='ctime',descending=True)
    print(files[0])
    #plan is not the latest plan


