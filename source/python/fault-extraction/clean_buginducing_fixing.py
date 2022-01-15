import ast
import random
import numpy as np

import pandas as pd
import csv

path_general = '/Volumes/Cisco/Fall2021/quantum-revision/Analysis/general/'
path_inducing = '/Volumes/Cisco/Fall2021/quantum-revision/Analysis/bugs/'
input_path = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/'

df_inducing = pd.read_csv(path_inducing+'Inducing-combine_dates_latest.csv')
inducing_project = df_inducing.project.values.tolist()
inducing_BugInducing = df_inducing.BugInducing.values.tolist()
inducing_Date = df_inducing.Date.values.tolist()
inducing_CLOC = df_inducing.CLOC.values.tolist()
inducing_Files = df_inducing.Files.values.tolist()

unique_commits = set()
unique_files_initial = set()
unique_files_final = set()
data_file = open(path_inducing + 'inducing-cleaned.csv', mode='w', newline='', encoding='utf-8')
data_writer = csv.writer(data_file)
data_writer.writerow(['Project','BugInducing', 'Date', 'CLOC', 'Files'])
file = 'MLRepos_Quantum_non_quantum.xlsx'
df_data = pd.read_excel(open(input_path + file, 'rb'), sheet_name='quant_non_quantum', engine="openpyxl")

# Convert to list
Repos_Name = df_data.Repos_Name.values.tolist()
file_name = df_data.file_name.values.tolist()
Language = df_data.Language.values.tolist()

df_data = pd.read_excel(open(input_path + file, 'rb'),  sheet_name='category', engine="openpyxl")
# Convert to list
Repos_Name2 = df_data.Repos_Name.values.tolist()
Type_ = df_data.Type.values.tolist()
ID = df_data.ID.values.tolist()

categories = set(Type_)
categories = set(Type_)
exclude_categories = ['None-Quantum','Web-Extension', 'Fun/ Game']
for cat in categories:
    if not cat in exclude_categories:
        list_proj = []
        for index in range(len(Repos_Name2)):
            if Type_[index] == cat:
                list_proj.append(Repos_Name2[index])
        for proj in list_proj:
            for index in range(len(inducing_project)):
                if inducing_project[index] == proj:
                    file_dict = ast.literal_eval(str(inducing_Files[index]))
                    flag = 0
                    for file_str, loc in file_dict.items():
                        file_str = str(file_str).lower()
                        unique_files_initial.add(file_str)
                        if not 'readme' in file_str and not 'doc' in file_str and not 'test' in file_str\
                                and not '.png' in file_str \
                                and not '.pdf' in file_str and not '.jpeg' in file_str \
                                and not '.jpg' in file_str and not '.gif' in file_str \
                                and not 'licence' in file_str and not 'makefile' in file_str \
                                and not '.txt' in file_str and not '.md' in file_str and not 'cmake' in file_str \
                                and not '.git' in file_str and not '.yml' in file_str and not '.json' in file_str \
                                and not '.rst' in file_str and not 'changelog' in file_str and not '.bib' in file_str \
                                and not 'tox.' in file_str:
                            unique_files_final.add(file_str)
                            flag += 1
                    if flag > 0:
                        unique_commits.add(inducing_BugInducing[index])
                        data_writer.writerow([inducing_project[index], inducing_BugInducing[index], inducing_Date[index], inducing_CLOC[index], inducing_Files[index]])
data_file.close()
print('Bug inducing summary, fixing commits: ', len(unique_commits), '/',len(set(inducing_BugInducing)), 'files: ',len(unique_files_final),'/', len(unique_files_initial))
sample_inducing = random.sample(list(unique_commits), 381)




df_fixing = pd.read_csv(path_inducing + 'BugInducing-details_combined_latest.csv')
fixing_project = df_fixing.project.values.tolist()
fixing_Bugfixing = df_fixing.Bugfixing.values.tolist()
fixing_Date = df_fixing.Date.values.tolist()
fixing_Bugs = df_fixing.Bugs.values.tolist()

issues = df_fixing.issues.values.tolist()
Buggy_issues = df_fixing.Buggy_issues.values.tolist()
is_status = df_fixing.is_status.values.tolist()
totalinducing2 = df_fixing.totalinducing2.values.tolist()
BugInducing = df_fixing.BugInducing.values.tolist()
fixing_changedfiles = df_fixing.changedfiles.values.tolist()
fixing_cloc = df_fixing.cloc.values.tolist()

df_msg = pd.read_csv(path_inducing + 'repos-commits-message.csv')
Hash = df_msg.Hash.values.tolist()
Message = df_msg.Message.values.tolist()

