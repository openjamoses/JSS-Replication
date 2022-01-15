import ast
import os
from datetime import timedelta

import pandas as pd
import csv
import numpy as np
import collections
from numpy import std, mean

path_loc = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/snapshots/LOC/'
input_path = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/'
report_path = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/sonar-results/analysis/snapshots_v2/'
report_path_debt = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/sonar-results/analysis/summery2/'

output_path = '/Volumes/Cisco/Fall2021/quantum-revision/Analysis/RQ3/regression-cleaned2/'
path_file = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/snapshots/file-histroy/'

path_bugs = '/Volumes/Cisco/Fall2021/quantum-revision/Analysis/bugs/old/'

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


from datetime import datetime as dt
from datetime import datetime, timedelta
def compare_dates(date1, date2):
    a = dt.strptime(date1, "%Y-%m-%d")
    b = dt.strptime(date2, "%Y-%m-%d")
    if b >= a:
        return True
    else:
        return False

xl2 = pd.ExcelFile(report_path_debt + 'smells-sort.xlsx')
df_data2 = xl2.parse('smells')
smells_rule = df_data2.rule.values.tolist()
smells_Tags = df_data2.Tags.values.tolist()
smells_mgs = df_data2.message.values.tolist()


df_data2 = xl2.parse('bugs')
bugs_rule = df_data2.rule.values.tolist()
bugs_Tags = df_data2.Tags.values.tolist()
bugs_mgs = df_data2.message.values.tolist()

tag_rule_split = []
tags_lists = []
for val_id in range(len(bugs_rule)):
    splits = str(bugs_Tags[val_id]).split(' ')
    for sp in splits:
        #bug_set.add(sp)
        if not sp is np.nan and len((sp))>0 and str(sp) != 'nan':
            tag = bugs_rule[val_id].split(':')[1]
            tag_rule_split.append(tag)
            tags_lists.append(sp.replace('-','_'))

#smells_set = set()
for val_id in range(len(smells_rule)):
    splits = str(smells_Tags[val_id]).split(' ')
    for sp in splits:
        #smells_set.add(sp)
        if not sp is np.nan and len((sp))>0 and str(sp) != 'nan':
            #print(smells_rule[val_id])
            tag = smells_rule[val_id].split(':')[1]
            tag_rule_split.append(tag)
            tags_lists.append(sp.replace('-','_'))

tags_sets = set(tags_lists)
#print(len(tag_rule_split),tag_rule_split)
#print(len(tags_lists),tags_lists)

df_data = pd.read_csv(report_path_debt + 'bugs.csv')
filepath_bugs = df_data.filepath.values.tolist()
rule_bugs = df_data.rule.values.tolist()
Project_bugs = df_data.Project.values.tolist()
snapshot_bugs = df_data.snapshot.values.tolist()
effort_bugs = df_data.effort.values.tolist()
severity_bugs = df_data.severity.values.tolist()


