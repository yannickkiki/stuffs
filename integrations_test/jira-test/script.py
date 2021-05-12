from collections import namedtuple
import json

from jira.client import JIRA as BaseJIRA, json_loads, JIRAError, OrderedDict
from jira.resources import User


def convert_to_object(object_name: str, d: dict):
    object_class = namedtuple(object_name, d.keys())
    return object_class(*d.values())


class ClientMixin:
    def add_user(self, username, email, directoryId=1, password=None,
                 fullname=None, notify=False, active=True, ignore_existing=False, application_keys=None):

        if not fullname:
            fullname = username

        # of 1 which is the internal one.
        url = self._options['server'] + '/rest/api/latest/user'

        # implementation based on
        # https://docs.atlassian.com/jira/REST/ondemand/#d2e5173
        x = OrderedDict()

        x['displayName'] = fullname
        x['emailAddress'] = email
        x['name'] = username
        if password:
            x['password'] = password
        if notify:
            x['notification'] = 'True'
        if application_keys is not None:
            x['applicationKeys'] = application_keys

        payload = json.dumps(x)
        try:
            response = self._session.post(url, data=payload)
        except JIRAError as e:
            err = e.response.json()['errors']
            if 'username' in err and err['username'] == 'A user with that username already exists.' and ignore_existing:
                return True
            raise e

        user_data = json_loads(response)
        return convert_to_object('User', user_data)

    def add_user_to_group(self, account_id, group_name):
        url = self._options['server'] + '/rest/api/latest/group/user'
        x = {'groupname': group_name}
        y = {'accountId': account_id}

        payload = json.dumps(y)

        r = json_loads(self._session.post(url, params=x, data=payload))
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

    def search_users(self, query, startAt=0, maxResults=50, includeActive=True, includeInactive=False):
        params = {
            'query': query,
        }
        return self._fetch_pages(User, None, 'user/search', startAt, maxResults, params)


class JIRA(ClientMixin, BaseJIRA):
    pass


server_url = 'https://almeki.atlassian.net'
jira_client = JIRA(server_url, basic_auth=('almeki.dev@gmail.com', 'jw6akZZSYMT3bdzAjk8Z388B'))
# jira_client = BaseJIRA('https://almeki.atlassian.net/', basic_auth=('almeki.dev@gmail.com', 'jw6akZZSYMT3bdzAjk8Z388B'))
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

users = jira_client.search_users(query="seyivevelo")
# jira_client.search_users('.')
