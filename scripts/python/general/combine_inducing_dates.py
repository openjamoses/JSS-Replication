import pandas as pd
import csv

path = '/Volumes/Cisco/Fall2021/quantum-revision/Analysis/bugs/old/'
path_output = '/Volumes/Cisco/Fall2021/quantum-revision/Analysis/bugs/'
data_file = open(path_output + 'Inducing-combine_dates_latest.csv', mode='w', newline='', encoding='utf-8')
data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
data_writer.writerow(['project', 'BugInducing', "Date", "CLOC", "Files"])
count = 0
for i in ['',2]:
    df_data = pd.read_csv(path + 'Inducing-dates_latest{}.csv'.format(i))
    project = df_data.project.values.tolist()
    BugInducing = df_data.BugInducing.values.tolist()
    Date = df_data.Date.values.tolist()
    CLOC = df_data.CLOC.values.tolist()
    Files = df_data.Files.values.tolist()
    print(i, len(project))
    for index in range(len(project)):
        if str(project[index]) != 'nan':
            count += 1
            data_writer.writerow([project[index], BugInducing[index], Date[index], CLOC[index], Files[index]])
data_file.close()

print('total records: ', count)