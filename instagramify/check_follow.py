import os
from instaloader import Instaloader, Profile


L = Instaloader()

bot_username, bot_password = 'yannick_kiki', 'xxxx'  # Set valid credentials here
L.login(bot_username, bot_password)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
session_filename = f'{BASE_DIR}/session-{bot_username}'
L.save_session_to_file(session_filename)

# L.load_session_from_file(bot_username, filename)


def check_follow(username_x, username_y):
    # Check if username_x is following username_y
    profile_x = Profile.from_username(L.context, username_x)
    profile_y = Profile.from_username(L.context, username_y)
    is_follow = False
    for followee in profile_x.get_followees():
        if followee.userid == profile_y.userid:
            is_follow = True
            break
    return is_follow


result = check_follow('yannick_kiki', 'bombe_robii')
print(result)
