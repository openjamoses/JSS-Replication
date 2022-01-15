import os
from statistics import mean, median, stdev

import pandas as pd
import csv
import numpy as np
import urllib.request
import json

from datetime import timedelta

from src.quantum.codeanalyser.v2.TOKENS import get_tokens

input_path = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/'

report_path = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/sonar-results/report/xlsx/'
ouput_path = '/Volumes/Cisco/Fall2021/quantum-revision/Analysis/RQ1/'
ouput_path2 = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/sonar-results/analysis_2/types/snaps/'
report_path3 = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/sonar-results/report/xlsx2/'

path_snaps = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/sonar-results/analysis/snapshots_v2/'

file = 'MLRepos_Quantum_non_quantum.xlsx'
#xl1 = pd.read_excel(input_path + file, engine='openpyxl')
#df_data = xl1.parse('quant_non_quantum')
#df_data = pd.read_excel(
#     os.path.join(input_path, "quant_non_quantum", file),
#     engine='openpyxl',
#)

df_data = pd.read_excel(open(input_path + file, 'rb'), sheet_name='quant_non_quantum')

# Convert to list
Repos_Name = df_data.Repos_Name.values.tolist()
file_name = df_data.file_name.values.tolist()
Language = df_data.Language.values.tolist()

df_data = pd.read_excel(open(input_path + file, 'rb'),  sheet_name='category')
#df_data = pd.read_excel(
#     os.path.join(input_path, "category", file),
#     engine='openpyxl',
#)
#df_data = xl1.parse('category')
# Convert to list
Repos_Name2 = df_data.Repos_Name.values.tolist()
Type_ = df_data.Type.values.tolist()
ID = df_data.ID.values.tolist()

categories = set(Type_)

data_file_1 = open(ouput_path + 'issues_types_category.csv', mode='w', newline='', encoding='utf-8')
data_writer_1 = csv.writer(data_file_1)

row = ['Category', 'Type', 'Frequency', 'Total', 'Percentage']
data_writer_1.writerow(row)

data_file_2 = open(ouput_path + 'issues_severity_category.csv', mode='w', newline='', encoding='utf-8')
row2 = ['Category','Severity', 'Frequency', 'Total', 'Percentage']
data_writer_2 = csv.writer(data_file_2)
data_writer_2.writerow(row2)

data_file_v2 = open(ouput_path + 'issues_types_category-v2.csv', mode='w', newline='', encoding='utf-8')
data_writer_v2 = csv.writer(data_file_v2)

row = ['Category','Project', 'Type', 'Frequency', 'Total', 'Percentage']
data_writer_v2.writerow(row)

data_file_v22 = open(ouput_path + 'issues_severity_category-V2.csv', mode='w', newline='', encoding='utf-8')
row2 = ['Category','Project','Severity', 'Frequency', 'Total', 'Percentage']
data_writer_v22 = csv.writer(data_file_v22)
data_writer_v22.writerow(row2)

