import pandas as pd
import csv
path = '/Volumes/Cisco/Fall2021/quantum-revision/Analysis/bugs/old/'
data_file = open(path + 'BugInducing-details_latest4.csv', mode='w',newline='', encoding='utf-8')
data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
data_writer.writerow(['project', 'Bugfixing', "Date", "Bugs", "issues",  'Buggy_issues','is_status', 'changedfiles', 'cloc', "TotalBugInducing", 'totalinducing2', 'BugInducing'])
proj_list = []
fixing_list = []
inducing_list = []
for i in [1,2,3,4,5]:
    df_data = pd.read_csv(path+'Bug-details_0{}.csv'.format(i))
    project = df_data.project.values.tolist()
    Bugfixing = df_data.Bugfixing.values.tolist()
    issues = df_data.issues.values.tolist()
    Email = df_data.Email.values.tolist()
    Date = df_data.Date.values.tolist()
    Bugs = df_data.Bugs.values.tolist()
    Commitmessage = df_data.Commitmessage.values.tolist()
    issues = df_data.issues.values.tolist()
    Buggy_issues = df_data.Buggy_issues.values.tolist()
    is_status = df_data.is_status.values.tolist()
    changedfiles = df_data.changedfiles.values.tolist()
    cloc = df_data.cloc.values.tolist()
    TotalBugInducing = df_data.TotalBugInducing.values.tolist()
    BugInducing = df_data.BugInducing.values.tolist()

    totalinducing2 = df_data.totalinducing2.values.tolist()
    
    for index in range(len(project)):
        if not project[index] in proj_list and not Bugfixing[index] in fixing_list and not BugInducing[index] in inducing_list:
            data_writer.writerow(
                [project[index], Bugfixing[index], Date[index], Bugs[index], issues[index], Buggy_issues[index], is_status[index], changedfiles[index], cloc[index],
                 TotalBugInducing[index], totalinducing2[index], BugInducing[index]])
            proj_list.append(project[index])
            fixing_list.append(Bugfixing[index])
            inducing_list.append(BugInducing[index])

data_file.close()