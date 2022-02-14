
class TimeCreator:

    def __init__(self, subject, start_time):
        self.subject = subject
        self.start_time = start_time

    def __repr__(self):
        return f'You have been learning for about {self.start_time} about {self.subject}'

class DeltaCalculation(TimeCreator):

    def __init__(self, end_time):
        super().__init__(subject, start_time)
        self.end_time = end_time





