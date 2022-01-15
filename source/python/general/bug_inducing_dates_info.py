import ast

import pandas as pd
import csv
import json

from src.quantum_revision.utils.github import GitHubMeta

path = '/Volumes/Cisco/Fall2021/quantum-revision/Analysis/bugs/old/'
df_data = pd.read_csv(path + 'BugInducing-details_combined_latest.csv')
project = df_data.project.values.tolist()
Bugfixing = df_data.Bugfixing.values.tolist()
Date = df_data.Date.values.tolist()
changedfiles = df_data.changedfiles.values.tolist()
cloc = df_data.cloc.values.tolist()
TotalBugInducing = df_data.TotalBugInducing.values.tolist()
BugInducing = df_data.BugInducing.values.tolist()

df = pd.read_csv(path + 'Inducing-dates_latest.csv')
project_read = df.project.values.tolist()

data_file = open(path + 'Inducing-dates_latest2.csv', mode='w', newline='', encoding='utf-8')
data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
data_writer.writerow(['project', 'BugInducing', "Date", "CLOC", "Files"])
ct = 0
for proj in set(project):
    if not proj in project_read:
        set_inducing = set()
        for i in range(len(project)):
            if proj == project[i]:
                bug_str = str(BugInducing[i])
                try:
                    data_json = ast.literal_eval(bug_str)
                    for key, val in data_json.items():
                        for hash in val:
                            set_inducing.add(hash)
                except Exception as e:
                    print(e)
        print(proj, len(set_inducing))
        counts = 0
        for hash in set_inducing:
            counts += 1
            if counts%200 == 0:
                print('    ---', counts)
            data_dict, ct = GitHubMeta(proj, ct).get_file_dates_infor_hash_(hash)
            if data_dict != None:
                dict_files = {}
                for key, val in data_dict.items():
                    if key != 'date' and key != 'cloc':
                        dict_files[key] = val
                data_writer.writerow([proj, hash, data_dict['date'], data_dict['cloc'], dict_files])
data_file.close()