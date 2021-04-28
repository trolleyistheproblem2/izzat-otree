from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'izzat_enter'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    subject_id = models.IntegerField(min=1,max=30,label='Please enter your subject ID in the box below.')

    question1 = models.IntegerField(label="How much would your individual share be from this round?",
                                    choices=[[1, '20'], [2, '7'], [3, '5'], [4, '2']],
                                    widget=widgets.RadioSelect
                                    )