import os,sys,shutil
sys.path.append(os.path.abspath('..'))
from backtester.timeRule.time_rule import TimeRule
import pytest

def test_timerule():
        timerule=TimeRule()
        with pytest.raises(NotImplementedError):
                TimeRule.emitTimeToTrade(timerule)