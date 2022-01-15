import pandas as pd
import csv
input_path = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/'
path = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/snapshots/LOC/'
df_data = pd.read_csv(path + 'Repos_LOC__snaps_001.csv')
project = df_data.project.values.tolist()
snap_added = df_data.snap_added.values.tolist()
snap_removed = df_data.snap_removed.values.tolist()

exclude_categories = ['None-Quantum','Web-Extension', 'Fun/ Game']

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
path_inducing = '/Volumes/Cisco/Fall2021/quantum-revision/Analysis/bugs/'
data_file = open(path_inducing + 'snapshots_loc.csv', mode='w', newline='', encoding='utf-8')
data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
data_writer.writerow(["Category", 'ProjectId', 'snapshot','CLOC', 'addedLOC', 'removedLOC'])

#for cat in set(Type_):
#    if not cat in exclude_categories:
#        total_projects = 0
for i in range(len(project)):
    if project[i] in Repos_Name_2 :
        index2 = Repos_Name_2.index(project[i])
        cat2 =  Type_[index2]
        if not cat2 in exclude_categories: # and cat == cat2 and total_projects < 10:
            split_added = str(snap_added[i]).split('/')
            split_removed = str(snap_removed[i]).split('/')
            for j in range(len(split_added)):
                if split_added[j].isnumeric() and j < 10:
                    #print(split_added[j], split_removed[j])
                    data_writer.writerow([cat2, project[i], j,(int(split_added[j])+int(split_removed[j]))/1000, int(split_added[j])/1000, int(split_removed[j])/1000])
            #total_projects += 1
data_file.close()
