
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
from src.quantum_revision.utils.github import get_data, GitHubMeta

path_output = '/Volumes/Cisco/Fall2021/quantum-revision/Analysis/general/'
path_snaps = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/sonar-results/analysis/snapshots_v2/'

input_path = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/'

fixing_path = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/bugs2/inducing-fixing-dates/'
inducing_path = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/bugs2/inducing/'
file = 'repos.csv'
df_data = pd.read_csv(input_path + file)

Repos_Name = df_data.Repos_Name.values.tolist()
Created_at = df_data.Created_at.values.tolist()
age = df_data.age.values.tolist()
commits = df_data.commits.values.tolist()
releases = df_data.releases.values.tolist()
Size = df_data.Size.values.tolist()


file = 'category.csv'
df_data = pd.read_csv(input_path + file)
Repos_Name2 = df_data.Repos_Name.values.tolist()
Type = df_data.Type.values.tolist()
categories = set(Type)
ignore_cat = ['Fun/ Game', 'None-Quantum', 'Web-Extension'] # , 'Quantum-Chemistry', 'ToolKit', 'Assembly'

print(categories)
data_file = open(path_output + 'projects_general_statistics.csv', mode='w', newline='', encoding='utf-8')
data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
data_writer.writerow(['Category','PIndex','Age', 'commits', 'Size', 'releases'])
for cat in categories:
    if not cat in ignore_cat:
        print(cat)
        p_index = 0
        for repo_id in range(len(Repos_Name2)):
            if Type[repo_id] == cat:
                index = Repos_Name.index(Repos_Name2[repo_id])
                #data_writer.writerow([cat, p_index, age[index]])
                data_writer.writerow([cat, p_index, age[index], commits[index], Size[index], releases[index]])
                p_index += 1
data_file.close()
