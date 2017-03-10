# -*- coding: utf-8 -*-
"""
Created on 10.03.2017

@summary:

@version: 0.1

@organization:  GEOCOM Informatik AG
@author:    Matthias Brunner

@change:

"""
import csv


# ----------------------------------------------------------------------------------------------------------------------
def open_csv_file(file_path):
    """
    :param file_path: Takes the file path
    :return data: Returns a list with all data
    """
    csv_data = {}
    with open("datei.csv", 'rb') as csv_file:
        csv_data = list(csv.reader(csv_file))

    return csv_data


# ----------------------------------------------------------------------------------------------------------------------
def analyse_data(data_pool):
    """
    :param data_pool: list with data to analyse
    :return:
    """
    # Bestimme die länge der list

    # range(start, end, inc)
    for i in range():
        print data_pool[i]


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    base_csv_file = r"C:\temp\testdata.csv"

    # Öffne die csv Datai
    open_csv_file()

    # Starte eine analyse der csv Datei
    analyse_data()

