import requests
from pprint import pprint


class TodoistBaseAPI:

    def __init__(self, api_token):
        self.api_token = api_token

    def get(self, endpoint, params=None):
        response = requests.get(
            url=f"https://api.todoist.com/rest/v1/{endpoint}",
            headers={"Authorization": f"Bearer {self.api_token}"},
            params=params or {}
        )
        return response.json()


class TodoistAPI:

    def __init__(self, api_token):
        self.api = TodoistBaseAPI(api_token=api_token)

    def _get_section_id(self, section_name):
        sections = self.api.get('sections')
        for section in sections:
            if section['name'] == section_name:
                return section['id']
        raise AssertionError(f"La section {section_name} semble ne pas exister. "
                             f"Si c'est une erreur , contactes le Yannoveli.")

    def get_tasks(self, section_name):
        section_id = self._get_section_id(section_name)
        tasks = self.api.get('tasks', params={'section_id': section_id})
        tasks.sort(key=lambda task: task.get('parent_id') or 0)
        return tasks


if __name__ == '__main__':
    api = TodoistAPI(
        api_token="xxx"  # https://todoist.com/prefs/integrations
    )
    tasks = api.get_tasks(section_name="Done")
    pprint(tasks, indent=2)
