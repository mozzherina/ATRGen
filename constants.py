import pandas as pd

pdSeries = pd.core.series.Series
pdFrame = pd.core.frame.DataFrame
pdDateTime = pd.Timestamp

Timeframe = str
TIMEFRAME_MIN5 = '5T'
TIMEFRAME_MIN15 = '15T'
TIMEFRAME_HOUR = 'H' 
TIMEFRAME_DAY = 'D'
TIMEFRAME_MONTH = 'M'

FINAM_DATETIME = '%Y%m%d%H%M%S'
AV_DATETIME = '%Y-%m-%d %H:%M:%S'
STD_DATE = '%Y-%m-%d'
STD_DATETIME = '%Y-%m-%d %H:%M'

BAR_SIZE = 5
BAR_SIZE_NARROW = 1
MARKER_SIZE = 15
FIGURE_SIZE = (15, 11)