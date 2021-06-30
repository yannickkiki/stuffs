import json

import requests


class TodoistAPI:

    def __init__(self, api_token):
        self.api_token = api_token

    def get(self, endpoint, params=None):
        response = requests.get(
            url=f"https://api.todoist.com/rest/v1/{endpoint}",
            headers={"Authorization": f"Bearer {self.api_token}"},
            params=params or {}
        )
        return response.json()


api = TodoistAPI(
    api_token="xxx"  # https://todoist.com/prefs/integrations
)
projects = api.get('projects')
sections = api.get('sections', params={'project_id': 2262341594})
tasks = api.get('tasks', params={'section_id': 49852392})
parent_tasks = api.get('tasks', params={'section_id': 49852392, 'filter': '!subtask'})

with open('tasks.json', 'w') as f:
    json.dump(parent_tasks, f, indent=4)
