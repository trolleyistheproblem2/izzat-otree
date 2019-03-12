from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'izzat_t2'
    players_per_group = 4
    num_rounds = 4

    endowment = c(10)
    multiplier = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()

    punr_1 = models.CurrencyField(initial=0)
    punr_2 = models.CurrencyField(initial=0)
    punr_3 = models.CurrencyField(initial=0)
    punr_4 = models.CurrencyField(initial=0)

    def set_punishments(self):
        self.punr_1 = sum(p.pun_1 for p in self.get_players())
        self.punr_2 = sum(p.pun_2 for p in self.get_players())
        self.punr_3 = sum(p.pun_3 for p in self.get_players())
        self.punr_4 = sum(p.pun_4 for p in self.get_players())

        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p3 = self.get_player_by_id(3)
        p4 = self.get_player_by_id(4)

        p1.payoff = Constants.endowment - p1.contribution - 0.5*p1.punishment_sent - p1.group.punr_1 + p1.group.individual_share
        p2.payoff = Constants.endowment - p2.contribution - 0.5 * p2.punishment_sent - p2.group.punr_1 + p2.group.individual_share
        p3.payoff = Constants.endowment - p3.contribution - 0.5 * p3.punishment_sent - p3.group.punr_1 + p3.group.individual_share
        p4.payoff = Constants.endowment - p4.contribution - 0.5 * p4.punishment_sent - p4.group.punr_1 + p4.group.individual_share

        print('sumpr1',self.punr_1)

    def set_contribution(self):
        self.total_contribution = sum([p.contribution for p in self.get_players()])
        self.individual_share = self.total_contribution * Constants.multiplier / Constants.players_per_group


class Player(BasePlayer):

    contribution = models.CurrencyField(min=0,max=Constants.endowment, label='Enter your contribution')

    pun_1 = models.CurrencyField(min=0,max=Constants.endowment,label='Enter punishment amount for member 1',blank=True,initial=c(0))

    pun_2 = models.CurrencyField(min=0,max=Constants.endowment,label='Enter punishment amount for member 2',blank=True,initial=c(0))

    pun_3 = models.CurrencyField(min=0,max=Constants.endowment,label='Enter punishment amount for member 3',blank=True,initial=c(0))

    pun_4 = models.CurrencyField(min=0,max=Constants.endowment,label='Enter punishment amount for member 4',blank=True,initial=c(0))

    remaining = models.CurrencyField(min=0,max=Constants.endowment)

    essay_text = models.LongStringField()

    punishment_sent = models.CurrencyField(initial=0)
    punishment_cost_self = models.CurrencyField(initial=0)

    def set_player_sent_punishment(self):
        print(self.pun_1,self.pun_2,self.pun_3,self.pun_4)
        self.punishment_sent = self.pun_1 + self.pun_2 + self.pun_3 + self.pun_4
        self.punishment_cost_self = 0.5 * self.punishment_sent

    def set_payoffs(self):
        if self.id_in_group == 1:
            self.payoff = Constants.endowment - self.contribution - 0.5*self.punishment_sent - self.group.punr_1 + self.group.individual_share
        elif self.id_in_group == 2:
            self.payoff = Constants.endowment - self.contribution - 0.5*self.punishment_sent - self.group.punr_2 + self.group.individual_share
        elif self.id_in_group == 3:
            self.payoff = Constants.endowment - self.contribution - 0.5*self.punishment_sent - self.group.punr_3 + self.group.individual_share
        elif self.id_in_group == 4:
            self.payoff = Constants.endowment - self.contribution - 0.5*self.punishment_sent - self.group.punr_4 + self.group.individual_share