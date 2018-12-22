import re
import plotly
import plotly.graph_objs as go
from plotly import tools


def getName(line):
    result = re.split(r',', line, maxsplit=1)
    # name = re.findall(r'([A-Z][a-z]+\s{0,1})+',result[0])
    name = result[0].strip()
    return name[1:len(name)-2],result[1]

def getPosition(line):
    result = re.split(r',', line, maxsplit=1)
    position = re.search(r'([A-Z][a-z]+[\s-]{0,1})+',result[0]).group()
    return position,result[1]


def getAge(line):
    result = re.split(r',', line, maxsplit=1)
    age=re.search(r'\d+',result[0]).group()
    return age,result[1]


def getTeam_from(line):
    result = re.split(r',', line, maxsplit=1)
    # team_from = re.findall(r'(([A-Z]+){0,1})+[.]{0,1}[\s]{0,1}[A-Z][a-z]+\s{0,1}', result[0])
    team_from= result[0].strip()
    return team_from[1:len(team_from)-2], result[1]


try:
   with open('top250-00-19.csv', encoding="utf-8", mode='r') as file:


       file.readline()
       line_number = 1
       for line in file:
           line = line.strip().rstrip()
           line_number += 1
           if not line:
               continue


           name,line = getName(line)
           position, line = getPosition(line)
           age,line = getAge(line)
           team_from,line = getTeam_from(line)

           dataset={}

           if age not in dataset:
               dataset[age]= {}
           if team_from  not in dataset[age]:
               dataset[age][team_from] = {}
           if position not in dataset[age][team_from]:
               dataset[age][team_from][position]=[]
           if name not in dataset[age][team_from][position]:
               dataset[age][team_from][position].append(name)


except IOError as e:
   print ("I/O error({0}): {1}".format(e.errno, e.strerror))

except ValueError as ve:
    print("Value error {0} in line {1}".format(ve, line_number))

labels = ["Luís Figo","Hernán Crespo","Marc Overmars","Gabriel Batistuta","Claudio López","Sérgio Conceição"]
values = [27,25,27,31,25,25]

pie = go.Pie(labels=labels, values=values)

plotly.offline.plot([pie], filename='basic_pie_chart')
x=["Luís Figo","Hernán Crespo","Marc Overmars","Gabriel Batistuta","Claudio López","Sérgio Conceição"]
y=[27,25,27,31,25,25]

bar = go.Bar(
    x=x,
    y=y
)

scatter = go.Scatter(
    x=x,
    y=y
)

figure = tools.make_subplots(rows=2, cols=2)
figure.append_trace(bar, 1, 2)
figure.append_trace(scatter, 2, 2)


plotly.offline.plot(figure, filename='project.html')









