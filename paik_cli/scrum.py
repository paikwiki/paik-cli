import datetime
import json

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
    if now_weekday == "Mon":
        target_date = now - datetime.timedelta(3)
    elif now_weekday == "Sun":
        target_date = now - datetime.timedelta(2)
    else:
        target_date = now - datetime.timedelta(1)

    weekday = target_date.strftime("%a")

    h1_title = f"📝 Note-{target_date.strftime('%Y%m%d')}({weeks[weekday]})"

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

    print()
    print("\n".join(urls))
    print()

