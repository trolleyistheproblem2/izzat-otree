from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'izzat_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ultimatum_type = models.IntegerField()

    ultimatum_reservation_price = models.IntegerField(min=0, max=50,
                                                      label='Please enter the minimum amount you would accept:')

    partner_religion = models.StringField()

    def set_partner_religion(self):
        if self.participant.id_in_session % 2 == 0:
            self.partner_religion = 'Hindu'
        else:
            self.partner_religion = 'Muslim'

    gender = models.StringField(
        choices=['Male', 'Female'],
        label='What is your gender?',
        widget=widgets.RadioSelect)

    age = models.IntegerField(min=0, max=30, label='What is your age?', choices=range(18, 31))

    city = models.StringField(label='What is your hometown?')

    religion = models.StringField(choices=['Hindu', 'Muslim', 'Christian', 'Parsi', 'Jain'],
                                  widget=widgets.RadioSelect,
                                  label='What religion have you been brought up with?')

    income = models.IntegerField(min=0, max=100000000,
                                 label='''What is your family's monthly income? Please enter your best estimate in rupees in the box below.''')

    religiosity = models.StringField(choices=['1', '2', '3', '4', '5', '6', '7'],
                                        widget=widgets.RadioSelectHorizontal,
                                        label='Please tell us how religious a person you are? 1 means not religious at all, and 7 means extremely religious. ')

