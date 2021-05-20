from jira.client import *


class CustomJIRA(JIRA):
    def add_user(
        self,
        username: str,
        email: str,
        directoryId: int = 1,
        password: str = None,
        fullname: str = None,
        notify: bool = False,
        active: bool = True,
        ignore_existing: bool = False,
        application_keys: Optional[List] = None,
    ):
        """Create a new Jira user.

        Args:
            username (str): the username of the new user
            email (str): email address of the new user
            directoryId (int): The directory ID the new user should be a part of (Default: 1)
            password (Optional[str]): Optional, the password for the new user
            fullname (Optional[str]): Optional, the full name of the new user
            notify (bool): Whether or not to send a notification to the new user. (Default: False)
            active (bool): Whether or not to make the new user active upon creation. (Default: True)
            ignore_existing (bool): Whether or not to ignore and existing user. (Default: False)
            applicationKeys (Optional[list]): Keys of products user should have access to

        Raises:
            JIRAError:  If username already exists and `ignore_existing` has not been set to `True`.

        Returns:
            bool: Whether or not the user creation was successful.


        """
        if not fullname:
            fullname = username
        # TODO(ssbarnea): default the directoryID to the first directory in jira instead
        # of 1 which is the internal one.
        url = self._get_latest_url("user")

        # implementation based on
        # https://docs.atlassian.com/jira/REST/ondemand/#d2e5173
        x: Dict[str, Any] = OrderedDict()

        x["displayName"] = fullname
        x["emailAddress"] = email
        x["name"] = username
        if password:
            x["password"] = password
        if notify:
            x["notification"] = "True"
        if application_keys is not None:
            x["applicationKeys"] = application_keys

        payload = json.dumps(x)
        r = self._session.post(url, data=payload)
        return User(self._options, self._session, json_loads(r))

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

jira_client = JIRA(server_url, basic_auth=('almeki.dev@gmail.com', 'xxx'))
jira_client.add_user_to_group(username='seyiveveli', group='jira-servicedesk-users')  # not working
jira_client.remove_user_from_group(username='seyiveveli', groupname='jira-servicedesk-users')  # not working

jira_client_custom = CustomJIRA(server_url, basic_auth=('almeki.dev@gmail.com', 'xxx'))
jira_client_custom.add_user_to_group(accountId='609c0dbe2009f100682a4a32', group='jira-servicedesk-users')
jira_client_custom.remove_user_from_group(accountId='609c0dbe2009f100682a4a32', groupname='jira-servicedesk-users')
user = jira_client_custom.add_user(username="seyivecoy", email="seyive+coy@trellix.io", fullname="Seyive Coy")

# Others
displayName = "Seyive Yan"
users = jira_client.search_users(query=displayName)
user = jira_client.add_user(username="seyiveyan", email="seyive+yan@trellix.io", fullname="Seyive Yan")  # username is not really considered by the api

# we might need to update everywhere where `username` is used
# username deprecated JIRA cloud, backwards compatibility, i.e. Jira Server/Data Center??
