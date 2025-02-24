import networkx as nx
import matplotlib.pyplot as plt
import sys
import os
import pandas as pd

Base='C:/VKHCG'
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
sInputFileName='01-Retrieve/01-EDS/02-Python/Retrieve_Router_Location.csv'
sOutputFileName='Assess-DAG-Company-GPS.png'
Company='01-Vermeulen'
### Import Company Data
sFileName=Base + '/' + Company + '/' + sInputFileName
print('################################')
print('Loading :',sFileName)
print('################################')
CompanyData=pd.read_csv(sFileName,header=0,low_memory=False, encoding="latin-1")
print('Loaded Company :',CompanyData.columns.values)
print('################################')
print(CompanyData)
print('################################')
print('Rows : ',CompanyData.shape[0])
print('################################')
G=nx.Graph()
for i in range(CompanyData.shape[0]):
 nLatitude=round(CompanyData['Latitude'][i],2)
 nLongitude=round(CompanyData['Longitude'][i],2)

 if nLatitude < 0:
     sLatitude = str(nLatitude*-1) + ' S'
 else:
     sLatitude = str(nLatitude) + ' N'

 if nLongitude < 0:
     sLongitude = str(nLongitude*-1) + ' W'
 else:
     sLongitude = str(nLongitude) + ' E'

 sGPS= sLatitude + '-' + sLongitude
 G.add_node(sGPS)
print('################################')
for n1 in G.nodes():
 for n2 in G.nodes():
     if n1 != n2:
         print('Link :',n1,' to ', n2)
         G.add_edge(n1,n2)
print('################################')

print('################################')
print("Nodes of graph: ")
print(G.number_of_nodes())

print("Edges of graph: ")
print(G.number_of_edges())
print('################################')
