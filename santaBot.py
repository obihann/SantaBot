import yaml
import santaslist

from errbot import BotPlugin, botcmd
from pathlib import Path

YML_FILE = 'people.yml'


class SantaBot(BotPlugin):
    def __init__(self, *args, **kwargs):
        if Path(YML_FILE).is_file():
            data = open('people.yml', 'r')
            santaslist.load_people(yaml.load(data)['people'])

        super(SantaBot, self).__init__(*args, **kwargs)

    @botcmd
    def people(self, msg, args):
        return santaslist.print_people()

    @botcmd
    def pairs(self, msg, args):
        return santaslist.print_pairs()
