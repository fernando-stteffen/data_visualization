import requests

from operator import itemgetter

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
response = requests.get(url)
print("Status code:", response.status_code)


# Process information
submission_ids = response.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
            str(submission_id) + '.json')
    sub_response = requests.get(url)
    print(url + " - " + str(sub_response.status_code))
    response_dict = sub_response.json()
    
    submission_dict = {
        'title':  response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
    }
    
    submission_dicts.append(submission_dict)


submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), 
reverse=True)


for submission_dict in submission_dicts:
    print("############################################")
    print("Title:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments", submission_dict['comments'])

