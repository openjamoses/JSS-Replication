import pandas as pd
import numpy as np
import os
import subprocess
from datetime import date
import time

def clone_git_repository(url, target_path):
    os.chdir(target_path)
    git_clone_command = "git clone " + url
    print("Cloning repository from :{} into {}".format(url, target_path))
    p = subprocess.Popen(git_clone_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ""
    for line in p.stdout.readlines():
        output = output + str(line) + '\n'
    retval = p.wait()
    if retval == 0:
        print("Repository cloned successfully!")
    else:
        print("Error in cloning!")
        print(output)
    return retval

def extract_git_commit_logs(repo_path, log_path):
    os.chdir(repo_path)
    git_log_command = "git --no-pager log --pretty=format:\"%H|%ad|%an|%s\" --date=short >" + log_path
    # print(git_log_command)
    print("Extracting commit logs from repository in :{}".format(repo_path))
    p = subprocess.Popen(git_log_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ""
    for line in p.stdout.readlines():
        output = output + str(line) + '\n'
    retval = p.wait()
    if retval == 0:
        print("Commit log extracted successfully!")
    else:
        print("Error in commit log extraction!")
        print(output)
    return retval


def list_git_commits(log_path):
    commit_list = []
    try:
        with open(log_path, "r", encoding='utf-8') as fp:
            text_lines = fp.readlines()
            for line in text_lines:
                try:
                    log_parts = line.split('|')
                    #print(log_parts)
                    csha = log_parts[0]
                    c_date = log_parts[1]
                    commit_list.append([csha, c_date])
                except:
                    pass
        fp.close()
        no_commit = len(commit_list)
        commit_list1 = []
        for i in range(no_commit - 1, -1, -1):
            commit_list1.append(commit_list[i])
    except FileNotFoundError:
        print("Error in file reading")
    return commit_list1

def get_date_days_diff(date1, date2):
    dy1, dm1, dd1 = date1.split('-')
    dy2, dm2, dd2 = date2.split('-')

    d1 = date(int(dy1), int(dm1), int(dd1))
    d2 = date(int(dy2), int(dm2), int(dd2))

    delta = d2 - d1
    no_days = delta.days
    # print(delta.days)
    return no_days


def get_next_commit(commits, ref_commit, cur_pos, day_threshold):
    next_commit = None
    new_pos = cur_pos
    no_commit = len(commits)
    for i in range(cur_pos, no_commit - 1):
        if get_date_days_diff(ref_commit[1], commits[i][1]) > day_threshold:
            new_pos = i
            break
    if new_pos != cur_pos and new_pos != no_commit:
        next_commit = commits[new_pos]

    return next_commit, new_pos


def select_git_snapshots(commits, start_pos=0, day_threshold=90):
    n_commits = len(commits)
    selected_commits = []
    c1 = commits[start_pos]
    cur_pos = start_pos
    selected_commits.append(c1)

    for i in range(start_pos, n_commits - 1):
        c2, pos = get_next_commit(commits=commits, ref_commit=c1, cur_pos=cur_pos, day_threshold=day_threshold)
        cur_pos = pos
        if c2 is not None:
            selected_commits.append(c2)
            c1 = c2
        else:
            break
    return selected_commits

def main_commits():
    path = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/'
    path_snaps = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/snapshots/all-snapshots/'
    repo_target_path_root = "/Users/mosesopenja/Documents/summer2020/Quantum/v2/snapshots/all"

    file = 'MLRepos_Quantum_non_quantum.xlsx'
    xl1 = pd.ExcelFile(path + file)
    df_topic = xl1.parse('quant_non_quantum')
    Repos_Name = df_topic.Repos_Name.values.tolist()
    file_name = df_topic.file_name.values.tolist()
    for index in range(len(Repos_Name)):
        if not file_name[index] is np.nan:
            print(index, Repos_Name[index])
            repository_url = "https://github.com/" + Repos_Name[index] + ".git"
            repo_name_parts = repository_url.split('/')
            repo_name = repo_name_parts[len(repo_name_parts) - 1]
            repo_name = repo_name.replace('.git', '')
            repo_path = repo_target_path_root + "/" + repo_name
            repo_path2 = repo_target_path_root + "/" + repo_name+"_"+str(index)

            log_path = repo_target_path_root + '/' + file_name[index] + '.txt'
            repository_url = "https://github.com/" + Repos_Name[index] + ".git"
            cloned = 0  # 0 if not cloned yet, else 1
            log_extracted = 0  # 0 if not log is not extracted yet, else 1

            if cloned == 0:
                clone = clone_git_repository(url=repository_url, target_path=repo_target_path_root)
                cloned = 1 if clone == 0 else 0
            if cloned == 1 and log_extracted == 0:
                extract_git_commit_logs(repo_path=repo_path, log_path=log_path)
            commit_list = list_git_commits(log_path)
            print("Commits listed: {}".format(len(commit_list)))
            # next_commit, pos = get_next_commit(commits=commit_list, ref_commit=commit_list[0], cur_pos=0, day_threshold=90)
            selected_commits = select_git_snapshots(commits=commit_list, start_pos=0, day_threshold=90)
            total = len(selected_commits)
            print('Selected Commits:', total)
            time.sleep(5)
            os.rename(repo_path, repo_path2)






main_commits()