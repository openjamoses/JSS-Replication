import os
import subprocess
import pandas as pd
import time

def move_file(report_path,report_path_new):
    git_log_command = "mv "+report_path+" "+report_path_new+""
    # print(git_log_command)
    p = subprocess.Popen(git_log_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = []
    for line in p.stdout.readlines():
        output.append(str(line))
    retval = p.wait()
    if retval == 0:
        print(" -- Extracted and moved")
def report_command(report_path,report_path_new, projectKey):
    os.chdir(report_path)
    git_log_command = "java -jar sonar-cnes-report-3.2.2.jar -t cd9cd41c9576d0c33bb0d323b8c566a144f4ed8d  -s http://localhost:9000/ -p "+projectKey+" -r ./template.csv"
    # print(git_log_command)
    print("Extracting sonar report for  :{}".format(projectKey))
    p = subprocess.Popen(git_log_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = []
    for line in p.stdout.readlines():
        output.append(str(line))
    retval = p.wait()
    if retval == 0:
        #rename the report here:
        for folder in os.listdir(report_path):
            full_path = str(report_path) + "/" + str(folder)
            if os.path.exists(full_path):
                if 'report.csv'  in str(folder):
                    #os.rename(folder, projectKey+".csv")
                    move_file(report_path+folder,report_path_new+"csv/"+projectKey+".csv" )
                if 'report.xlsx'  in str(folder):
                    #os.rename(folder, projectKey+".xlsx")
                    move_file(report_path+folder, report_path_new +"xlsx/"+ projectKey + ".xlsx")
                if 'report.md'  in str(folder):
                    #os.rename(folder, projectKey+".xlsx")
                    move_file(report_path+folder, report_path_new +"others/"+ projectKey + ".md")
                if 'report.docx'  in str(folder):
                    #os.rename(folder, projectKey+".xlsx")
                    move_file(report_path+folder, report_path_new +"others/"+ projectKey + ".docx")
        #print("Report extracted successfully!")
    else:
        print("Error in commit log extraction!")
        print(output)
    return output
def run_sonar_scanner(path, projectKey, language):
    os.chdir(path)
    path_repos_properties = path+"sonar-project.properties"
    trainingStream = open(path_repos_properties, 'w')
    if language == '':
        trainingStream.write('sonar.projectKey=' + projectKey + '\n' \
                             'sonar.projectName=' + projectKey + '\n' \
                             'sonar.projectVersion=1.0\n' \
                              'sonar.sources=./\n'\
                              'sonar.exclusions=**/*.java\n'\
                               'sonar.login=admin\n'\
                               'sonar.password=bright\n'\
                              'sonar.sourceEncoding=UTF-8')
    elif 'C' in language:
        trainingStream.write('sonar.projectKey=' + projectKey + '\n' \
                              'sonar.projectName=' + projectKey + '\n' \
                              'sonar.projectVersion=1.1\n' \
                               'sonar.cxx.gcc.reportPath=*.log\n' \
                               'sonar.cxx.gcc.charset=UTF-8\n' \
                                'sonar.language=C++\n' \
                                'sonar.login=admin\n'\
                                'sonar.password=bright\n'\
                                'sonar.cpp.file.suffixes=.cc,.cpp,.cxx,.c++,.hh,.hpp,.hxx,.h++,.ipp,.c,.h\n'\
                                'sonar.sources=./\n' \
                                 'sonar.exclusions=**/*.java\n'\
                                'sonar.sourceEncoding=UTF-8')
    else:
        trainingStream.write('sonar.projectKey=' + projectKey + '\n' \
                              'sonar.projectName=' + projectKey + '\n' \
                              'sonar.projectVersion=1.0\n' \
                             'sonar.sources=./\n' \
                             'sonar.language=' + language + '\n' \
                              'sonar.exclusions=**/*.java\n'\
                              'sonar.login=admin\n'\
                              'sonar.password=bright\n'\
                             'sonar.sourceEncoding=UTF-8')

    trainingStream.close()
    git_log_command = "sonar-scanner"
    # print(git_log_command)
    print("Executing sonar scanner on  :{}".format(projectKey))
    p = subprocess.Popen(git_log_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = []
    for line in p.stdout.readlines():
        output.append(str(line))
    retval = p.wait()
    if retval == 0:
        print("  -- Execution successfull!")
def main_report():
    report_path = '/Users/mosesopenja/Documents/summer2020/Quantum/new-collection/report-plugin/'
    report_path_new = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/sonar-results/report/'
    input_path = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/'
    file = 'MLRepos_Quantum_non_quantum.xlsx'
    xl1 = pd.ExcelFile(input_path + file)
    df_data = xl1.parse('quant_non_quantum')
    # Convert to list
    Repos_Name = df_data.Repos_Name.values.tolist()
    Language = df_data.Language.values.tolist()
    #status = df_data.status.values.tolist()
    list_type = ['C++', 'C']
    for index in range(194, len(Repos_Name)):
        list_type = ['C++', 'C']
        #if Language[index] in list_type:
        project = str(Repos_Name[index]).split('/')[1] + "_" + str(index) + "_snapshots"
        #project = str(Repos_Name[index]).split('/')[1]+"_snapshots" #+ "_snapshots"
        report_command(report_path, report_path_new, project)
        time.sleep(5)
def main_scanner():
    #report_path = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/snapshots/others/'
    #input_path = '/Users/mosesopenja/Documents/summer2020/Quantum/v2/'
    #file = 'MLRepos_Quantum_non_quantum.xlsx'
    path_snaps = '/Volumes/Cisco/Fall2021/Businge/v2/sonarqube/clone-variants/'
    #xl1 = pd.ExcelFile(input_path + file)
    #path = '/Users/mosesopenja/Documents/summer2021/Businge/New2021/'
    path = '/Volumes/Cisco/Fall2021/Businge/v2/'
    #df_data = xl1.parse('quant_non_quantum')
    #df_data = pd.read_csv(input_path + "Selected_Quantum_Repos.csv")
    # Convert to list
    df_data = pd.read_csv(path + '0families_npm_divergency.csv')
    #df_data2 = pd.read_csv(path + 'variants_dataset_13.csv')
    mainline = df_data.mainline.values.tolist()
    variant = df_data.variant.values.tolist()

    exclude_categories = ['maven', 'Rubygems', 'cargo', 'PlatformIO', 'CocoaPods', 'nuget', 'Clojars', 'Hex', 'Atom', 'Puppet', 'Carthage', 'pub']

    #mainline2 = df_data2.mainline.values.tolist()
    #variant2 = df_data2.variant.values.tolist()
    #ecosystem = df_data2.ecosystem.values.tolist()

    scanned_list = []

    divergency_date = df_data.divergency_date.values.tolist()
    least_date = df_data.least_date.values.tolist()
    repo_target_path_root = "/Users/mosesopenja/Documents/summer2021/Businge/New2021/clone2"
    # id_list = [187, 148, 139]
    #print(len(mainline))
    for index in range(len(variant)):
        repo = variant[index]
        if not repo in scanned_list:
            language = ''
            #if variant[index] in variant2:
            #    language = '' #ecosystem[variant2.index(variant[index])]
            project = str(repo).split('/')[1] + "_" + str(index) + "_snapshots"
            if os.path.exists(path_snaps+project):
                run_sonar_scanner(path_snaps+project+'/', project, language)
                time.sleep(5)
                scanned_list.append(repo)

def test_scan_main():
    report_path = '/Users/mosesopenja/Documents/summer2020/Quantum/new-collection/Non-quantum/Clones2/'
    input_path = '/Users/mosesopenja/Documents/summer2020/Quantum/new-collection/Non-quantum/'
    df_data = pd.read_csv(input_path + "Selected_Quantum_Repos.csv")
    # Convert to list
    Repos_Name = df_data.Repos_Name.values.tolist()
    Language = df_data.Language.values.tolist()
    project = 'RebornCore'
    run_sonar_scanner(report_path, project,Language)
## Call here to run
#test_scan_main()
main_scanner()