data_file = open(path_inducing + 'sampled-inducing-381.csv', mode='w', newline='', encoding='utf-8')
data_writer = csv.writer(data_file)
data_writer.writerow(['project','Buginducing', 'Date', 'Modifiedfiles', 'LOC', 'TotalFixing', 'Bugfixing', 'FixingFiles', 'Tag', 'commitmessage'])
for sample_ in sample_inducing:
    set_fixing = set()
    set_files = set()
    loc_dict = {}
    cloc = 0
    index_of = inducing_BugInducing.index(sample_)
    for i in range(len(BugInducing)):
        if sample_ in str(BugInducing[i]):
            set_fixing.add(fixing_Bugfixing[i])
            #print(type(eval(fixing_cloc[i])), eval(fixing_cloc[i]))
            cloc += np.sum(eval(fixing_cloc[i]))
            try:
                file_dict = ast.literal_eval(str(BugInducing[i]))
                for file_, shaaL in file_dict.items():
                    if sample_ in shaaL:
                        set_files.add(file_)
            except:
                pass
    tag_flag = 0
    for file1, loc in ast.literal_eval(str(inducing_Files[index_of])).items():
        for file2 in set_files:
            if file1 == file2:
                tag_flag += 1
    Tag = False
    if tag_flag > 0:
        Tag = True
    if cloc > 5000:
        Tag = 'Unclear'
    msg = ''
    if sample_ in Hash:
        msg = Message[Hash.index(sample_)]
    data_writer.writerow(
        [inducing_project[index_of], sample_, inducing_Date[index_of], inducing_Files[index_of], inducing_CLOC[index_of], len(set_fixing), set_fixing, set_files, Tag, msg])
data_file.close()

data_file = open(path_inducing + 'Bugfixing-inducing-cleaned.csv', mode='w', newline='', encoding='utf-8')
data_writer = csv.writer(data_file)
data_writer.writerow(['project','Bugfixing', 'Date', 'Bugs_keywords', 'issues_reference', 'Buggy_issues', 'issues_status', 'changedfiles', 'cloc', 'totalinducing', 'BugInducing_details'])

unique_fixing = set()
unique_files = set()
inital_files = set()
for cat in categories:
    if not cat in exclude_categories:
        list_proj = []
        for index in range(len(Repos_Name2)):
            if Type_[index] == cat:
                list_proj.append(Repos_Name2[index])
        for proj in list_proj:
            for index in range(len(fixing_project)):
                if fixing_project[index] == proj:
                    file_dict = ast.literal_eval(str(inducing_Files[index]))
                    flag = 0
                    for file_str in list(fixing_changedfiles[index]):
                        file_str = str(file_str).lower()
                        inital_files.add(file_str)
                        if not 'readme' in file_str and not 'doc' in file_str and not 'test' in file_str \
                                and not '.png' in file_str \
                                and not '.pdf' in file_str and not '.jpeg' in file_str \
                                and not '.jpg' in file_str and not '.gif' in file_str \
                                and not 'licence' in file_str and not 'makefile' in file_str \
                                and not '.txt' in file_str and not '.md' in file_str and not 'cmake' in file_str \
                                and not '.git' in file_str and not '.yml' in file_str and not '.json' in file_str \
                                and not '.rst' in file_str and not 'changelog' in file_str and not '.bib' in file_str \
                                and not 'tox.' in file_str:
                            flag += 1
                            unique_files.add(file_str)

                    #print(totalinducing2[index])
                    if flag > 0:
                        unique_fixing.add(fixing_Bugfixing[index])
                        data_writer.writerow(
                            [fixing_project[index], fixing_Bugfixing[index], fixing_Date[index], fixing_Bugs[index], issues[index], Buggy_issues[index], is_status[index],
                             fixing_changedfiles[index], fixing_cloc[index], totalinducing2[index], BugInducing[index]])
data_file.close()
sample_fixing = random.sample(list(unique_fixing), 379)
print('Bug fixing summary, fixing commits: ', len(unique_fixing), '/',len(set(fixing_Bugfixing)), 'files: ',len(unique_files),'/', len(inital_files))

data_file = open(path_inducing + 'sampled-bugfixing-379.csv', mode='w', newline='', encoding='utf-8')
data_writer = csv.writer(data_file)
data_writer.writerow(['project','Bugfixing', 'Date', 'Bugs_keywords', 'issues_reference', 'Buggy_issues', 'issues_status', 'changedfiles', 'cloc', 'Tag','CommitMessage'])
for sample_ in sample_fixing:
    index_of = fixing_Bugfixing.index(sample_)
    msg = ''
    if sample_ in Hash:
        msg = Message[Hash.index(sample_)]
    data_writer.writerow(
        [fixing_project[index_of], sample_, fixing_Date[index_of], fixing_Bugs[index_of], issues[index_of], Buggy_issues[index_of], is_status[index_of],
         fixing_changedfiles[index_of], fixing_cloc[index_of], True, msg])
data_file.close()
