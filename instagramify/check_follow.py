import json
import os
from instaloader import Instaloader, Profile, FrozenNodeIterator

username = 'suzykeech'
password = 'xxx'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filename = f'{BASE_DIR}/session-{username}'

L = Instaloader()
# L.login(username, password)
L.load_session_from_file(username, filename)

profile_follower = Profile.from_username(L.context, 'yannick_kiki')
profile_followee = Profile.from_username(L.context, 'suzykeech')

is_follow = False
for followee in profile_follower.get_followees():
    if int(followee.userid) == int(profile_followee.userid):
        is_follow = True
        break
