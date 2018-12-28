import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates

def graph_data(stock):

  stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'

  source_code = urllib.request.urlopen(stock_price_url).read().decode()

  stock_data = []
  split_source = source_code.split('\n')

  for line in split_source:
    split_line = line.split('')
    if len(split_line) == 6:
      if 'values' not in line:
        stock_data.append(line)

  date, closep,highp, lowp,openp,volume = np.loadtxt(stock_data,
                                                     delimiter = ',',
                                                     unpack = True,
                                                     converters = {0: bytespdate2num('%Y%m%d')})

  plt.xlabel('x')
  plt.ylabel('y')
  plt.title('cool graph')
  plt.legend()
  plt.show()

graph_data('TSLA')