data_file2 = open(output_path + 'debt_files_details_tags_.csv', mode='w', newline='', encoding='utf-8')
data_writer2 = csv.writer(data_file2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
rows = ["Category", 'project', 'snapshot_id', 'FileId', 'total_debt',
                'total_effort', 'bug_inducing', "bug_fixing",'inducing_loc', 'fixing_loc','total_loc','sonar_loc', 'is_inducing', 'is_debt', 'ERROR', 'CODE_SMELL','is_erroneous','is_smelly', 'MAJOR',
                'CRITICAL', 'MINOR', 'BLOCKER']

for tag in tags_sets:
    rows.append(tag)
data_writer2.writerow(rows)

df_data2 = pd.read_csv(path_bugs + 'BugInducing-details_combined_latest.csv')
bug_project = df_data2.project.values.tolist()
Bugfixing = df_data2.Bugfixing.values.tolist()
Date = df_data2.Date.values.tolist()
changedfiles = df_data2.changedfiles.values.tolist()
BugInducing = df_data2.BugInducing.values.tolist()
report_path = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/sonar-results/report/xlsx/'
report_path3 = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/sonar-results/report/xlsx2/'
path_snaps = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/snapshots/all/'
path_general = '/Volumes/Cisco/Fall2021/quantum-revision/Analysis/general/'
path_inducing = '/Volumes/Cisco/Fall2021/quantum-revision/Analysis/bugs/'

df_data = pd.read_excel(open(input_path + file, 'rb'),  sheet_name='category')
categories = set(Type_)
exclude_categories = ['None-Quantum','Web-Extension', 'Fun/ Game']
for cat in categories:
    if not cat in exclude_categories:
        cat_str = cat
        if '/' in cat:
            cat_str = str(cat).replace('/', '_')
        data_file = open(output_path + 'debt_files_details_tags_{}.csv'.format(cat_str), mode='w', newline='', encoding='utf-8')
        data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        rows = ["Category", 'project', 'snapshot_id', 'FileId', 'total_debt',
                'total_effort', 'bug_inducing', "bug_fixing",'inducing_loc', 'fixing_loc','total_loc','sonar_loc', 'is_inducing', 'is_debt', 'ERROR', 'CODE_SMELL','is_erroneous','is_smelly', 'MAJOR',
                'CRITICAL', 'MINOR', 'BLOCKER']
        for tag in tags_sets:
            rows.append(tag)
        data_writer.writerow(rows)


        for index in range(len(Repos_Name)):
            if str(file_name[index]) != 'nan' and Repos_Name[index] in Repos_Name_2:
                repos = Repos_Name[index].split('/')[1]
                category = Type_[Repos_Name_2.index(Repos_Name[index])]
                if cat == category:

                    print(index, Repos_Name[index])
                    index_of = index

                    df_dates = pd.read_csv(path_general+'snapshots_dates.csv')
                    snapshot_Repos = df_dates.Repos.values.tolist()
                    snapshot_id = df_dates.snapshot_id.values.tolist()
                    snapshot_date = df_dates.snapshot_date.values.tolist()
                    snapshot_Hash = df_dates.Hash.values.tolist()
                    if Repos_Name[index] in snapshot_Repos:
                        #df_data = pd.read_csv(path_snaps + repos + '_' + str(index_of) + '_snaps_v2.csv')
                        #snapshots = df_data.snapshots.values.tolist()
                        snap_date_list = []
                        #snap_hash_list = []
                        for i in range(len(snapshot_Repos)):
                            if Repos_Name[index] == snapshot_Repos[i]:
                                snap_date_list.append(snapshot_date[i])
                        # if os.path.exists(input_path + file_name[index_of]+'.xlsx'):
                        xl1 = pd.ExcelFile(report_path + file_name[index_of] + '.xlsx')
                        df_Issues = xl1.parse('Issues')
                        Rule = df_Issues.Rule.values.tolist()
                        Type = df_Issues.Type.values.tolist()
                        Severity = df_Issues.Severity.tolist()
                        File = df_Issues.File.tolist()
                        Effort = df_Issues.Effort.tolist()

                        print(repos, index_of)

                        total_effort_dict_all = {}
                        total_debts_dict_all = {}
                        severity_dict_all = {}
                        severity_counts_dict_all = {}
                        type_dict_all = {}
                        type_count_dict_all = {}
                        rule_count_dict_all = {}

                        inducing_data_dict_all = {}
                        fixing_data_dict_all = {}
                        inducing_data_dict_counts_all = {}
                        fixing_data_dict_counts_all = {}
                        sonar_loc_dict_all = {}

                        for snap_id in range(len(snap_date_list)):
                            cloc = 0
                            total_effort_dict = {}
                            total_debts_dict = {}
                            severity_dict = {}
                            severity_counts_dict = {}
                            type_dict = {}
                            type_count_dict = {}

                            rule_count_dict = {}

                            sonar_loc_dict = {}

                            if len(File) > 0:
                                xl2 = pd.ExcelFile(report_path3 + file_name[index_of] + '.xlsx')
                                df_Metrics = xl2.parse('Metrics')
                                # df_Metrics = xl1.parse('Metrics')
                                Path = df_Metrics.Path.values.tolist()
                                ncloc = df_Metrics.ncloc.tolist()
                                for file_id in range(len(File)):
                                    fileShaps = File[file_id][File[file_id].index(':') + 1:]
                                    if file_name[index_of] + '/' + repos + '_' + str(snap_id) in fileShaps:
                                        path_index = Path.index(fileShaps)
                                        # print(path_index)
                                        cloc += ncloc[path_index]

                                        if fileShaps in sonar_loc_dict.keys():
                                            sonar_loc_dict[fileShaps] += ncloc[path_index]
                                        else:
                                            sonar_loc_dict[fileShaps] = ncloc[path_index]
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
                                            #total_effort += minutes
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
                                                #total_effort += minutes
                                                val = minutes
                                            else:
                                                val = int(Effort[file_id].replace('min', ''))
                                            #total_effort += val
                                        if fileShaps in total_effort_dict.keys():
                                            total_effort_dict[fileShaps] += val
                                        else:
                                            total_effort_dict[fileShaps] = val

                                        if fileShaps in total_debts_dict.keys():
                                            total_debts_dict[fileShaps] += 1
                                        else:
                                            total_debts_dict[fileShaps] = 1
                                        ## Severity efforts
                                        if Severity[file_id] in severity_dict.keys():
                                            if Severity[file_id] in severity_dict.get(fileShaps).keys():
                                                severity_dict[str(fileShaps)][Severity[file_id]] += val
                                            else:
                                                severity_dict[str(fileShaps)][Severity[file_id]] = val
                                        else:
                                            severity_dict[str(fileShaps)] = {}
                                            severity_dict[str(fileShaps)][Severity[file_id]] = val

                                        ## Severity counts
                                        if Severity[file_id] in severity_counts_dict.keys():
                                            if Severity[file_id] in severity_counts_dict.get(fileShaps).keys():
                                                severity_counts_dict[str(fileShaps)][Severity[file_id]] += 1
                                            else:
                                                severity_counts_dict[str(fileShaps)][Severity[file_id]] = 1
                                        else:
                                            severity_counts_dict[str(fileShaps)] = {}
                                            severity_counts_dict[str(fileShaps)][Severity[file_id]] = 1

                                        ## Type Efforts
                                        if fileShaps in type_dict.keys():
                                            if Type[file_id] in type_dict.get(fileShaps).keys():
                                                type_dict[str(fileShaps)][Type[file_id]] += val
                                            else:
                                                type_dict[str(fileShaps)][Type[file_id]] = val
                                        else:
                                            type_dict[str(fileShaps)] = {}
                                            type_dict[str(fileShaps)][Type[file_id]] = val

                                        ## Type counts
                                        if fileShaps in type_count_dict.keys():
                                            if Type[file_id] in type_count_dict.get(fileShaps).keys():
                                                type_count_dict[str(fileShaps)][Type[file_id]] += 1
                                            else:
                                                type_count_dict[str(fileShaps)][Type[file_id]] = 1
                                        else:
                                            type_count_dict[str(fileShaps)] = {}
                                            type_count_dict[str(fileShaps)][Type[file_id]] = 1

                                        ## type_dict
                                        rule_str = str(Rule[file_id]).split(':')[1]
                                        if rule_str in tag_rule_split:
                                            tag_name = tags_lists[tag_rule_split.index(rule_str)]
                                            if fileShaps in rule_count_dict.keys():
                                                if tag_name in rule_count_dict.get(str(fileShaps)).keys():
                                                    rule_count_dict[fileShaps][tag_name] += 1
                                                else:
                                                    rule_count_dict[fileShaps][tag_name] = 1
                                            else:
                                                rule_count_dict[fileShaps] = {}
                                                rule_count_dict[fileShaps][tag_name] = 1
                            total_effort_dict_all[snap_id] = total_effort_dict
                            total_debts_dict_all[snap_id] = total_debts_dict
                            severity_dict_all[snap_id] = severity_dict
                            severity_counts_dict_all[snap_id] = severity_counts_dict
                            type_dict_all[snap_id] = type_dict
                            type_count_dict_all[snap_id] = type_count_dict
                            rule_count_dict_all[snap_id] = rule_count_dict
                            sonar_loc_dict_all[snap_id] = sonar_loc_dict


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
                            fixing_changedfiles= df_fixing.changedfiles.values.tolist()
                            fixing_cloc = df_fixing.cloc.values.tolist()

                            snap_to = ''
                            if snap_id < len(snap_date_list)-1:
                                snap_to = snap_date_list[snap_id+1]
                            inducing_data_dict = {}
                            fixing_data_dict = {}

                            inducing_data_dict_counts = {}
                            fixing_data_dict_counts = {}
                            for x in range(len(inducing_project)):
                                if Repos_Name[index] == inducing_project[x]:
                                    if snap_to != '':
                                        if compare_dates(snap_date_list[snap_id], str(inducing_Date[x])[:10]) and compare_dates(str(inducing_Date[x])[:10], snap_to):
                                            try:
                                                data_json = ast.literal_eval(str(inducing_Files[x]))
                                                for key, val in data_json.items():
                                                    if key in inducing_data_dict.keys():
                                                        inducing_data_dict[key] += val
                                                        inducing_data_dict_counts[key] += 1
                                                    else:
                                                        inducing_data_dict[key] = val
                                                        inducing_data_dict_counts[key] = 1
                                            except Exception as e:
                                                print(e)
                                    else:
                                        if compare_dates(snap_date_list[snap_id], str(inducing_Date[x])[:10]):
                                            try:
                                                data_json = ast.literal_eval(str(inducing_Files[x]))
                                                for key, val in data_json.items():
                                                    if key in inducing_data_dict.keys():
                                                        inducing_data_dict[key] += val
                                                        inducing_data_dict_counts[key] += 1
                                                    else:
                                                        inducing_data_dict[key] = val
                                                        inducing_data_dict_counts[key] = 1
                                            except Exception as e:
                                                print(e)

                            for x in range(len(fixing_project)):
                                if Repos_Name[index] == fixing_project[x]:
                                    if snap_to != '':
                                        if compare_dates(snap_date_list[snap_id], str(fixing_Date[x])[:10]) and compare_dates(
                                                str(fixing_Date[x])[:10], snap_to):
                                            try:
                                                data_list = ast.literal_eval(str(fixing_changedfiles[x]))
                                                cloc_list = ast.literal_eval(str(fixing_cloc[x]))
                                                for ii in range(len(data_list)):
                                                    if data_list[ii] in fixing_data_dict.keys():
                                                        fixing_data_dict[data_list[ii]] += cloc_list[ii]
                                                        fixing_data_dict_counts[data_list[ii]] += 1
                                                    else:
                                                        fixing_data_dict[data_list[ii]] = cloc_list[ii]
                                                        fixing_data_dict_counts[data_list[ii]] = 1

                                            except Exception as e:
                                                print(e)
                                    else:
                                        if compare_dates(snap_date_list[snap_id], str(fixing_Date[x])[:10]):
                                            try:
                                                data_list = ast.literal_eval(str(fixing_changedfiles[x]))
                                                cloc_list = ast.literal_eval(str(fixing_cloc[x]))
                                                for ii in range(len(data_list)):
                                                    if data_list[ii] in fixing_data_dict.keys():
                                                        fixing_data_dict[data_list[ii]] += cloc_list[ii]
                                                        fixing_data_dict_counts[data_list[ii]] += 1
                                                    else:
                                                        fixing_data_dict[data_list[ii]] = cloc_list[ii]
                                                        fixing_data_dict_counts[data_list[ii]] = 1

                                            except Exception as e:
                                                print(e)
                            inducing_data_dict_all[snap_id] = inducing_data_dict
                            fixing_data_dict_all[snap_id] = fixing_data_dict

                            inducing_data_dict_counts_all[snap_id] = inducing_data_dict_counts
                            fixing_data_dict_counts_all[snap_id] = fixing_data_dict_counts


                        if os.path.exists(path_file + repos + '_' + str(index) + '.csv'):

                            df_data = pd.read_csv(path_file + repos + '_' + str(index) + '.csv')
                            FileName_ = df_data.FileName.values.tolist()
                            Added_ = df_data.Added.values.tolist()
                            Removed_ = df_data.Removed.values.tolist()
                            Id_ = df_data.Id.values.tolist()

                            Id = []
                            FileName = []
                            Added = []
                            Removed = []

                            for a in range(len(FileName_)):
                                file_str = str(FileName_[a]).lower() #and not 'test' in file_str
                                if not 'readme' in file_str and not 'doc' in file_str  \
                                        and not'.png' in file_str \
                                        and not '.pdf' in file_str and not '.jpeg' in file_str\
                                        and not '.jpg' in file_str and not '.gif' in file_str \
                                        and not 'license' in file_str and not 'makefile' in file_str\
                                        and not '.txt' in file_str and not '.md' in file_str and not 'cmake' in file_str \
                                        and not '.git' in file_str and not '.yml' in file_str and not '.json' in file_str \
                                        and not '.rst' in file_str and not 'changelog' in file_str and not '.bib' in file_str \
                                        and not 'tox.' in file_str:
                                    Id.append(Id_[a])
                                    FileName.append(FileName_[a])
                                    Added.append(Added_[a])
                                    Removed.append(Removed_[a])
                            print('  ---- prevoius files: ',len(FileName_), 'current files: ', len(FileName) )

                            Id_unique = set(Id)
                            for ID in Id_unique:
                                BUG = 0
                                CODE_SMELL = 0
                                MAJOR = 0
                                CRITICAL = 0
                                MINOR = 0
                                BLOCKER = 0
                                effort = 0
                                debts = 0
                                inducing = 0
                                fixing = 0

                                inducing_loc = 0
                                fixing_loc = 0

                                cloc = 0
                                modified = 0
                                sonar_loc = 0

                                tag_rules_dict = {}

                                list_of_files = []

                                tag_data_dict = {}

                                rows = ["Category", 'project','snapshot_id', 'FileId', 'total_debt',
                                        'total_effort', 'bug_inducing', "bug_fixing", 'is_inducing','is_debt', 'ERROR','CODE_SMELL', 'MAJOR', 'CRITICAL', 'MINOR', 'BLOCKER']

                                for i in range(len(Id)):
                                    # Bugs
                                    if Id[i] == ID:

                                        cloc += Added[i] + Removed[i]
                                        #modified += modifications[i]
                                        list_of_files.append(FileName[i])
                                for snap_id in range(len(snap_date_list)):
                                    for file_ in list_of_files:
                                        file_ = str(file_)
                                        if file_ in inducing_data_dict_all.get(snap_id).keys():
                                            inducing_loc += inducing_data_dict_all[snap_id][file_]
                                            inducing += inducing_data_dict_counts_all[snap_id][file_]
                                        if file_ in fixing_data_dict_all.get(snap_id).keys():
                                            fixing_loc += fixing_data_dict_all[snap_id][file_]
                                            fixing += fixing_data_dict_counts_all[snap_id][file_]
                                        for key, val in total_effort_dict_all.get(snap_id).items():
                                            if file_ in str(key):
                                                effort += val
                                        for key, val in total_debts_dict_all.get(snap_id).items():
                                            if file_ in str(key):
                                                debts += val
                                        for key, val in severity_counts_dict_all.get(snap_id).items():
                                            if file_ in str(key):
                                                if 'MAJOR' in val.keys():
                                                    MAJOR += severity_counts_dict_all[snap_id][key]['MAJOR']
                                                if 'CRITICAL' in val.keys():
                                                    CRITICAL += severity_counts_dict_all[snap_id][key]['CRITICAL']
                                                if 'MINOR' in val.keys():
                                                    MINOR += severity_counts_dict_all[snap_id][key]['MINOR']
                                                if 'BLOCKER' in val.keys():
                                                    BLOCKER += severity_counts_dict_all[snap_id][key]['BLOCKER']
                                        for key, val in type_count_dict_all.get(snap_id).items():
                                            if file_ in str(key):
                                                if 'BUG' in val.keys():
                                                    BUG += type_count_dict_all[snap_id][key]['BUG']
                                                if 'CODE_SMELL' in val.keys():
                                                    CODE_SMELL += type_count_dict_all[snap_id][key]['CODE_SMELL']
                                        for key, val in rule_count_dict_all.get(snap_id).items():
                                            if file_ in str(key):
                                                for key2, val2 in val.items():
                                                    if key2 in tag_data_dict.keys():
                                                        tag_data_dict[key2] += rule_count_dict_all[snap_id][key][key2]
                                                    else:
                                                        tag_data_dict[key2] = rule_count_dict_all[snap_id][key][
                                                            key2]
                                        for key, val in sonar_loc_dict_all.get(snap_id).items():
                                            if file_ in str(key):
                                                sonar_loc += sonar_loc_dict_all[snap_id][key]

                                is_inducing = 0
                                is_debt = 0
                                is_smelly = 0
                                is_erroneous = 0
                                if inducing > 0:
                                    is_inducing = 1
                                if debts > 0:
                                    is_debt = 1
                                if BUG > 0:
                                    is_erroneous = 1
                                if CODE_SMELL > 0:
                                    is_smelly = 1

                                rows = [cat, Repos_Name[index], snap_id,ID, debts,
                                        effort, inducing, fixing, inducing_loc, fixing_loc,
                                        cloc, sonar_loc, is_inducing, is_debt, BUG, CODE_SMELL, is_erroneous, is_smelly,
                                        MAJOR,CRITICAL, MINOR, BLOCKER]
                                for tag in tags_sets:
                                    val = 0
                                    if tag in tag_data_dict.keys():
                                        val = tag_data_dict.get(tag)
                                    rows.append(val)
                                data_writer.writerow(rows)
                                data_writer2.writerow(rows)


        data_file.close()
data_file2.close()
