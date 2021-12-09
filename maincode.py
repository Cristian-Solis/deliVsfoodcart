"""
Name:  Cristian Solis
Email: cristian.solis79@myhunter.cuny.edu
Resources: https://stackoverflow.com/questions/5807195/how-to-get-coordinates-of-address-from-python, https://www.geeksforgeeks.org/python-plotting-google-map-using-folium-package/?ref=lbp, https://stackoverflow.com/questions/11350770/filter-pandas-dataframe-by-substring-critera, https://www.geeksforgeeks.org/python-plotting-google-map-using-gmplot-package/?ref=lbp, program 15, program 25, Rahul, Dan and classmates reminding me of past assignments that may be useful for aggregating data
"""

from geopy.geocoders import Nominatim
import numpy as np
import pandas as pd
import folium as fml
import pandasql as psql
import gmplot

### Functions that do what the dew could not do
def addressToCoords(df):
    geolocator = Nominatim(user_agent="school")
    lat = pd.Series(dtype=object)
    lon = pd.Series(dtype=object)
    for x in df['location']:
        tempLoc = geolocator.geocode(x)
        print(tempLoc)
    df = df.assign(Latitude = lat)
    df = df.assign(Longitude = lon)
    return df

def cartSpecificDF(df):
    return df[(df['type_name'].str.contains('Food Cart'))|(df['type_name'].str.contains('Food Cart'))]

def deliSpecificDF(df):
    return df[(df['Store Name'].str.contains('DELI'))|(df['Store Name'].str.contains('Deli'))]

def graf(df):
    return df

def computeLocationNum(df, cName, val):
    leCounter = df[cName].str.count(val)
    return leCounter.sum()

### Reading Files
deliStartDf = pd.read_csv('Recognized_Shop_Healthy_Stores.csv')
freshZone = pd.read_csv('DCP_nyc_freshzoning.csv')
foodCarto = pd.read_json('DPR_Eateries_001.json', dtype=dict)
foodCarto = pd.DataFrame(foodCarto)

### Manipulating said files
deliCoords = deliSpecificDF(deliStartDf)
foodCarto = cartSpecificDF(foodCarto)
cartCoords = addressToCoords(foodCarto)

### Crunching numbers
numDeli = computeLocationNum(deliStartDf, 'Store Name', 'Deli') + computeLocationNum(deliStartDf, 'Store Name', 'DELI')
numFoodCart = computeLocationNum(foodCarto, 'type_name', 'Food Cart')
numGroceries = computeLocationNum(deliStartDf, 'Store Name','Grocery') + computeLocationNum(deliStartDf, 'Store Name','GROCERY')
numAllCarts = computeLocationNum(foodCarto, 'type_name', 'Cart')

### Grafing


### Test Outputs
print(foodCarto)
print(f'{numDeli} vs {numFoodCart}')
print(f'{numGroceries} vs {numAllCarts}')
