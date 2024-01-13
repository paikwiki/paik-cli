import datetime
import json

import pyperclip

urls = []


def pick_jira_url(string, config, spaces=0):
    if string.find(config.jira_url) == -1:
        return string

    url = string[string.find(config.jira_url) :]
    urls.append(url)

    return string.replace(url, "")


def print_for_scrum(memo, config):
    weeks = {
        "Mon": "월",
        "Tue": "화",
        "Wed": "수",
        "Thu": "목",
        "Fri": "금",
        "Sat": "토",
        "Sun": "일",
    }
    now = datetime.datetime.now()
    now_weekday = now.strftime("%a")

    h1_title = f"📝 Note-{now.strftime('%Y%m%d')}({weeks[now_weekday]})"
    h1_title = "📝 Note-20240112(금)"
    data = {"did": memo[h1_title]["did"], "willDo": memo[h1_title]["willDo"]}

    for key in data:
        print(key)
        if type(data[key]) == list:
            for string in data[key]:
                print(f"  {pick_jira_url(string, config, 2)}")
        else:
            for key2 in data[key]:
                print(pick_jira_url(key2, config, 2))
                if type(data[key][key2]) == list:
                    for string in data[key][key2]:
                        print(f"  {pick_jira_url(string, config, 4)}")

    urls_str = "\n".join(urls)
    pyperclip.copy(urls_str)
    print(f"\n{urls_str}\n")
