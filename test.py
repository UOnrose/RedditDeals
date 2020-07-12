import requests
import json
from datetime import datetime, timezone
from dateutil import tz

'''     User comment example    '''
# Get request using a custom agent (default can cause 429: Too Many Requests)
r = requests.get(r'http://www.reddit.com/user/spilcm/comments/.json', headers = {'User-agent': 'Noah Bot'})
# Read data as JSON object
data = r.json()

# Print keys (should be 'kind' and 'data')
#print(data.keys())

# Print comments from a user
'''
try:
    for child in data['data']['children']:
        print(child['data']['id'], " ", child['data']['author'],child['data']['body'])
        print()
except:
    print("Error reading data")
'''

'''     Subreddit posts example     '''

''' Example URLs:
    Top posts today: r'https://www.reddit.com/r/buildapcsales/top.json?t=day'
    Top posts this week: r'https://www.reddit.com/r/buildapcsales/top.json?t=week'
    New posts: r'https://www.reddit.com/r/buildapcsales/new.json'
'''

r = requests.get(r'https://www.reddit.com/r/buildapcsales/new.json', headers = {'User-agent': 'Noah Bot'})
# Read data as JSON object
data = r.json()

# Print keys (should be 'kind' and 'data')
#print(data.keys())

try:
    # Subreddit keys
    #print(data['data'].keys())
    #print()
    # Post keys
    #print(data['data']['children'][0]['data'].keys())
    #print()

    # Print info for each post
    print()
    for child in data['data']['children']:
        # Get time in seconds
        ts = child['data']['created_utc']
        # Convert to date string
        date_str = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        # Autodetect timezone
        from_zone = tz.tzutc()
        to_zone = tz.tzlocal()

        # Replace timezone
        utc = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        utc = utc.replace(tzinfo=from_zone)
        
        date_str_final = utc.astimezone(to_zone)

        # Get post tag
        tag = child['data']['title'].split("[")[1].split("]")[0]

        # Show only monitors
        if tag == "Monitor":
            # Time --- score - title - link - tag
            print(date_str_final, " --- ", child['data']['score'], " - ", child['data']['title'], " - ", child['data']['url'], " - ", tag)
            print()
            
except Exception as e:
    print("Error reading data")
    print(e)