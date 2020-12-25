import amanobot
import amanobot.aio
import asyncio


token = "1474570701:AAG2tQ3ykzosRpvgCs9o8-QoICehhB1Ttzc"


loop = asyncio.get_event_loop()  # Do not change this


bot = amanobot.aio.Bot(token)
na_bot = amanobot.Bot(token)


me = loop.run_until_complete(bot.getMe())
bot_username = me['username']
bot_id = me['id']


keys = dict(
    giphy = 'key_here',                                             #You can get a key at https://developers.giphy.com
)

git_repo = ('https://github.com/kmacprt/robatkmac', 'master') #Repository where your bot is in

max_time = 60

version = open('version.txt').read()

logs = 

backups_chat = 1131653685  # Put a 0, False or None to disable.
backup_hours = ['00:00', '12:00']

sudoers = [
    1131653685
]

enabled_plugins = [
    'processmsg',
    'start',
    'rules',
    'shorten',
    'sed',
    'kibe',
    'translate',
    'rextester',
    'inlines',
    'welcome',
    'admins',
    'warns',
    'prints',
    'pypi',
    'weather',
    'youtube',
    'ping',
    'gif',
    'git',
    'reddit',
    'coub',
    'sudos',
    'ids',
    'ip',
    'jsondump',
    'dice',
    'misc',
    'antipedro'
]
