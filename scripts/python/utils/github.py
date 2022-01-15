import csv
import pandas as pd
import math
import time
import random
#from src.quantum.codeanalyser.v2.TOKENS import get_tokens
import urllib.request
import json

def get_tokens():
    tokens = []# please provide atleast one tokens here before running this script
    return tokens
class GitHub:
    def __init__(self, url, ct):
        self.ct = ct
        self.url = url
    def getResponse(self):
        jsonData = None
        code = 200
        try:
            if self.ct == len(get_tokens()):
                self.ct = 0
            reqr = urllib.request.Request(self.url)
            reqr.add_header('Authorization', 'token %s' % get_tokens()[self.ct])
            opener = urllib.request.build_opener(urllib.request.HTTPHandler(debuglevel=1))
            content = opener.open(reqr).read()
            self.ct += 1
            #print(content)
            jsonData = json.loads(content)
            #return jsonData, self.ct
        except Exception as e:
            #pass
            print(e, self.url, self.ct)
            if not 'HTTP Error 403:' in str(e):
                code = 404
        return jsonData, code, self.ct
    def url_header(self):
        jsonData = None
        try:
            if self.ct == len(get_tokens()):
                self.ct = 0
            reqr = urllib.request.Request(self.url)
            reqr.add_header('Accept', 'application/vnd.github.mercy-preview+json')
            reqr.add_header('Authorization', 'token %s' % get_tokens()[self.ct])
            opener = urllib.request.build_opener(urllib.request.HTTPHandler(debuglevel=1))
            content = opener.open(reqr).read()
            self.ct += 1
            jsonData = json.loads(content)
            return jsonData, self.ct
        except Exception as e:
            pass
            #print(e)
        return jsonData, self.ct
def get_data(url, ct):
    while True:
        data, code, ct = GitHub(url, ct).getResponse()
        if data != None:
            break
        if code == 404:
            break
        time.sleep(15)
    return data, ct
class GitHubMeta:
    def __init__(self, repo, ct):
        self.ct = ct
        self.repo = repo
    def check_issues_buggy_(self, issue_id):
        p = 1
        is_buggy = False
        is_status = ''
        url2 = 'https://api.github.com/repos/'+self.repo+'/issues/'+str(issue_id)
        data, self.ct = get_data(url2, self.ct) #GitHub(url2, self.ct).getResponse()
        p += 1
        if data != None:
            is_status = data['state']
            for label_obj in data['labels']:
                name = label_obj['name']
                if 'bug' in str(name).lower():
                    is_buggy = True

        return is_buggy, is_status, self.ct

    def get_file_infor_hash_(self, hash):
        p = 1
        list_filename = []
        list_changes = []
        url2 = 'https://api.github.com/repos/'+self.repo+'/commits/'+str(hash)
        data, self.ct = get_data(url2, self.ct) #GitHub(url2, self.ct).getResponse()
        p += 1
        if data != None:
            for files_obj in data['files']:
                list_filename.append(files_obj['filename'])
                list_changes.append(files_obj['changes'])
        return list_filename, list_changes, self.ct

    def get_file_dates_infor_hash_(self, hash):
        p = 1
        data_dict = {}
        url2 = 'https://api.github.com/repos/'+self.repo+'/commits/'+str(hash)
        data, self.ct = get_data(url2, self.ct) #GitHub(url2, self.ct).getResponse()
        p += 1
        if data != None:
            data_dict['date'] = data['commit']['author']['date']
            data_dict['cloc'] = data['stats']['total']
            for files_obj in data['files']:
                data_dict[files_obj['filename']] = files_obj['changes']
        return data_dict, self.ct

    def get_hash_cloc_(self, hash):
        p = 1
        cloc = 0
        url2 = 'https://api.github.com/repos/'+self.repo+'/commits/'+str(hash)
        data, self.ct = get_data(url2, self.ct) #GitHub(url2, self.ct).getResponse()
        p += 1
        if data != None:

            cloc = data['stats']['total']
        return cloc, self.ct
