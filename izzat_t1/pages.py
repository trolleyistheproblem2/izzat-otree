from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class StartPage(Page):
    def is_displayed(self):
        return self.round_number == 4

class EssayPage(Page):
    def is_displayed(self):
        return self.round_number == 4

    form_model = 'player'
    form_fields = ['essay_text']

    timeout_seconds = 600

class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']

    timeout_submission = {'contribution': 5}

    def before_next_page(self):
        self.player.remaining = Constants.endowment - self.player.contribution
        print('remaining for',self.player.id_in_group,'is',self.player.remaining)


class PunishmentWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_contribution()

class PunishmentAlt(Page):
    def is_displayed(self):
        return True

class Punishment1(Page):
    form_model = 'player'
    form_fields = ['pun_2','pun_3','pun_4']

    timeout_submission = {'pun_2': c(0),
                          'pun_3':c(0),
                          'pun_4':c(0),
                          }

    def is_displayed(self):
        return False

    def before_next_page(self):
        self.player.set_player_sent_punishment()

class Punishment2(Page):
    form_model = 'player'
    form_fields = ['pun_1','pun_3','pun_4']

    timeout_submission = {'pun_1': c(0),
                          'pun_3':c(0),
                          'pun_4':c(0),
                          }

    def is_displayed(self):
        return False

    def before_next_page(self):
        self.player.set_player_sent_punishment()

class Punishment3(Page):
    form_model = 'player'
    form_fields = ['pun_1','pun_2','pun_4']

    timeout_submission = {'pun_1': c(0),
                          'pun_2':c(0),
                          'pun_4':c(0),
                          }

    def is_displayed(self):
        return False

    def before_next_page(self):
        self.player.set_player_sent_punishment()

class Punishment4(Page):
    form_model = 'player'
    form_fields = ['pun_1','pun_2','pun_3']

    timeout_submission = {'pun_1': c(0),
                          'pun_2':c(0),
                          'pun_3':c(0),
                          }

    def is_displayed(self):
        return False

    def before_next_page(self):
        self.player.set_player_sent_punishment()

class ResultsWaitPage(WaitPage):

    # def is_displayed(self):
    #     return self.round_number > 3

    def after_all_players_arrive(self):
        self.group.set_punishments()

class Process(Page):

    def before_next_page(self):
        self.player.set_payoffs()

class Results(Page):
    def is_displayed(self):
        return True

class Results_2(Page):
    def is_displayed(self):
        return False

class FinalResults(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    StartPage,
    EssayPage,
    Contribute,
    PunishmentWaitPage,
    PunishmentAlt,
    Punishment1,
    Punishment2,
    Punishment3,
    Punishment4,
    ResultsWaitPage,
    # Process,
    Results,
    Results_2,
    FinalResults
]
