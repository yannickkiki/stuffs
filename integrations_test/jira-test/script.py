from collections import namedtuple
import json

from jira.client import JIRA as BaseJIRA, json_loads, OrderedDict
from jira.resources import User


def convert_to_object(object_name: str, d: dict):
    object_class = namedtuple(object_name, d.keys())
    return object_class(*d.values())


class ClientMixin:
    def add_user(self, username, email, password=None, fullname=None):
        body_params = {
            'displayName': fullname or username,
            'emailAddress': email,
            'name': username,
        }
        if password:
            body_params['password'] = password

        response = self._session.post(
            url=self._options['server'] + '/rest/api/latest/user',
            data=json.dumps(body_params)
        )

        user_data = json_loads(response)
        return convert_to_object('User', user_data)

    def add_user_to_group(self, account_id, group_name):
        body_params = {'accountId': account_id}

        response = self._session.post(
            url=self._options['server'] + '/rest/api/latest/group/user',
            params={'groupname': group_name},
            data=json.dumps(body_params)
        )

        r = json_loads(response)
        if 'name' not in r or r['name'] != group_name:
            return False
        else:
            return r

    def remove_user_from_group(self, account_id, group_name):
        url = self._options['server'] + '/rest/api/latest/group/user'
        x = {'groupname': group_name,
             'accountId': account_id}

        self._session.delete(url, params=x)

        return True

    def search_users(self, query, startAt=0, maxResults=50):
        params = {
            'query': query,
        }
        return self._fetch_pages(User, None, 'user/search', startAt, maxResults, params)


class JIRA(BaseJIRA):
    pass


server_url = 'https://almeki.atlassian.net'
jira_client = JIRA(server_url, basic_auth=('almeki.dev@gmail.com', 'xxx'))
# jira_client = BaseJIRA('https://almeki.atlassian.net/', basic_auth=('almeki.dev@gmail.com', 'xxx'))
issue = jira_client.issue('BEN-13')

projects = jira_client.projects()

issue_types = jira_client.issue_types()

issue = jira_client.create_issue(
    summary='Naaw issue from jira-python',
    # summary='New Contact Form Issue',
    description='*Email*: seyiva.kiki@gmail.com \n *Customer*: Nice customer \n',
    project={'id': 10000},
    # issuetype={'name': 'Epic'},
    issuetype={'id': 10001},
    reporter={'id': '609c10df97f3d40070b8b75f'}
)
issue_url = f"{server_url}/browse/{issue.key}"

# jira_client.groups()
# jira_client.add_group('TestiGroup')
user = jira_client.add_user(username="seyivevelo", email="seyive+velo@trellix.io")
# jira_client.add_user_to_group(username="seyiveveli", group="jira-servicedesk-users")  # not working anymore
jira_client.add_user_to_group(account_id=user.accountId, group_name="jira-servicedesk-users")
jira_client.remove_user_from_group(account_id='609c10df97f3d40070b8b75f', group_name="jira-software-users")

users = jira_client.search_users(query="seyivevelii")
# jira_client.search_users('.')
