import matplotlib.pyplot as plt
import numpy as np
import urllib
import urllib2

import matplotlib.dates as mdates

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter


def graph_data():

    fig = plt.figure()
    ax_1 = plt.subplot2grid((1, 1), # Plot grid
                            (0, 0)) # Starting point of plot

    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source[1:]:
        stock_data.append(line)


    # adjustedp = adjusted close price
    date, closep, highp, lowp, openp, adjustedp, volume \
        = np.loadtxt(stock_data, delimiter=',', unpack=True,
                     # %Y = full year: 2015
                     # %y = partial year: 15
                     # %m = number of month
                     # %d = number of day
                     # %H = hours
                     # %M = minutes
                     # %S = seconds
                     converters={0: bytespdate2num('%Y-%m-%d')})

    ax_1.plot_date(date, closep, '-', label='Price')

    for label in ax_1.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax_1.grid(True, color='g', linestyle='--')

    ax_1.set_xlabel('date')
    ax_1.set_ylabel('price')

    ax_1.set_title('Price of stocks')
    ax_1.legend()
    fig.subplots_adjust(left=0.1, bottom=0.20, right=0.94, top=0.95,
                       wspace=0.2, hspace=0)
    fig.show()


graph_data()
