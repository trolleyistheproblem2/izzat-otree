from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Intro(Page):
    def is_displayed(self):
        return True

    form_model = 'player'
    form_fields = ['subject_id']

class TrialQuestion(Page):
    def is_displayed(self):
        return True

    form_model = 'player'
    form_fields = ['question1']

    def question1_error_message(self, question1):
        print('just checking', question1)
        if question1 != 2:
            return '''Wrong answer. Please try again! Remember, the total contribution of the group is multiplied by 2 and divided equally!'''

class Thanks(Page):
    def is_displayed(self):
        return True


page_sequence = [
    Intro,
    TrialQuestion,
    Thanks
]
