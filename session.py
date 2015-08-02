#
from main import *


class Session():
    """
    Session object
    """

    def __init__(self, ir):
        self.classification = []
        self.ir = ir

    def session_state_qualify(self):
        """
        :return: True if session state is Qualify or Lone Qualify
        """
        if "Qualify" in ir['SessionInfo']['Sessions'][ir['SessionNum']]['SessionType']:
            return True
        else:
            return False

    def update_classification(self):
        for idx, driver in enumerate(self.ir['SessionInfo']['Sessions'][0]['ResultsPositions']):
            self.classification.append({
                'CarIdx': driver['CarIdx'],
                'FastestTime': driver['FastestTime'],
            })
            # print('{}:{}'.format(int(m), str(s)[:6]))
