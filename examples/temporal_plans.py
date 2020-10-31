import src.main as tp
import src

if __name__ == '__main__':
    # Task: find the latest plan in a directory
    # find all files in path
    files=src.main.search(dir='./temporal_plans_dir')
    # sort by created time,
    # assuming latest created time equals the latest plan
    plans=src.main.sort_paths(files,'ctime',descending=True)
    latest_plan=plans[0]
    print(latest_plan)
    #plan is not the latest plan