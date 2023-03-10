
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 17:47:00 2022

@author: Dante Dagandanan
"""

import tkinter as tk
from tkinter import ttk
import serial
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import numpy as np
import pandas as pd
import csv



class App:
    def __init__(self, root):
        # Set up the serial connection to the Spectral Triad
        try:
            self.ser = serial.Serial('COM5', 115200)
            time.sleep(2)
        except serial.serialutil.SerialException:
            print("Error: Could not connect to the device.")
            
        self.root=root
        self.captured_NIR = []
        
        self.root.geometry("1000x700") #width x height
        self.root.resizable(False, False)

        # Set up the GUI
        # Create left and right frames
        self.left_frame=tk.Frame(root,  width=10,  height=  400,  bg='grey',highlightbackground='red',highlightthickness=3)
        self.left_frame.grid(row=0,  column=0,  padx=10,  pady=5)
        
        self.left_frame_bottom=tk.Frame(root,  width=10,  height=  400,  bg='white',highlightbackground='red',highlightthickness=3)
        self.left_frame_bottom.grid(row=1,  column=0,  padx=10,  pady=5)
        
        self.right_frame  =  tk.Frame(root,  width=300,  height=300,  bg='grey',highlightbackground='red',highlightthickness=3)
        self.right_frame.grid(row=0,  column=1,  padx=10,  pady=5)
        
        self.right_frame_bottom  =  tk.Frame(root,  width=300,  height=300,  bg='grey',highlightbackground='red',highlightthickness=3)
        self.right_frame_bottom.grid(row=1,  column=1,  padx=10,  pady=5)
       
        # Set up the plot for the intensity readings
        self.wavelengths = [410, 435, 460, 485, 510, 535, 560, 585, 610, 645, 680, 705, 730, 760, 810, 860, 900, 940]
        self.intensities = [0] * 18
        ###################################################################################
        
        self.image = tk.PhotoImage(file='C:/Users/PRO/Downloads/purepng.com-jackfruitfruitsjackfruitjakfruitjackjak-9815251836382omag (1).png')
        self.image = self.image.subsample(3, 3)
        self.label = tk.Label(self.right_frame, image=self.image)
        self.label.pack()
        
        self.image1 = tk.PhotoImage(file='C:/Users/PRO/Downloads/purepng.com-jackfruitfruitsjackfruitjakfruitjackjak-9815251836382omag (1).png')
        self.image1 = self.image1.subsample(3, 3)
        self.label1 = tk.Label(self.right_frame_bottom, image=self.image1)
        self.label1.pack()
        
        ##############################################################################
        services = []
        
        def showInfo(selected_checkbox_index):
            for i in range(len(services)):
                # Disable all checkboxes except for the selected one
                if i != selected_checkbox_index:
                    services[i].set(0)
                else:
                    if services[i].get() == 0:
                        # Enable all checkboxes if the selected one is unchecked
                        for j in range(len(services)):
                            services[j].set(1)
                    else:
                        # Show selected checkbox information
                        selected = str(i)
                        #tk.messagebox.showinfo(message="You selected Checkbox " + selected)  
        
        services = []
        for i in range(15):
            option = tk.StringVar()
            option.set(0)
            services.append(option)
        
        tk.Checkbutton(self.right_frame, text= "1", variable=services[0], command=lambda: showInfo(0)).place(x=35,y=100)
        tk.Checkbutton(self.right_frame, text= "2", variable=services[1], command=lambda: showInfo(1)).place(x=35,y=150)
        tk.Checkbutton(self.right_frame, text= "3", variable=services[2], command=lambda: showInfo(2)).place(x=100,y=60)
        tk.Checkbutton(self.right_frame, text= "4", variable=services[3], command=lambda: showInfo(3)).place(x=100,y=120)
        tk.Checkbutton(self.right_frame, text= "5", variable=services[4], command=lambda: showInfo(4)).place(x=100,y=180)
        tk.Checkbutton(self.right_frame, text= "6", variable=services[5], command=lambda: showInfo(5)).place(x=180,y=30)
        tk.Checkbutton(self.right_frame, text= "7", variable=services[6], command=lambda: showInfo(6)).place(x=180,y=90)
        tk.Checkbutton(self.right_frame, text= "8", variable=services[7], command=lambda: showInfo(7)).place(x=180,y=150)
        tk.Checkbutton(self.right_frame, text= "9", variable=services[8], command=lambda: showInfo(8)).place(x=180,y=210)
        tk.Checkbutton(self.right_frame, text= "10", variable=services[9], command=lambda: showInfo(9)).place(x=250,y=50)
        tk.Checkbutton(self.right_frame, text= "11", variable=services[10], command=lambda: showInfo(10)).place(x=250,y=120)
        tk.Checkbutton(self.right_frame, text= "12", variable=services[11], command=lambda: showInfo(11)).place(x=250,y=200)
        tk.Checkbutton(self.right_frame, text= "13", variable=services[12], command=lambda: showInfo(12)).place(x=320,y=70)
        tk.Checkbutton(self.right_frame, text= "14", variable=services[13], command=lambda: showInfo(13)).place(x=320,y=160)
        tk.Checkbutton(self.right_frame, text= "15", variable=services[14], command=lambda: showInfo(14)).place(x=360,y=120)



        ############################################################################################
        services = []
        
        def showInfo(selected_checkbox_index):
            for i in range(len(services)):
                # Disable all checkboxes except for the selected one
                if i != selected_checkbox_index:
                    services[i].set(0)
                else:
                    if services[i].get() == 0:
                        # Enable all checkboxes if the selected one is unchecked
                        for j in range(len(services)):
                            services[j].set(1)
                    else:
                        # Show selected checkbox information
                        selected = str(i)
                        #tk.messagebox.showinfo(message="You selected Checkbox " + selected)  
        
        services = []
        for i in range(15):
            option = tk.StringVar()
            option.set(0)
            services.append(option)
        
        tk.Checkbutton(self.right_frame_bottom, text= "16", variable=services[0], command=lambda: showInfo(0)).place(x=35,y=100)
        tk.Checkbutton(self.right_frame_bottom, text= "17", variable=services[1], command=lambda: showInfo(1)).place(x=35,y=150)
        tk.Checkbutton(self.right_frame_bottom, text= "18", variable=services[2], command=lambda: showInfo(2)).place(x=100,y=60)
        tk.Checkbutton(self.right_frame_bottom, text= "19", variable=services[3], command=lambda: showInfo(3)).place(x=100,y=120)
        tk.Checkbutton(self.right_frame_bottom, text= "20", variable=services[4], command=lambda: showInfo(4)).place(x=100,y=180)
        tk.Checkbutton(self.right_frame_bottom, text= "21", variable=services[5], command=lambda: showInfo(5)).place(x=180,y=30)
        tk.Checkbutton(self.right_frame_bottom, text= "22", variable=services[6], command=lambda: showInfo(6)).place(x=180,y=90)
        tk.Checkbutton(self.right_frame_bottom, text= "23", variable=services[7], command=lambda: showInfo(7)).place(x=180,y=150)
        tk.Checkbutton(self.right_frame_bottom, text= "24", variable=services[8], command=lambda: showInfo(8)).place(x=180,y=210)
        tk.Checkbutton(self.right_frame_bottom, text= "25", variable=services[9], command=lambda: showInfo(9)).place(x=250,y=50)
        tk.Checkbutton(self.right_frame_bottom, text= "26", variable=services[10], command=lambda: showInfo(10)).place(x=250,y=120)
        tk.Checkbutton(self.right_frame_bottom, text= "27", variable=services[11], command=lambda: showInfo(11)).place(x=250,y=200)
        tk.Checkbutton(self.right_frame_bottom, text= "28", variable=services[12], command=lambda: showInfo(12)).place(x=320,y=70)
        tk.Checkbutton(self.right_frame_bottom, text= "29", variable=services[13], command=lambda: showInfo(13)).place(x=320,y=160)
        tk.Checkbutton(self.right_frame_bottom, text= "30", variable=services[14], command=lambda: showInfo(14)).place(x=360,y=120)



        ############################################################################################
        
        # Add a button to start measurement
        self.measure_button = tk.Button(self.left_frame_bottom, text='Start Measurement', command=self.pressed_button)
        self.measure_button.pack(side=tk.LEFT, padx=50, pady=50)
        
        ########################################################################################
        y1=40 #increment
        y2=20 #intial position
        x1=780 
        fontz=13
        
        # Create a frame to hold the list of images
        self.image_list_frame = tk.Frame(self.left_frame)
        self.image_list_frame.pack(side=tk.LEFT)
        
        # Create a vertical scrollbar for the list of images
        self.scrollbar = tk.Scrollbar(self.image_list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
        # Create a listbox to display the captured images
        self.image_list = tk.Listbox(self.image_list_frame, yscrollcommand=self.scrollbar.set)
        self.image_list.config(width=70, height=20)
        self.image_list.pack(side=tk.RIGHT, fill=tk.BOTH)
        
        # Set the scrollbar's command to scroll the listbox
        self.scrollbar.config(command=self.image_list.yview)
        options = ["sensor 1", "sensor 2", "sensor 3"]
        #options = [1,2,3]
        self.current_var = tk.StringVar()
        self.current_var.set(options[0])
        
        ############################################################
        
        
        self.drop = ttk.OptionMenu(self.left_frame_bottom,self.current_var,*options)
        self.drop.pack(side=tk.RIGHT, padx=50, pady=50)
        # Read the .csv file
        with open('readings.csv', 'r') as file:
            reader = csv.reader(file)
            # Loop through the rows of the .csv file
            for row in reader:
                # Insert each row into the Listbox
                self.captured_NIR=row
                self.image_list.insert(tk.END, row)
                self.image_list.yview(tk.END)

        
        
    def pressed_button(self):
        # Send the command to start measurement
        self.ser.write(b'o')
        
        # Read the intensity readings for each channel
        a = int(self.ser.readline().strip().decode('utf-8'))
        b = int(self.ser.readline().strip().decode('utf-8'))
        c = int(self.ser.readline().strip().decode('utf-8'))
        d = int(self.ser.readline().strip().decode('utf-8'))
        e = int(self.ser.readline().strip().decode('utf-8'))
        f = int(self.ser.readline().strip().decode('utf-8'))
        g = int(self.ser.readline().strip().decode('utf-8'))
        r = int(self.ser.readline().strip().decode('utf-8'))
        i = int(self.ser.readline().strip().decode('utf-8'))
        s = int(self.ser.readline().strip().decode('utf-8'))
        j = int(self.ser.readline().strip().decode('utf-8'))
        t = int(self.ser.readline().strip().decode('utf-8'))
        u = int(self.ser.readline().strip().decode('utf-8'))
        v = int(self.ser.readline().strip().decode('utf-8'))
        w = int(self.ser.readline().strip().decode('utf-8'))
        k = int(self.ser.readline().strip().decode('utf-8'))
        l = int(self.ser.readline().strip().decode('utf-8'))
    
        # Update the bar graph with the intensity readings
        self.intensities = [a,b,c,d,e,f,g,r,i,s,j,t,u,v,w,k,l]
        print(a,b,c,d,e,f,g,r,i,s,j,t,u,v,w,k,l)

    
        df = pd.DataFrame({'410': [a], '435': [b], '460': [c], '485': [d], '510': [e], '535': [f],
                   '560': [g], '585': [r], '610': [i], '645': [s], '680': [j], '705': [t],
                   '730': [u], '760': [v], '810': [w], '860': [k], '900': [l],"sensor":[str(self.current_var.get())]})
        
        # Save the dataframe to a CSV file
        df.to_csv('readings.csv', mode='a', header=False, index=False)
        self.captured_NIR=[str(self.intensities),self.current_var.get()]
        
        self.image_list.insert(tk.END,self.captured_NIR)
        self.image_list.yview(tk.END)
        
        

                
                



root = tk.Tk()
app = App(root)
root.mainloop()
