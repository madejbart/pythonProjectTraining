import requests
import unittest

# # ======-----------Python book "" 17.1 - 17.4

# Make an API call and store the response.
def get_response(language):
    url = f'https://api.github.com/search/repositories?q=language:{language},&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    statusResponse = r.status_code

# Store API response in a variable.
    response_dict = r.json()
    return statusResponse
# Process results.

class Testresponses(unittest.TestCase):
    """ Tests for get_response.py  """
    def test_python_repos(self):
        status = get_response(language='C')
        self.assertEqual(status, 200)

if __name__ == '__main__':
    unittest.main()
