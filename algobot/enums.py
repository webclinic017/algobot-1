"""
Enum classes and constants.
"""

BULLISH = "Bullish"
BEARISH = "Bearish"
ENTER_LONG = "Enter Long"
EXIT_LONG = "Exit Long"
ENTER_SHORT = "Enter Short"
EXIT_SHORT = "Exit Short"

TRENDS = [ENTER_LONG, EXIT_LONG, ENTER_SHORT, EXIT_SHORT]
ALL_TRENDS = {*TRENDS, BULLISH, BEARISH}


class GraphType:
    """
    Graph type enums.
    """
    # pylint: disable=too-few-public-methods
    NET = "NET"
    AVG = "AVG"


LONG = "Long"
SHORT = "Short"

TRAILING = "Trailing"
STOP = "Stop"

BACKTEST = "Backtest"
SIMULATION = "Simulation"
LIVE = "Live"
OPTIMIZER = "Optimizer"