exclude_categories = ['None-Quantum','Web-Extension', 'Fun/ Game']
for cat in categories:
    if not cat in exclude_categories:
        print(cat)
        List_bugs = []
        List_smells = []
        List_vulnerability = []
        List_critical = []
        List_major = []
        List_minor = []
        List_blocker = []
        List_cloc = []

        List_bugs_1 = []
        List_smells_1 = []
        List_vulnerability_1 = []
        List_critical_1 = []
        List_major_1 = []
        List_minor_1 = []
        List_blocker_1 = []
        List_cloc_1 = []

        for index in range(len(Repos_Name2)):
            if cat == Type_[index]:
                index_of = Repos_Name.index(Repos_Name2[index])
                repos = Repos_Name2[index].split('/')[1]
                if os.path.exists(path_snaps + repos + '_' + str(index_of) + '_snaps_v2.csv'):
                    df_data = pd.read_csv(path_snaps + repos + '_' + str(index_of) + '_snaps_v2.csv')
                    snapshots = df_data.snapshots.values.tolist()

                    # if os.path.exists(input_path + file_name[index_of]+'.xlsx'):
                    xl1 = pd.ExcelFile(report_path + file_name[index_of] + '.xlsx')
                    df_Issues = xl1.parse('Issues')
                    Type = df_Issues.Type.values.tolist()
                    Severity = df_Issues.Severity.tolist()
                    File = df_Issues.File.tolist()
                    Effort = df_Issues.Effort.tolist()

                    print(repos, index_of)

                    list_bugs_repo = []
                    list_smells_repo = []

                    list_critical_repo = []
                    list_major_repo = []
                    list_minor_repo = []
                    list_bloker_repo = []
                    if len(File) > 0:
                        xl2 = pd.ExcelFile(report_path3 + file_name[index_of] + '.xlsx')
                        df_Metrics = xl2.parse('Metrics')
                        # df_Metrics = xl1.parse('Metrics')
                        Path = df_Metrics.Path.values.tolist()
                        ncloc = df_Metrics.ncloc.tolist()

                        for snap_id in range(len(snapshots)):
                            cloc = 0
                            total_effort = 0
                            severity_dict = {}
                            type_dict = {}
                            for file_id in range(len(File)):
                                fileShaps = File[file_id][File[file_id].index(':') + 1:]
                                if file_name[index_of] + '/' + repos + '_' + str(snap_id) in fileShaps:
                                    path_index = Path.index(fileShaps)
                                    # print(path_index)
                                    cloc += ncloc[path_index]
                                    val = 0
                                    if ('h' or 'd') in Effort[file_id]:

                                        days = 1
                                        hrs = 0
                                        mins = 0
                                        if 'd' in Effort[file_id]:
                                            print(Effort[file_id])
                                            split_d = Effort[file_id].split('d')
                                            days = int(split_d[0])
                                            hrs = days * 24
                                            if len(split_d) > 1:
                                                if 'h' in split_d[1]:
                                                    split_h = split_d[1].split('h')
                                                    hrs += int(split_h[0])
                                                    if 'min' in split_d[1]:
                                                        mins = int(split_h[1].replace('min', ''))
                                                elif 'min' in split_d[1]:
                                                    mins = int(split_d[1].replace('min', ''))
                                        else:
                                            split_ = Effort[file_id].split('h')
                                            hrs = split_[0]
                                            if 'min' in Effort[file_id]:
                                                mins = split_[1].replace('min', '')
                                        delta = timedelta(hours=int(hrs), minutes=int(mins), seconds=0)
                                        total_seconds = delta.total_seconds()
                                        minutes = int(total_seconds // 60)
                                        total_effort += minutes
                                        val = minutes
                                    else:
                                        # print(Effort[file_id])
                                        hrs = 0
                                        mins = 0
                                        if 'd' in Effort[file_id]:
                                            splits_ = Effort[file_id].split('d')
                                            hrs = int(splits_[0]) * 24
                                            if len(splits_) > 1:
                                                if 'min' in splits_[1]:
                                                    mins = int(splits_[1].replace('min', ''))
                                                else:
                                                    hrs += int(splits_[1])
                                            delta = timedelta(hours=int(hrs), minutes=int(mins), seconds=0)
                                            total_seconds = delta.total_seconds()
                                            minutes = int(total_seconds // 60)
                                            total_effort += minutes
                                            val = minutes
                                        else:
                                            val = int(Effort[file_id].replace('min', ''))
                                        total_effort += val
                                    if Severity[file_id] in severity_dict.keys():
                                        value = severity_dict.get(Severity[file_id])
                                        value += val
                                        severity_dict[Severity[file_id]] = value
                                    else:
                                        severity_dict[Severity[file_id]] = val
                                    if Type[file_id] in type_dict.keys():
                                        type_val = type_dict.get(Type[file_id])
                                        type_val += val
                                        type_dict[Type[file_id]] = type_val
                                    else:
                                        type_dict[Type[file_id]] = val
                                    if Type[file_id] == 'BUG':
                                        List_bugs_1.append(val)
                                    elif Type[file_id] == 'CODE_SMELL':
                                        List_smells_1.append(val)
                                    elif Type[file_id] == 'VULNERABILITY':
                                        List_vulnerability_1.append(val)
                                    if Severity[file_id] == 'CRITICAL':
                                        List_critical_1.append(val)
                                    elif Severity[file_id] == 'MAJOR':
                                        List_major_1.append(val)
                                    elif Severity[file_id] == 'MINOR':
                                        List_minor_1.append(val)
                                    elif Severity[file_id] == 'BLOCKER':
                                        List_blocker_1.append(val)
                            # print(type_dict)
                            # print(severity_dict)
                            bugs = 0
                            smells = 0
                            vulnerability = 0
                            major = 0
                            critical = 0
                            minor = 0
                            blocker = 0
                            if 'BUG' in type_dict.keys():
                                bugs = type_dict.get('BUG')
                            if 'CODE_SMELL' in type_dict.keys():
                                smells = type_dict.get('CODE_SMELL')
                            if 'VULNERABILITY' in type_dict.keys():
                                vulnerability = type_dict.get('VULNERABILITY')
                            if 'CRITICAL' in severity_dict.keys():
                                critical = severity_dict.get('CRITICAL')
                            if 'MAJOR' in severity_dict.keys():
                                major = severity_dict.get('MAJOR')
                            if 'MINOR' in severity_dict.keys():
                                minor = severity_dict.get('MINOR')
                            if 'BLOCKER' in severity_dict.keys():
                                blocker = severity_dict.get('BLOCKER')

                            bugs_kloc = 0
                            smells_kloc = 0
                            vulnerability_kloc = 0
                            critical_kloc = 0
                            major_kloc = 0
                            minor_kloc = 0
                            blocker_kloc = 0

                            if cloc > 0:
                                list_bugs_repo.append(bugs / (cloc * 1000))
                                list_smells_repo.append(smells / (cloc * 1000))

                                list_critical_repo.append(critical / (cloc * 1000))
                                list_major_repo.append(major / (cloc * 1000))
                                list_minor_repo.append(minor / (cloc * 1000))
                                list_bloker_repo.append(blocker / (cloc * 1000))

                                List_bugs.append(bugs / (cloc * 1000))
                                List_smells.append(smells / (cloc * 1000))
                                List_vulnerability.append(vulnerability / (cloc * 1000))
                                List_critical.append(critical / (cloc * 1000))
                                List_major.append(major / (cloc * 1000))
                                List_minor.append(minor / (cloc * 1000))
                                List_blocker.append(blocker / (cloc * 1000))
                                List_cloc.append(cloc)
                    if len(list_bugs_repo) == 0:
                        list_bugs_repo.append(0)
                    if len(list_smells_repo) == 0:
                        list_smells_repo.append(0)
                    if len(list_critical_repo) == 0:
                        list_critical_repo.append(0)
                    if len(list_major_repo) == 0:
                        list_major_repo.append(0)
                    if len(list_minor_repo) == 0:
                        list_minor_repo.append(0)
                    if len(list_bloker_repo) == 0:
                        list_bloker_repo.append(0)

                    total_type_ = np.mean(list_bugs_repo) + np.mean(list_smells_repo)
                    total_severity_ = np.mean(list_critical_repo) + np.mean(list_major_repo)+ np.mean(list_minor_repo) + np.mean(list_bloker_repo)
                    perc_bugs = 0
                    perc_smells = 0
                    if total_type_ > 0:
                        perc_bugs = round((np.mean(list_bugs_repo)*100/total_type_),3)
                        perc_smells = round((np.mean(list_smells_repo) * 100 / total_type_), 3)
                    perc_critical = 0
                    perc_major = 0
                    perc_minor = 0
                    perc_bloker = 0
                    if total_type_ > 0:
                        perc_critical = round((np.mean(list_critical_repo) * 100 / total_severity_), 3)
                        perc_major = round((np.mean(list_major_repo) * 100 / total_severity_), 3)
                        perc_minor = round((np.mean(list_minor_repo) * 100 / total_severity_), 3)
                        perc_bloker = round((np.mean(list_bloker_repo) * 100 / total_severity_), 3)


                    ## Debt Type
                    data_writer_v2.writerow([cat, repos, 'Bug', np.mean(list_bugs_repo), total_type_, perc_bugs])
                    data_writer_v2.writerow([cat, repos, 'Smell', np.mean(list_smells_repo), total_type_, perc_smells])

                    ## Debt Severity
                    data_writer_v22.writerow([cat, repos, 'Critical', np.mean(list_critical_repo), total_severity_, perc_critical])
                    data_writer_v22.writerow([cat, repos, 'Major', np.mean(list_major_repo), total_severity_,  perc_major])
                    data_writer_v22.writerow([cat, repos, 'Minor', np.mean(list_minor_repo), total_severity_, perc_minor])
                    data_writer_v22.writerow([cat, repos, 'NBlocker', np.mean(list_bloker_repo), total_severity_, perc_bloker])

                else:
                    print("Not found --- ", path_snaps + repos + '_' + str(index_of) + '_snaps_v2.csv')
        if len(List_bugs) == 0:
            List_bugs.append(0)
        if len(List_smells) == 0:
            List_smells.append(0)
        if len(List_vulnerability) == 0:
            List_vulnerability.append(0)
        if len(List_critical) == 0:
            List_critical.append(0)
        if len(List_major) == 0:
            List_major.append(0)
        if len(List_minor) == 0:
            List_minor.append(0)
        if len(List_blocker) == 0:
            List_blocker.append(0)
        List_cloc = [x for x in List_cloc if str(x) != 'nan']
        if len(List_cloc) == 0:
            List_cloc.append(1)
        if np.sum(List_cloc) == 0:
            List_cloc.append(1)

        ## Debt Type
        total_type = np.sum(List_bugs)+np.sum(List_smells)
        for bug_i in List_bugs:
            row = [cat, 'Bugs', bug_i, total_type, round((bug_i*100/total_type), 3)]
            data_writer_1.writerow(row)
        for smell_i in List_smells:
            row = [cat, 'Smells', smell_i, total_type, round((smell_i*100/total_type), 3)]
            data_writer_1.writerow(row)
        #for vul_i in List_vulnerability:
        #    row = [cat, 'VULNERABILITY', vul_i]
        #    data_writer_1.writerow(row)
        ## Debt Severity
        total_severity = np.sum(List_critical) + np.sum(List_major)+ np.sum(List_minor) + np.sum(List_blocker)
        for critical_i in List_critical:
            row = [cat, 'Critical', critical_i, total_severity, round((critical_i*100/total_severity), 3)]
            data_writer_2.writerow(row)
        for major_i in List_major:
            row = [cat, 'Major', major_i, total_severity, round((major_i*100/total_severity), 3)]
            data_writer_2.writerow(row)

        for minor_i in List_minor:
            row = [cat, 'Minor', minor_i, total_severity, round((minor_i*100/total_severity), 3)]
            data_writer_2.writerow(row)
        for blocker_i in List_blocker:
            row = [cat, 'Blocker', blocker_i, total_severity, round((blocker_i*100/total_severity), 3)]
            data_writer_2.writerow(row)


data_file_1.close()
data_file_2.close()
data_file_v2.close()
data_file_v22.close()













