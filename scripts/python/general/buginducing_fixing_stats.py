import ast

import pandas as pd
import csv
import os

path_inducing = '/Volumes/Cisco/Fall2021/quantum-revision/Analysis/bugs/'
path_file = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/snapshots/file-histroy/'
input_path = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/'

# path_bugs = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/bugs2/inducing-fixing-dates/'
file = 'MLRepos_Quantum_non_quantum.xlsx'
xl1 = pd.ExcelFile(input_path + file)
df_data = xl1.parse('quant_non_quantum')
# Convert to list
Repos_Name = df_data.Repos_Name.values.tolist()
file_name = df_data.file_name.values.tolist()
Language = df_data.Language.values.tolist()

df_data = xl1.parse('category')
Repos_Name_2 = df_data.Repos_Name.values.tolist()
Type_ = df_data.Type.values.tolist()
ID = df_data.ID.values.tolist()

df_inducing = pd.read_csv(path_inducing+'Inducing-combine_dates_latest.csv')
inducing_project = df_inducing.project.values.tolist()
inducing_BugInducing = df_inducing.BugInducing.values.tolist()
inducing_Date = df_inducing.Date.values.tolist()
inducing_CLOC = df_inducing.CLOC.values.tolist()
inducing_Files = df_inducing.Files.values.tolist()

df_fixing = pd.read_csv(path_inducing + 'BugInducing-details_combined_latest.csv')
fixing_project = df_fixing.project.values.tolist()
fixing_Bugfixing = df_fixing.Bugfixing.values.tolist()
fixing_Date = df_fixing.Date.values.tolist()
fixing_Bugs = df_fixing.Bugs.values.tolist()
fixing_issues = df_fixing.issues.values.tolist()
fixing_Buggy_issues = df_fixing.Buggy_issues.values.tolist()
fixing_is_status = df_fixing.is_status.values.tolist()
fixing_changedfiles= df_fixing.changedfiles.values.tolist()
fixing_cloc = df_fixing.cloc.values.tolist()

exclude_categories = ['None-Quantum','Web-Extension', 'Fun/ Game']

data_file2 = open(path_inducing + '10categories/inducing-10categories_files_ID.csv', mode='w', newline='', encoding='utf-8')
data_writer2 = csv.writer(data_file2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
data_writer2.writerow(["Category", 'project', 'BugInducing','ID', 'Files'])

data_file3 = open(path_inducing + '10categories/fixing-10categories_files_ID.csv', mode='w', newline='', encoding='utf-8')
data_writer3 = csv.writer(data_file3, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
data_writer3.writerow(["Category", 'project', 'Bugfixing','ID', 'changedfiles'])


unique_bugs = set()
unique_bugs_files = set()
for repo in set(inducing_project):
    repo_ = repo.split('/')[1]
    if repo in Repos_Name_2:
        index_of = Repos_Name.index(repo)
        cat = Type_[Repos_Name_2.index(repo)]
        if os.path.exists(path_file + repo_ + '_' + str(index_of) + '.csv') and not cat in exclude_categories:
            print('inside')
            df_data = pd.read_csv(path_file + repo_ + '_' + str(index_of) + '.csv')
            FileName_ = df_data.FileName.values.tolist()
            Added_ = df_data.Added.values.tolist()
            Removed_ = df_data.Removed.values.tolist()
            Id_ = df_data.Id.values.tolist()

            Id = []
            FileName = []
            Added = []
            Removed = []

            for a in range(len(FileName_)):
                file_str = str(FileName_[a]).lower()  # and not 'test' in file_str
                if not 'readme' in file_str and not 'doc' in file_str \
                        and not '.png' in file_str \
                        and not '.pdf' in file_str and not '.jpeg' in file_str \
                        and not '.jpg' in file_str and not '.gif' in file_str \
                        and not 'license' in file_str and not 'makefile' in file_str \
                        and not '.txt' in file_str and not '.md' in file_str and not 'cmake' in file_str \
                        and not '.git' in file_str and not '.yml' in file_str and not '.json' in file_str \
                        and not '.rst' in file_str and not 'changelog' in file_str and not '.bib' in file_str \
                        and not 'tox.' in file_str:
                    Id.append(Id_[a])
                    FileName.append(FileName_[a])
                    Added.append(Added_[a])
                    Removed.append(Removed_[a])

            for i in range(len(inducing_project)):
                if repo == inducing_project[i]:
                    #if not cat in exclude_categories:
                    try:
                        data_json = ast.literal_eval(str(inducing_Files[i]))
                        for key, val in data_json.items():
                            file_id = -1
                            if key in FileName:
                                unique_bugs.add(inducing_BugInducing[i])
                                unique_bugs_files.add(key)
                                file_id = Id[FileName.index(key)]
                                data_writer2.writerow([cat, inducing_project[i], inducing_BugInducing[i],file_id, key])
                    except Exception as e:
                        print(e)
            for i in range(len(fixing_project)):
                if fixing_project[i] == repo:
                    #if not cat in exclude_categories:
                    try:
                        data_list = ast.literal_eval(str(fixing_changedfiles[i]))
                        for key in data_list:
                            file_id = -1
                            if key in FileName:
                                file_id = Id[FileName.index(key)]
                            data_writer3.writerow([cat, fixing_project[i], fixing_Bugfixing[i], file_id, key])
                    except Exception as e:
                        print(e)


print('Unique inducing: ', len(unique_bugs), 'unique files: ', len(unique_bugs_files))
data_file3.close()
data_file2.close()
'''



        '''