from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
import urllib2
from urllib2 import urlopen
import json
def index(request):
    return render_to_response('codeforces.html')

def view1(request):
    template=loader.get_template('blog/form.html')
    return HttpResponse(template.render(request))

from django.shortcuts import render_to_response
import random
import datetime
import time

def view2(request):
    list={'A':'1','B':'2','C':'3'}
    return render_to_response('pie.html',{"list":list})
def view3(request):


    global_dict = {
        'dp': 35,
        'dfs and similar': 34,
        'binary search': 33,
        'ternary search': 32,
        'two pointers': 31,
        'fft': 30,
        'meet-in-the-middle': 29,
        'shortest paths': 28,
        'constructive algorithms': 27,
        'implementation': 26,
        'divide and conquer': 25,
        'graph matchings': 24,
        'greedy': 23,
        'number theory': 22,
        'combinatorics': 21,
        'sortings': 20,
        'graphs': 19,
        'trees': 18,
        'string suffix structures': 17,
        'data structures': 16,
        'strings': 15,
        'expression parsing': 14,
        'schedules': 13,
        'probabilities': 12,
        'flows': 11,
        'math': 10,
        'matrices': 9,
        '2-sat': 8,
        'chinese remainder theorem': 7,
        'geometry': 6,
        'brute force': 5,
        'hashing': 4,
        'dsu': 3,
        'bitmasks': 2,
        'games': 1}
    user_verdicts = {}
    user_data_complete = {}

    def get_maxprior_tag(all_tags):
        max_till_now = 0
        tag_with_max_priority = ''
        for i in all_tags:
            if max_till_now < global_dict[i]:
                max_till_now = global_dict[i]
                tag_with_max_priority = i
        return tag_with_max_priority

    def get_user_data(user_handle):
        url = "http://codeforces.com/api/user.status?handle="
        url = url + user_handle
        response = urllib2.urlopen(url)
        data = json.load(response)
        for i in data['result']:
            if (i['verdict'] in user_verdicts):
                user_verdicts[i['verdict']] = user_verdicts[i['verdict']] + 1
            else:
                user_verdicts[i['verdict']] = 1
        for i in data['result']:
            local_verdict = i['verdict']
            problem_tag = get_maxprior_tag(i['problem']['tags'])
            if problem_tag in user_data_complete:
                if local_verdict in user_data_complete[problem_tag]:
                    user_data_complete[problem_tag][local_verdict] = user_data_complete[problem_tag][local_verdict] + 1
                else:
                    user_data_complete[problem_tag][local_verdict] = 1
            else:
                user_data_complete[problem_tag] = {local_verdict: 1}

    handle = 'Black_Hammer96'
    get_user_data(handle)
    import demjson
    obj = demjson.encode(user_verdicts)
    user={"a":1,"b":2,"c":3}
    return render_to_response('goog.html',{"user_verdicts":user_verdicts,"user":user})