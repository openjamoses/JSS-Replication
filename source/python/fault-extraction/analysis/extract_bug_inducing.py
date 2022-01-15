#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
import ast
import os, sys, shutil
from shlex import split as format_cmd
from subprocess import Popen, PIPE, STDOUT, call
import pandas as pd
import csv
import re

from pydriller import Repository, Git

import git_command

path = '/Volumes/Cisco/Fall2021/quantum-revision/Analysis/bugs/old/'
data_file = open(path + 'BugInducing-details_latest4.csv', mode='w',newline='', encoding='utf-8')
data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
data_writer.writerow(['project', 'Bugfixing', "Date", "Bugs", "issues",  'Buggy_issues','is_status', 'changedfiles', 'cloc', "TotalBugInducing", 'totalinducing2', 'BugInducing', 'unique_bugfixing', 'uniquebuginducing', 'uniquebuginducing_hash'])
df = pd.read_csv(path + 'BugInducing-details_latest.csv')
repo_read = df.project.values.tolist()
list_repos = []
for repo_ in repo_read:
    list_repos.append(repo_)
df = pd.read_csv(path + 'BugInducing-details_latest2.csv')
repo_read = df.project.values.tolist()
for repo_ in repo_read:
    list_repos.append(repo_)
df = pd.read_csv(path + 'BugInducing-details_latest3.csv')
repo_read = df.project.values.tolist()
for repo_ in repo_read:
    list_repos.append(repo_)
path_cat = '/Volumes/Cisco/Fall2021/quantum-revision/codes/bug-implimentation/'
df_cat = pd.read_csv(path_cat + 'category.csv')
Repos_cat = df_cat.Repos_Name.values.tolist()

sys.setrecursionlimit(10000)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path = '/Volumes/Cisco/Fall2021/quantum-revision/Analysis/bugs/old/'
df_data = pd.read_csv(path + 'Bug-details_latest.csv')
Repos = df_data.project.values.tolist()
Bugfixing = df_data.Bugfixing.values.tolist()
Date = df_data.Date.values.tolist()
Bugs = df_data.Bugs.values.tolist()
Commitmessage = df_data.Commitmessage.values.tolist()
issues = df_data.issues.values.tolist()
Buggy_issues = df_data.Buggy_issues.values.tolist()
is_status = df_data.is_status.values.tolist()
changedfiles = df_data.changedfiles.values.tolist()
cloc = df_data.cloc.values.tolist()
TotalBugInducing = df_data.TotalBugInducing.values.tolist()
#path_codes = 'data/projects'

#print(set(Name))
set_bug_fixing = set()
set_bug_inducing = set()
cm_inducing = 0
cm_fixing = 0
counts = 0
for proj in set(Repos):
    #bug_list = []
    if not proj in list_repos:
        if proj in Repos_cat:
            print(counts, proj)
            counts += 1

            repo = proj
            repo_name = repo.split('/')[1]
            if not os.path.exists('data/projects'):
                os.makedirs('data/projects')
            repo_root = 'data/projects/' + repo.split('/')[1]
            repository_url = "https://github.com/" + repo + ".git"
            if not os.path.exists(repo_root):
                code = git_command.Git.clone_git_repository(url=repository_url, target_path='data/projects')
            #else:
            os.chdir(ROOT_DIR)
            gr = Git(repo_root)
            index = 0
            #print(proj)
            for i in range(len(Repos)):
                if proj == Repos[i]:
                    try:
                        commit = gr.get_commit(Bugfixing[i])
                        buggy_commits = gr.get_commits_last_modified_lines(commit)
                        total_inducing = len(set_bug_inducing)
                        total_fixing = len(set_bug_fixing)
                        set_bug_fixing.add(Bugfixing[i])
                        set_hash = set()
                        #print(buggy_commits)
                        for key in buggy_commits.keys():
                            if not '.md' in str(key):
                                #res = ast.literal_eval(buggy_commits.get(key))
                                for hash in buggy_commits.get(key):
                                    set_hash.add(hash)
                                    set_bug_inducing.add(hash)
                        hash_str = ''
                        for hash in set_hash:
                            hash_str += hash+', '
                        cm_inducing += len(set_bug_inducing)-total_inducing
                        cm_fixing += len(set_bug_fixing)-total_fixing
                        data_writer.writerow(
                            [proj, Bugfixing[i],  Date[i], Bugs[i], issues[i], Buggy_issues[i],
                             is_status[i], changedfiles[i], cloc[i], TotalBugInducing[i], len(set_hash), buggy_commits, cm_fixing,cm_inducing, hash_str])
                        #bug_list.append(Bugfixing[i])
                    except Exception as e:
                        print(' Error: ', e)
            try:
                shutil.rmtree(repo_root)
            except OSError as e:
                print("Error: %s - %s." % (e.filename, e.strerror))
data_file.close()

