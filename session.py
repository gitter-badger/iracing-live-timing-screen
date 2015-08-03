#
class Session:
    """
    Session object
    """

    def __init__(self, ir):
        self.classification = {'event': 'ping', 'data': []}
        self.ir = ir

    def session_state_qualify(self):
        """
        :return: True if  iRacing session state is Qualify or Lone Qualify
        """
        if "Qualify" in self.ir['SessionInfo']['Sessions'][self.ir['SessionNum']]['SessionType']:
            return True
        else:
            return False

    def update_classification(self):
        for idx, driver in enumerate(self.ir['SessionInfo']['Sessions'][0]['ResultsPositions']):
            m, s = divmod(driver['FastestTime'], 60)

            self.classification['data'].append({
                'CarIdx': driver['CarIdx'],
                'Position': driver['Position'],
                'FastestTime': '{}:{}'.format(int(m), str(s)[:6]),
            })