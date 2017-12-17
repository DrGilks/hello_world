'''
Created on 17 Dec 2017

@author: Daniel
'''


import random 
import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy as np



def create_city_frame():
    #Generate Set of Cities 
    num_cities=5+int(math.floor(10.0*random.random()))
    print("Number of Cities: " + str(num_cities))
    
    temp_city_frame=pd.DataFrame()
    
    for i in range(num_cities):
        single_city={"city_index":int(i),
                     "x":random.random(),
                     "y":random.random()}
        
        temp_city_frame=temp_city_frame.append(single_city,ignore_index=True)
    return(temp_city_frame)

def map_random_solution(df,step_dict):
    
    
    
    return(df)

def create_random_solve(df):
    
    city_indexs=list(df['city_index'].unique())
    print(type(city_indexs))
    
    step_dictionary={}
    
    city_1_first=int(city_indexs.pop())
    city_1=int(city_1_first)
    city_2=int(city_indexs.pop())
    
    for i in range(len(df)):
        if(i<len(df)-2):
            step_dictionary[i]=(city_1,city_2)
            city_1=int(city_2)
            city_2=int(city_indexs.pop())
        else:
            step_dictionary[i]=(city_1,city_1_first)
        
    df=map_random_solution(df,step_dictionary)    
    
    
    return(df)
    

def plot_cities(frame,fig_num):
    plt.figure(fig_num,figsize=(8,8))
    plt.scatter(frame['x'],frame['y'])
    plt.xlim(0,1)
    plt.ylim(0,1)

city_frame=create_city_frame()

plot_cities(city_frame,1)

city_frame=create_random_solve(city_frame)

plt.show()
plt.close()