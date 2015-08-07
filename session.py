#
class Session:
    """

    Session object
    """

    def __init__(self, ir):
        self.classification = {'event': 'getStandings', 'data': []}
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
            s = self.fix_driver_laptime(str(s))

            self.classification['data'].append({
                'CarIdx': driver['CarIdx'],
                'Position': driver['Position'],
                'FastestTime': '{}:{}'.format(int(m), s),
                'UserName': self.get_driver_name(driver['CarIdx'])
            })

    def get_driver_name(self, idx):
        # TODO make a Driver class?
        for driver in self.ir['DriverInfo']['Drivers']:
            if driver['CarIdx'] == idx:
                return driver['UserName']

    def fix_driver_laptime(self, second):
        """
        :param second: str
        :return: str

        irsdk sometimes gives laptime data like this: '106.34'
        here I just add a zero because I think iracing omits it.
        # TODO test this.
        """
        if len(second) > 5:
            return second[:6]
        else:
            return second[:5] + '0'
