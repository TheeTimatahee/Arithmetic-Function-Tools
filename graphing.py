#import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import numberTheoryTools as ntt
import time
# import numpy as np
# import pandas as pd
# import cufflinks as cf
import plotly.plotly as py
# import plotly.tools as tls
import plotly.graph_objs as go
# import webbrowser


def secToHMS(n):
    """Method for calculating the amount of time taken to output"""
    #Get the hours portion
    hours = int(n/3600)
    n -= hours*3600

    #If less then 10 add a 0; for purely aesthetic purposes
    if hours < 10:
        hours = "0" + str(hours)
    
    #Get minutes portion
    minutes = int(n/60)
    n -= minutes*60

    #If less then 10 add a 0; for purely aesthetic purposes
    if minutes < 10:
        minutes = "0" + str(minutes)
    
    #return str(hours) + ":" + str(minutes) + ":" + str(n)
    return (str(hours),str(minutes),str(n))

def makeY(n,x):
    y = []
    for i in x:
        y.append(ntt.dirichletProduct(ntt.tau,ntt.e,i))
    return y
startTime = float(time.time())

# tls.set_credentials_file(username="takilmer",api_key="gHKIftt9g3IgedzVLze1")

n = 1000
x = list(range(1,(n+1)))
y = makeY(n,x)
# n1 = 201
# x = np.linspace(0, 2.0*np.pi, n)
# y = np.sin(x)
# print(x)
# print(y)

trace = go.Scatter(x=x,y=x,name='YEET')
data = [trace]
layout = dict(title='Number Theory Graph',xaxis=dict(title='n'),yaxis=dict(title='f(n)'))
fig = dict(data=data,layout=layout)

#url = py.plot(fig,file='graph')
#url = py.plot(data)
#print(str(url))

# webbrowser.open(str(url))
plot(fig)

(h,m,s) = secToHMS((float(time.time())) - startTime)
print("Time taken to output: " + h + ":" + m + ":" + s)


# n = 1000
# x = list(range(1,(n+1)))


plot([go.Scatter(x=x, y=y)])