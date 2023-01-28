import requests
import unittest

# # ======-----------Python book "" 17.1 - 17.4

# Make an API call and store the response.
# def get_response(language):
#     url = f'https://api.github.com/search/repositories?q=language:{language},&sort=stars'
#     headers = {'Accept': 'application/vnd.github.v3+json'}
#     r = requests.get(url, headers=headers)
#     statusResponse = r.status_code
#
# # Store API response in a variable.
#     response_dict = r.json()
#     return statusResponse
# # Process results.
#
# class Testresponses(unittest.TestCase):
#     """ Tests for get_response.py  """
#     def test_python_repos(self):
#         status = get_response(language='C')
#         self.assertEqual(status, 200)
#
# if __name__ == '__main__':
#     unittest.main()

from plotly.graph_objs import Bar, Layout
from plotly import offline
from operator import itemgetter
import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
#print(f"Status code: {r.status_code}")
# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
# Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
# Build a dictionary for each article.
    submission_dict = {
    'title': response_dict['title'],
    'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
    'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                            reverse=True)

#build a list of amount of coments
comments = []
titles = []
for submission_dict in submission_dicts:
    comment = submission_dict['comments']
    comments.append(comment)
    title = submission_dict['title']
    titles.append(title)
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

# Visualize the results.
# x_values = titles
# data = [Bar(x=x_values, y=comments)]
# x_axis_config = {'title': 'Result'}
# y_axis_config = {'title': 'Quantity of comments'}
# my_layout = Layout(title='Amount of comments',
#         xaxis=x_axis_config, yaxis=y_axis_config)
# offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')


