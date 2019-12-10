import json
import os
from instaloader import Instaloader, Profile, FrozenNodeIterator

username = 'suzykeech'
password = 'xxx'

username = 'yannick_kiki'
password = 'xxx'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filename = f'{BASE_DIR}/session-{username}'

L = Instaloader()
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
