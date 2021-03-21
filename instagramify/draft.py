<<<<<<< 7d7b3797e712139683354bc252c7bb08819db15c
import json
import os
from instaloader import Instaloader, Profile, FrozenNodeIterator

username = 'yannick_kiki'
password = 'xxx'
=======
import os
from instaloader import Instaloader, Profile

username = 'yannick_kiki'
password = 'Peace1999'
>>>>>>> - stuffs

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filename = f'{BASE_DIR}/session-{username}'

L = Instaloader()
<<<<<<< 7d7b3797e712139683354bc252c7bb08819db15c
L.login(username, password)
L.save_session_to_file(filename)

# Use
L.load_session_from_file(username, filename)
profile = Profile.from_username(L.context, username)
followers_count = profile.followers

followers = profile.get_followers()  # follower.username to get username
for idx, follower in enumerate(followers):
    if idx == 1:
        break

f_list = []
for follower in profile.get_followers():
    f_list.append(follower)


post_iterator = profile.get_posts()

with open("resume_information.json") as json_file:
    data = json.load(json_file)
post_iterator.thaw(FrozenNodeIterator(**data))

for idx, post in enumerate(post_iterator):
    print(post.url)
    if idx == 1:
        # with open('resume_information.json', 'w') as outfile:
        #     json.dump(post_iterator.freeze()._asdict(), outfile)
        break


# ---- Session handling ---- #
import os
import pickle
from functools import partial

import requests
from instaloader import Instaloader as BaseInstaloader, Profile


class Instaloader(BaseInstaloader):

    def load_session_from_cookies(self, username, session_cookies_dict):
        session = requests.Session()
        session.cookies = requests.utils.cookiejar_from_dict(session_cookies_dict)
        session.headers.update(self.context._default_http_header())
        session.headers.update({'X-CSRFToken': session.cookies.get_dict()['csrftoken']})
        if self.context.request_timeout is not None:
            # Override default timeout behavior.
            # Need to silence mypy bug for this. See: https://github.com/python/mypy/issues/2427
            session.request = partial(session.request, timeout=self.context.request_timeout)  # type: ignore
        self.context._session = session
        self.context.username = username


username = 'yannick_kiki'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filename = f'{BASE_DIR}/session-{username}'

with open(filename, 'rb') as sessionfile:
    session_cookies_dict = pickle.load(sessionfile)

# We can use the session cookies directly to avoid logging in every time
# instaloader = Instaloader()
# instaloader.login()
# instaloader.save_session_to_file()
# session_cookies_dict = pickle.load(sessionfile)
L = Instaloader()
# L.load_session_from_file()
L.load_session_from_cookies(username, session_cookies_dict_)

profile = Profile.from_username(L.context, username)
followers = profile.get_followers()
=======
L.load_session_from_file(username, filename)

profile = Profile.from_username(L.context, 'yannick_kiki')
followees = list(profile.get_followees())
>>>>>>> - stuffs
