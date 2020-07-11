import requests
import json

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
print(data.keys())

try:
    # Subreddit keys
    print(data['data'].keys())
    print()
    # Post keys
    print(data['data']['children'][0]['data'].keys())
    print()

    # Print info for each post
    for child in data['data']['children']:
        print(child['data']['created_utc'], " --- ", child['data']['title'], " - ", child['data']['url'])
        print()
except:
    print("Error reading data")
    print(data)