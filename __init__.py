from mycroft import MycroftSkill, intent_file_handler


class HacksPoetic(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('poetic.hacks.intent')
    def handle_poetic_hacks(self, message):
        self.speak_dialog('poetic.hacks')


def create_skill():
    return HacksPoetic()

