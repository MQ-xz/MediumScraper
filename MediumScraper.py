import requests
import json

print('''\033[32;1m___  ___         _ _                 _____                                
|  \/  |        | (_)               /  ___|                               
| .  . | ___  __| |_ _   _ _ __ ___ \ `--.  ___ _ __ __ _ _ __   ___ _ __ 
| |\/| |/ _ \/ _` | | | | | '_ ` _ \ `--. \/ __| '__/ _` | '_ \ / _ \ '__|
| |  | |  __/ (_| | | |_| | | | | | /\__/ / (__| | | (_| | |_) |  __/ |   
\_|  |_/\___|\__,_|_|\__,_|_| |_| |_\____/ \___|_|  \__,_| .__/ \___|_|   
                                                         | |              
                                                         |_|              
                        https://t.me/Xpykerz
\033[0m''')

try:
    tage = input('Enter Tage {use - is there is space in tage (ex:bug-bounty)}: ')
    year = input('Year (yyyy): ')
    month = input('Month (mm): ')
    day = input('Day (dd): ')

    api = f"https://medium.com/tag/{tage}/archive/{year}/{month}/{day}"
    res = requests.get(api).text
    data = json.loads(res.split('window["obvInit"](')[1].split(')\n// ]]>')[0])

    for user,post in zip(data['references']['User'],data['references']['Post']):
        # print(json['references']['User'][i])
        username = data['references']['User'][user]['username']
        postdata = data['references']['Post'][post]
        postid = postdata['id']
        title = postdata['title']
        subtitle = postdata['content']['subtitle']
        url = f'https://medium.com/{username}/{postdata["uniqueSlug"]}'
        print(f'''\033[32;1m{title} by {username}
\033[0m{subtitle}
\033[34;4m{url}\033[0m
''')
except:
    print('Something Wrong Try Agian.........!')