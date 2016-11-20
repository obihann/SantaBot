import yaml
import SantasList

from errbot import BotPlugin, botcmd


class SantaBot(BotPlugin):
    def __init__(self, *args, **kwargs):
        data = open('people.yml', 'r')
        SantasList.load_people(yaml.load(data)['people'])

        super(SantaBot, self).__init__(*args, **kwargs)

    @botcmd
    def pairs(self, msg, args):
        return SantasList.list_matches()
