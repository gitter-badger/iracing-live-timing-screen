#
import irsdk

SESSION_STATE_QUALIFY = "Qualify"
SESSION_STATE_RACE = "Race"

ir = irsdk.IRSDK(test_file='data.bin')
ir.startup()
