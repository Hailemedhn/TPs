import random
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def calculate_radius_3():   
    pos = []
    avg = []
    for j in range(0,100): # num est le max N pour le graph
        x_c,y_c,z_c = 0,0,0
        for k in range(10): # average sur 10 iterations
            for i in range(0,j): # j == N dans l'enonce
                plus = random.choice([-1,1])
                axes = random.choice(["x","y","z"])
                match axes:
                    case "x":
                        x_c += plus                
                    case "y":
                        y_c += plus                    
                    case "z":
                        z_c += plus
            
            avg.append(np.sqrt((x_c**2) + (y_c**2) + (z_c**2))) 
        pos.append(np.average(avg))
    pos_1 = hit_zero_1()
    plt.plot([i for i in range (100)], pos_1,label="d = 1")
    pos_2 = hit_zero_2(0,0)
    plt.plot([i for i in range (100)], pos_2,label="d = 2")
    plt.plot([i for i in range (100)], pos,label="d = 3")
    pos_4 = calculate_radius_4()
    plt.plot([i for i in range(100)], pos_4,label="d = 4") 
    pos_5 = calculate_radius_5()
    plt.plot([i for i in range(100)], pos_4,label="d = 5") 
    pos_6 = calculate_radius_6()
    plt.plot([i for i in range(100)], pos_4,label="d = 6") 
    plt.xlabel("N")
    plt.ylabel("Distance Moyenne")
    plt.title("Radius Moyenne pour Dimensions differents.")
    plt.legend()

    plt.show()
    
    return pos


def calculate_radius_4():   
    pos = []
    avg = []
    for j in range(0,100): # num est le max N pour le graph
        x_c,y_c,z_c,a_c = 0,0,0,0
        for k in range(10): # average sur 10 iterations
            for i in range(0,j): # j == N dans l'enonce
                plus = random.choice([-1,1])
                axes = random.choice(["x","y","z","a"])
                match axes:
                    case "x":
                        x_c += plus                
                    case "y":
                        y_c += plus                    
                    case "z":
                        z_c += plus                   
                    case "a":
                        a_c += plus
            
            avg.append(np.sqrt((x_c**2) + (y_c**2) + (z_c**2) + (a_c**2))) 
        pos.append(np.average(avg))
    return pos

def calculate_radius_5():   
    pos = []
    avg = []
    for j in range(0,100): # num est le max N pour le graph
        x_c,y_c,z_c,a_c,b_c = 0,0,0,0,0
        for k in range(10): # average sur 10 iterations
            for i in range(0,j): # j == N dans l'enonce
                plus = random.choice([-1,1])
                axes = random.choice(["x","y","z","a","b"])
                match axes:
                    case "x":
                        x_c += plus                
                    case "y":
                        y_c += plus                    
                    case "z":
                        z_c += plus                   
                    case "a":
                        a_c += plus                  
                    case "b":
                        b_c += plus
            
            avg.append(np.sqrt((x_c**2) + (y_c**2) + (z_c**2) + (a_c**2) + (b_c**2))) 
        pos.append(np.average(avg))
    return pos

def calculate_radius_6():   
    pos = []
    avg = []
    for j in range(0,100): # num est le max N pour le graph
        x_c,y_c,z_c,a_c,b_c,c_c = 0,0,0,0,0,0
        for k in range(10): # average sur 10 iterations
            for i in range(0,j): # j == N dans l'enonce
                plus = random.choice([-1,1])
                axes = random.choice(["x","y","z","a","b","c"])
                match axes:
                    case "x":
                        x_c += plus                
                    case "y":
                        y_c += plus                    
                    case "z":
                        z_c += plus                   
                    case "a":
                        a_c += plus                    
                    case "b":
                        b_c += plus                   
                    case "c":
                        c_c += plus
            
            avg.append(np.sqrt((x_c**2) + (y_c**2) + (z_c**2) + (a_c**2+ (b_c**2) + (c_c**2)))) 
        pos.append(np.average(avg))
    return pos

def hit_zero_1():   
    pos = []
    avg = []
    for j in range(0,100): # num est le max N pour le graph
        x_c = 0
        for k in range(100): # average sur 100 iterations
            for i in range(0,j): # j == N dans l'enonce
                plus = random.choice([-1,1])
                x_c += plus         
            
            avg.append(x_c)
            x_c = 0 
        pos.append(np.sum(avg)/1000.0)
        avg = avg[0:0]
    return pos


def hit_zero_2(x,y):
    pos = []
    avg = []
    for j in range(0,100): # num est le max N pour le graph
        x_c,y_c,z_c = 0,0,0
        for k in range(10): # average sur 10 iterations
            for i in range(0,j): # j == N dans l'enonce
                plus = random.choice([-1,1])
                axes = random.choice(["x","y"])
                match axes:
                    case "x":
                        x_c += plus                
                    case "y":
                        y_c += plus  
            
            avg.append(np.sqrt((x_c**2) + (y_c**2))) 
        pos.append(np.average(avg))

    return pos




def hit_zero_3(x,y,z):
    x_c,y_c,z_c = 3,3,3 # le position ou la marcheuse commence et essaye d'arriver à (0,0,0)
    count = 0
    for i in range(1000000): # j == N dans l'enonce
        plus = random.choice([-1,1])
        axes = random.choice(["x","y","z"])
        match axes:
            case "x":
                x_c += plus                
            case "y":
                y_c += plus               
            case "z":
                z_c += plus     
        if x_c == x and y_c == y and z_c == z:
            count  += 1
    return count

def loi_SN():
    """La loi de SN en 3D"""
    X,Y,Z,N = 0,0,0,0
    y_plot = []
    for i in range(100):
        plus = random.choice([-1,1])
        axes = random.choice(["x","y","z"])
        match axes:
            case "x":
                X += plus                
            case "y":
                Y += plus               
            case "z":
                Z += plus 

        N += 1 
        y_plot.append(math.factorial(N)/(math.factorial((Y+N)//2) * math.factorial((N-Y)//2) *math.factorial((X+N)//2) * math.factorial((N-X)//2) * math.factorial((Z+N)//2)* math.factorial((N-Z)//2)) * (1/6)**N)
    plt.plot(list(range(100)),y_plot,label="Loi de SN")
    plt.xlabel("N") 
    plt.ylabel("P(SN=X)")
    plt.title("La loi de SN en 3D.")
    plt.show()

loi_SN()
calculate_radius_3()
print("Le nombre de fois où une marcheruse aleatoire arrive à l'origine à partir (3,3,3) en 3D = ",hit_zero_3(0,0,0)) #Simulation qui motre que si le marcheruse aleatoire est à (3,3,3) il ne quasiment peut pas retourner à (0,0,0)