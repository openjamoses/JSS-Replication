import csv
import pandas as pd
import math
import time
import random
#from src.quantum.codeanalyser.v2.TOKENS import get_tokens
import urllib.request
import json

def get_tokens():
    tokens = ["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",
              "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",
              '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',
              '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',
              #'​​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',
              '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',
              #'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'
              ]
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
            print('           opp! ', e, self.url, self.ct)
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
        url2 = 'https://api.github.com/repos/'+self.repo+'/issues/'+str(issue_id)
        data, self.ct = get_data(url2, self.ct) #GitHub(url2, self.ct).getResponse()
        p += 1
        state = ''
        if data != None:
            state = data['state']
            for label_obj in data['labels']:
                name = label_obj['name']
                if 'bug' in str(name).lower():
                    is_buggy = True

        return is_buggy, state, self.ct
