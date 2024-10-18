#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 22:59:48 2024

Based on a list of real numbers where consecutive numbers are equal to or greater than the previous one,
it generates a list where consecutive numbers are always greater than the previous one.
When it finds a group of equal numbers, it modifies their values, generating regular spacing between 
that value and the next greater number.

Example:
[1,2,2,2,2,5,6,6,6,8] --> [1, 2, 2.75, 3.50, 4.25, 5, 6, 6.667, 7.334, 8]

Input:
A table in a text file, where the first column is the aforementioned list.
The first row is considered the header.

Output:
The same table as the input, but adding the modified list in the last column.


@author: pablo
"""

import numpy as np
import csv

file_name = 'Interpolate_lists_input-data-example.csv'  # Indicate the input file name
delimiter = ','						# Indicate the delimiter

def main():
    data = np.genfromtxt(file_name, dtype='str', delimiter=delimiter) # Reading the file and retrieving data
    data_i = data[2:] # Remove the header

    list_out = ['Dist_mod', data[1][0]] #Initialize the list with the modified distance


    i = 0
    k = 1
    b = data[1][0] #first data
    for dato in data_i: #Loop through the data
        i += 1 
        if dato[0] != b: #If the value changes, save the distance(s)
            if k == 1:      #Save a unique distance value
                list_out.append(dato[0])
                b = dato[0]
                k = 1
            else: 	#Interpolate data between a minimum value (old distance, b) and 
    			#a maximum (new distance, dato[0]), with k+1 elements.
                new_dist = np.linspace(float(b), float(dato[0]), k+1) #Interpolated data in a list
                list_out.extend(new_dist[1:])
                k=1
                b = dato[0]
		    
        else:
            k += 1

    data_list=np.ndarray.tolist(data) 

	# Adding the modified list as the last column of the initial table
    for d, d_m in zip(data_list, list_out):
	    d.append(d_m)


	# Saving a txt file
    file_out = open(file_name[:-4]+'_mod.txt', 'w')
    writer = csv.writer(file_out, delimiter=delimiter, lineterminator='\r\n')
    for row in data_list:
        writer.writerow(row)
    del writer
    file_out.close()
	
main()
