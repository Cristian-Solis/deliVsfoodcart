"""
Name:  Cristian Solis
Email: cristian.solis79@myhunter.cuny.edu
Resources: https://stackoverflow.com/questions/43892459/check-if-geo-point-is-inside-or-outside-of-polygon, program 15, program 17, program 25, and classmates reminding me of past assignments that may be useful for aggregating data
"""

import numpy as np
import pandas as pd
# from shapely.geometry import Point
# from shapely.geometry.polygon import Polygon

def uniqueLocations(place):
    uniquePlaces, otherPlaces= np.unique(place, return_counts=True)
    mass = [x/len(place) for x in otherPlaces]
    return uniquePlaces, mass

def graf(df):
    # lons_lats_vect = np.column_stack((lons_vect, lats_vect)) # Reshape coordinates
    # polygon = Polygon(lons_lats_vect) # create polygon
    # point = Point(y,x) # create point
    return df

def computeLocationNum(df, cName, val):
    leCounter = df[cName].str.count(val)
    return leCounter.sum()

recogSHS = pd.read_csv('Recognized_Shop_Healthy_Stores.csv')
freshZone = pd.read_csv('DCP_nyc_freshzoning.csv')
wildCard = pd.read_json('DPR_Eateries_001.json')

numDeli = computeLocationNum(recogSHS, 'Store Name', 'Deli') + computeLocationNum(recogSHS, 'Store Name', 'DELI')
numFoodCart = computeLocationNum(wildCard, 'type_name', 'Food Cart')

numGroceries = computeLocationNum(recogSHS, 'Store Name','Grocery') + computeLocationNum(recogSHS, 'Store Name','GROCERY')
numAllCarts = computeLocationNum(wildCard, 'type_name', 'Cart')
print(f'{numDeli} vs {numFoodCart}')
print(f'{numGroceries} vs {numAllCarts}')