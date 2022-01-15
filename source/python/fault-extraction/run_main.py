#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
import os, sys, shutil
import pandas as pd
import csv
import re
from pydriller import Repository
from utils.github import GitHubMeta
from analysis.Git import Git
sys.setrecursionlimit(10000)

bugs = ["fixed ", "fixes ", " fixed", " fixes", "crash", " resolves",
"resolves ", "regression", "fall back", "assertion", "coverity", "reproducible",
"stack-wanted", "steps-wanted", "testcase", "failur", "fail", "npe ",
" npe", "except", "broken", " bug", "differential testing", "error", "addresssanitizer",
"hang ", " hang", "permaorange", "random orange", "intermittent", "test fix",
"steps to reproduce", "crash", "assertion", "failure", "leak", "stack trace", "heap overflow", "freez", "str:", "fix ", " fix", "problem ", " problem", " overflow", "overflow ", "avoid ", " avoid", " issue", "issue ", "workaround ", " workaround", "break ", " break", " stop", "stop "];

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_bugs = 'data/pydriller'
if not os.path.exists(path_bugs):
    os.makedirs(path_bugs)
def run_main():
    # Convert to list
    df_data = pd.read_csv('quantum_nonquantum_input.csv')
    Repos = df_data.Repos_Name.values.tolist()
    file_name = df_data.file_name.values.tolist()
    Language = df_data.Language.values.tolist()
    path_snaps = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/sonar-results/analysis/snapshots_v2/'

    df_data2 = pd.read_csv('category.csv')
    Repos2 = df_data2.Repos_Name.values.tolist()

    data_file = open(path_bugs + '/repos-commits-message3.csv', mode='w', newline='',
                          encoding='utf-8')
    data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    data_writer.writerow(['Repos','Hash', "Name", 'Email', "Date",  "Added", "Removed","bug_msg", "Message","issues", 'Buggy_issues', 'issues_status', 'filenames', 'old_path', 'new_path', 'complexity', 'nloc', 'added_lines', 'deleted_lines'])
    ct = 0
    for repo_index in range(82,len(Repos)):
        #if Repos[repo_index] in Repos2:

        repo = Repos[repo_index]
        repo_name = repo.split('/')[1]
        if not os.path.exists('data/projects'):
            os.makedirs('data/projects')
        #log_tags_path = path_codes+'/logs/' + repo_name+'_'+str(repo_index)+ '.txt'
        repo_root1 = 'data/projects/'+repo_name
        repo_root = 'data/projects/'+repo.replace('/', '_')
        repo_root_snapshots = 'data/snapshots/'+repo_name
        if os.path.exists(path_snaps + repo_name + '_' + str(repo_index) + '_snaps_v2.csv'):
            print(repo_index, repo)
            repository_url = "https://github.com/" + repo + ".git"

            if not os.path.exists(repo_root):
                code = Git.clone_git_repository(url=repository_url, target_path='data/projects')
                os.chdir(ROOT_DIR)
                os.rename(repo_root1, repo_root)
            else:
                code = 0
            if code == 0:
                total_buggy_commits = 0
                total_inducing_commits = 0
                total_added = 0
                total_deleted = 0

                added_buggy = 0
                deleted_buggy = 0
                index = 0
                os.chdir(ROOT_DIR)
                for commit in Repository(repo_root).traverse_commits():

                    gr = Git('test-repos/test5')

                    commit = gr.get_commit('lmn')
                    buggy_commits = gr.get_commits_last_modified_lines(commit)

                    #print("{} : {}".format(index, commit.hash))
                    index += 1
                    flag = 0
                    bug_msg = ""
                    added = 0
                    deleted = 0
                    #try:
                    if index%100 == 0:
                        print('    ---- ', index)
                    added = commit.insertions
                    deleted = commit.deletions

                    #    print(modified.filename, modified.old_path, modified.new_path, modified.complexity, modified.nloc, modified.added_lines, modified.deleted_lines, modified.methods)
                    for bug in bugs:
                        if bug in commit.msg.lower():
                            flag = 1
                            bug_msg = "{}{} , ".format(bug_msg, bug)
                            added_buggy += added
                            deleted_buggy += deleted
                    issues_flag = re.findall('#[0-9]+', str(commit.msg))
                    #if flag == 1:
                    list_isbuggy = []
                    issues_status = []
                    flag_is_buggy = 0
                    if len(issues_flag) > 0:
                        for ref in issues_flag:
                            is_buggy, state, ct = GitHubMeta(Repos[repo_index], ct).check_issues_buggy_(ref.replace('#', ''))
                            list_isbuggy.append(is_buggy)
                            issues_status.append(state)
                            if is_buggy == True:
                                flag_is_buggy += 1
                                print('         -- buggy issue: ', ref)
                    else:
                        issues_flag = ''
                    if flag == 1 or flag_is_buggy == 1:
                        for modified in commit.modified_files:
                            if not 'test' in str(modified.filename).lower() and not '.md' in str(modified.filename).lower():
                                methods = []
                                for name in modified.methods:
                                    methods.append(name)
                                changed_methods = []
                                for name in modified.changed_methods:
                                    changed_methods.append(name)
                                data_writer.writerow([Repos[repo_index],commit.hash, commit.author.name, commit.author.email, commit.author_date,  added, deleted,bug_msg, commit.msg, issues_flag,
                     list_isbuggy,issues_status, modified.filename, modified.old_path, modified.new_path, modified.complexity, modified.nloc, modified.added_lines, modified.deleted_lines])
                try:
                    shutil.rmtree(repo_root)
                except OSError as e:
                    print("Error: %s - %s." % (e.filename, e.strerror))
    data_file.close()
if __name__ == '__main__':
    run_main()
