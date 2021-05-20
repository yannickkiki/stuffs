from jira import JIRA
from jira.client import Union, Dict, Any, json_loads, json


class CustomJIRA(JIRA):
    def add_user_to_group(
            self, accountId: str, group: str
    ) -> Union[bool, Dict[str, Any]]:
        """Add a user to an existing group.

        Args:
            accountId (str): accountId of the user that will be added to specified group.
            group (str): Group that the user will be added to.

        Returns:
            Union[bool,Dict[str,Any]]: json response from Jira server for success or a value that evaluates as False in case of failure.
        """
        url = self._get_latest_url("group/user")
        x = {"groupname": group}
        y = {"accountId": accountId}

        payload = json.dumps(y)

        r: Dict[str, Any] = json_loads(self._session.post(url, params=x, data=payload))
        if "name" not in r or r["name"] != group:
            return False
        else:
            return r

    def remove_user_from_group(self, accountId: str, groupname: str):
        """Remove a user from a group.

        Args:
            accountId (str): accountId of the user to remove from the group.
            groupname (str): The group that the user will be removed from.
        """
        url = self._get_latest_url("group/user")
        x = {"groupname": groupname, "accountId": accountId}

        self._session.delete(url, params=x)

        return True


server_url = 'https://almeki.atlassian.net'

jira_client = JIRA(server_url, basic_auth=('almeki.dev@gmail.com', 'jw6akZZSYMT3bdzAjk8Z388B'))
jira_client.add_user_to_group(username='seyiveveli', group='jira-servicedesk-users')  # not working
jira_client.remove_user_from_group(username='seyiveveli', groupname='jira-servicedesk-users')  # not working

jira_client_custom = CustomJIRA(server_url, basic_auth=('almeki.dev@gmail.com', 'jw6akZZSYMT3bdzAjk8Z388B'))
jira_client_custom.add_user_to_group(accountId='609c0dbe2009f100682a4a32', group='jira-servicedesk-users')
jira_client_custom.remove_user_from_group(accountId='609c0dbe2009f100682a4a32', groupname='jira-servicedesk-users')

# Others
displayName = "Seyive Yan"
users = jira_client.search_users(query=displayName)
user = jira_client.add_user(username="seyiveyan", email="seyive+yan@trellix.io", fullname="Seyive Yan")  # username is not really considered by the api
# Add user: why not return the result when request is successful ? Will allow us to have accountId

# we might need to update everywhere where `username` is used
# username deprecated JIRA cloud, backwards compatibility, i.e. Jira Server/Data Center??
