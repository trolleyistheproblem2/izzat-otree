from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass

class Intro(Page):
    def before_next_page(self):
        return self.player.set_partner_religion()

class Ultimatum(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    form_model = 'player'
    form_fields = ['ultimatum_reservation_price']

    def vars_for_template(self):
        return {
            'partner_religion': self.player.partner_religion
        }


class Questions(Page):
    form_model = 'player'
    form_fields = ['age','gender','city','religion','income','religiosity']

    def is_displayed(self):
        return True

class FinalResults(Page):
    def is_displayed(self):
        return True

page_sequence = [
    Intro,
    Ultimatum,
    Questions,
    FinalResults
]
