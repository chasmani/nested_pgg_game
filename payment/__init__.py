from otree.api import *

doc = """
Your app description
"""

class C(BaseConstants):
    NAME_IN_URL = 'payment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    pass


class ThankYou(Page):
    pass

page_sequence = [ThankYou]
