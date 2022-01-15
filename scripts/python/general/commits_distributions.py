
from statistics import mean, median
import csv
import os
import datetime
from datetime import datetime as dt
from datetime import datetime, timedelta
import urllib.request
import json
#import seaborn as sns
import matplotlib
import pandas as pd
import os

import numpy as np
import pandas as pd# Plots
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

import pandas as pd

from src.quantum.codeanalyser.v2.TOKENS import get_tokens
from src.quantum_revision.utils.github import get_data

topic_path = "/Users/mosesopenja/Documents/summer2020/Quantum/v2/bugs2/messages/Topics/25/25-maps/"
path_output = '/Volumes/Cisco/Fall2021/quantum-revision/Analysis/general/plots/'
path_snaps = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/sonar-results/analysis/snapshots_v2/'

input_path = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/'

fixing_path = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/bugs2/inducing-fixing-dates/'
inducing_path = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/bugs2/inducing/'
file = 'repos.csv'
df_data = pd.read_csv(input_path + file)

Repos_Name = df_data.Repos_Name.values.tolist()
Created_at = df_data.Created_at.values.tolist()
updated_at = df_data.updated_at.values.tolist()


file = 'category.csv'
df_data = pd.read_csv(input_path + file)
Repos_Name2 = df_data.Repos_Name.values.tolist()
Type = df_data.Type.values.tolist()
categories = set(Type)

data_file = open(path_output + 'repos_commits_interval_metrics.csv', mode='w', newline='', encoding='utf-8')
data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
data_writer.writerow(["categories",'repos','repo_id', "interval","commits"])
def date_diff(date1, date2):

    #print(date1, date2)
    date1 = date1.replace('T', ' ')
    date1 = date1.replace('Z', '')

    date2 = date2.replace('T', ' ')
    date2 = date2.replace('Z', '')
    d1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
    d2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')
    return (d2 - d1).total_seconds() / (60 * 60)
def addDate(date, day):
    date = datetime.strptime(date, "%Y-%m-%d")
    modified_date = date + timedelta(days=day)
    return datetime.strftime(modified_date, "%Y-%m-%d")
def compare_dates(date1, date2):
    a = dt.strptime(date1, "%Y-%m-%d")
    b = dt.strptime(date2, "%Y-%m-%d")
    if b >= a:
        return True
    else:
        return False
def getResponse(url):
    try:
        operUrl = urllib.request.urlopen(url)
        if(operUrl.getcode()==200):
            data = operUrl.read()
            jsonData = json.loads(data)
        else:
            print("Error receiving data", operUrl.getcode())
        return jsonData
    except:
        return None
        pass
ct = 0
ignore_cat = ['Fun/ Game', 'None-Quantum', 'Web-Extension'] # , 'Quantum-Chemistry', 'ToolKit', 'Assembly'
data_all = {}

i_count = 0
count_index = 0
list_cat_ = []
#sns.set_style("darkgrid")

print(categories)
for cat in categories:
    if not cat in ignore_cat:
        print(cat)
        data_all[cat] = {}
        i_count += 1

        dict_dates_vals2 = {}
        list_cat_.append(cat)

        num = 0
        id_ = 0
        for repo_id in range(len(Repos_Name2)):
            if Type[repo_id] == cat:
                num += 2
                index = Repos_Name.index(Repos_Name2[repo_id])
                days = date_diff(Created_at[index], updated_at[index])

                proj_added = 0
                proj_removed = 0
                proj_commits = 0

                proj_added_snaps = ''
                proj_removed_snaps = ''

                snap_added = 0
                snap_removed = 0

                snap_index = 0
                count_commits = 0
                date_from = updated_at[index][:10]
                date_30 = addDate(updated_at[index][:10], -30)
                date_60 = addDate(updated_at[index][:10], -60)
                date_90 = addDate(updated_at[index][:10], -90)
                date_120 = addDate(updated_at[index][:10], -120)
                date_150 = addDate(updated_at[index][:10], -150)
                date_180 = addDate(updated_at[index][:10], -180)
                #date_210 = addDate(updated_at[index][:10], -210)

                dict_dates = {}
                dict_dates[30] = date_from+'/'+date_30
                dict_dates[60] = date_from + '/' + date_60
                dict_dates[90] = date_from + '/' + date_90
                dict_dates[120] = date_from + '/' + date_120
                dict_dates[150] = date_from + '/' + date_150
                dict_dates[180] = date_from + '/' + date_180
                #dict_dates[210] = date_from + '/' + date_210

                dict_dates_vals = {}

                print()
                p = 1
                while True:
                    if ct == len(get_tokens()):
                        ct = 0
                    url2 = 'https://api.github.com/repos/' + Repos_Name[index] + '/commits?page=' + str(p) + '&per_page=100'
                    commit_obj, ct = get_data(url2, ct)  # GitHub(url2, self.ct).getResponse()
                    p += 1
                    if commit_obj != None:
                        if len(commit_obj) == 0:
                            break
                        count_commits += len(commit_obj)
                        if count_commits % 500 == 0:
                            print(' --- {}' + format(count_commits))
                        ct += 1
                        p += 1
                        date_print = ''
                        for obj in commit_obj:
                            shaa = obj['sha']
                            date = obj['commit']['author']['date']
                            date_print = date

                            for key, val in dict_dates.items():
                                d_from = val.split('/')[0]
                                d_to = val.split('/')[1]
                                if compare_dates(d_to, date[:10]) and compare_dates(date[:10], d_from):
                                    if key in dict_dates_vals.keys():
                                        dict_dates_vals[key] += 1
                                    else:
                                        dict_dates_vals[key] = 1
                                elif compare_dates(date[:10], d_to):

                                    d_from = addDate(d_to, -1)
                                    d_to = addDate(d_from, -key)

                                    dict_dates[key] = d_from + '/' + d_to
                                    if key in dict_dates_vals2.keys():
                                        if key in dict_dates_vals.keys():
                                            dict_dates_vals2[key].append(dict_dates_vals.get(key))
                                        else:
                                            dict_dates_vals2[key] = [0]
                                    else:
                                        if key in dict_dates_vals.keys():
                                            dict_dates_vals2[key] = [dict_dates_vals.get(key)]
                                        else:
                                            dict_dates_vals2[key] = [0]

                                    # print(date, val)
                                    if compare_dates(d_to, date[:10]) and compare_dates(date[:10], d_from):
                                        if key in dict_dates_vals.keys():
                                            dict_dates_vals[key] += 1
                                        else:
                                            dict_dates_vals[key] = 1
                    else:
                        break

        if 30 in dict_dates_vals2.keys():
            data_all[cat][30] = dict_dates_vals2.get(30)
        if 60 in dict_dates_vals2.keys():
            data_all[cat][60] = dict_dates_vals2.get(60)
        if 90 in dict_dates_vals2.keys():
            data_all[cat][90] = dict_dates_vals2.get(90)
        if 120 in dict_dates_vals2.keys():
            data_all[cat][120] = dict_dates_vals2.get(120)
        if 150 in dict_dates_vals2.keys():
            data_all[cat][150] = dict_dates_vals2.get(150)
        if 180 in dict_dates_vals2.keys():
            data_all[cat][180] = dict_dates_vals2.get(180)
        for key, val in  dict_dates_vals2.items():
            for val2 in val:
                data_writer.writerow([cat, key, str(val2)+'D'])

#for key, val in data_all.items():
#    for key2, val2 in val.items():
#        for v in val2:
#            data_writer.writerow([key, key2, val2])

data_file.close()



