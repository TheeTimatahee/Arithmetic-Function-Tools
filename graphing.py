from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import numberTheoryTools as ntt
import time
import plotly.plotly as py
import plotly.graph_objs as go


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
        y.append(#Replace this portion of the code with whatever arithmetic function you wish to map to a graph#)
    return y
startTime = float(time.time())

n = 1000
x = list(range(1,(n+1)))
y = makeY(n,x)

trace = go.Scatter(x=x,y=x,name='YEET')
data = [trace]
layout = dict(title='Number Theory Graph',xaxis=dict(title='n'),yaxis=dict(title='f(n)'))
fig = dict(data=data,layout=layout)

plot(fig)

(h,m,s) = secToHMS((float(time.time())) - startTime)
print("Time taken to output: " + h + ":" + m + ":" + s)
