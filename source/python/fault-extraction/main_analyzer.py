import argparse
import csv
import json
import os
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dir', help="search directory")
parser.add_argument('-r', '--repo', help="repo org/name")
parser.add_argument('-v', '--repoversion', help="repo version")
parser.add_argument('-t', '--testing', help="run as testing", nargs="?", const="tangent")

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def run_main(repo_dir,repo_name, repo_version, save_version=0, save_image=False):
    repo_version = str(repo_version).replace("b'",'')
    docker_files = FileManagement.list_project_docker_files(repo_dir)
    path_output = ROOT_DIR+'/outputs/csv/'
    if not os.path.exists(ROOT_DIR+'/outputs/csv'):
        os.makedirs(ROOT_DIR+'/outputs/csv')
    if not os.path.exists(path_output + 'results_instruction_{}.csv'.format(save_version)):
         data_file = open(path_output + 'results_instruction_{}.csv'.format(save_version), mode='w', newline='', encoding='utf-8')
         data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
         data_writer.writerow(
             ['repos', 'repo_version','filename', 'instructions', 'instructions_count'])
         ## Second file
         data_file2 = open(path_output + 'results_options_{}.csv'.format(save_version), mode='w', newline='', encoding='utf-8')
         data_writer2 = csv.writer(data_file2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
         data_writer2.writerow(
             ['repos', 'repo_version', 'filename', 'option', 'option_count', 'category'])

         data_file3 = open(path_output + 'options_raw_details_{}.csv'.format(save_version), mode='w', newline='',
                           encoding='utf-8')
         data_writer3 = csv.writer(data_file3, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
         data_writer3.writerow(
             ['repos', 'repo_version', 'filename', 'option','total_counts', 'details'])
    else:
        data_file = open(path_output + 'results_instruction_{}.csv'.format(save_version), mode='a+', newline='', encoding='utf-8')
        data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        ## Second file
        data_file2 = open(path_output + 'results_options_{}.csv'.format(save_version), mode='a+', newline='', encoding='utf-8')
        data_writer2 = csv.writer(data_file2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        data_file3 = open(path_output + 'options_raw_details_{}.csv'.format(save_version), mode='a+', newline='',
                          encoding='utf-8')
        data_writer3 = csv.writer(data_file3, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # , repo_dir, repo_name, repo_version
    docker_image_contents = FileManagement.get_file_contents(docker_files)
    imageOptions = ImageOptions()
    parser = Parser()


    for file_, source in docker_image_contents.items():
        dockerImage = DockerImage()
        #print (type(source))
        #print (source)
        parser.content = source
        json_data = json.loads(parser.json)
        dockerImage.analyse(json_data)
        instructions_dict = dockerImage.instructions_dict
        instructions_options_dict = dockerImage.instructions_options_dict
        options_data = dockerImage.option_data
        file_name = str(file_).split('/')[len(str(file_).split('/')) - 1]
        for key, val in instructions_dict.items():
            data_writer.writerow(
                [repo_name, repo_version, file_name, key, val])
        for key, val in instructions_options_dict.items():
            data_writer2.writerow(
                [repo_name, repo_version, file_name, key, val, imageOptions.get_category(key)])
        for key, val in options_data.items():
            data_writer3.writerow(
                [repo_name, repo_version, file_name, key, len(val), val])
        if save_image:

            if not os.path.exists(ROOT_DIR+'/outputs/dockerfiles'):
                os.makedirs(ROOT_DIR+'/outputs/dockerfiles')
            if not os.path.exists(ROOT_DIR+'/outputs/dockerfiles/'+repo_name.split('/')[0]):
                os.makedirs(ROOT_DIR+'/outputs/dockerfiles/'+repo_name.split('/')[0])
            if not os.path.exists(ROOT_DIR+'/outputs/dockerfiles/'+repo_name):
                os.makedirs(ROOT_DIR+'/outputs/dockerfiles/'+repo_name)
            if '/' in repo_version:
                repo_version = repo_version.replace('/', '_')
            with open(ROOT_DIR+'/outputs/dockerfiles/'+str(repo_name)+'/'+file_name+'_'+str(repo_version), "w") as _file:
                _file.write(source)
    data_file.close()
    data_file2.close()
def exit_if_invalid_args(args):
    if args.dir is None or os.path.isfile(args.dir):
        raise SystemExit("ERROR: -d --dir arg should be directory.")
    if args.repo is None:
        raise SystemExit("ERROR: -r --repo arg should be repo org/name.")
    if args.repoversion is None:
        raise SystemExit("ERROR: -v --repoversion arg should be repo release version.")

if __name__ == "__main__":
    args = parser.parse_args()
    exit_if_invalid_args(args)
    repo_dir = os.path.abspath(args.dir)
    repo_name = args.repo
    repo_version = args.repoversion
    run_main(repo_dir,repo_name, repo_version)