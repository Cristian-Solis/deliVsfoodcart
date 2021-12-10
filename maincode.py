"""
Name:  Cristian Solis
Title: Deli Vs Food Cart
Email: cristian.solis79@myhunter.cuny.edu
Resources: https://geopy.readthedocs.io/en/stable/#nominatim,https://stackoverflow.com/questions/5807195/how-to-get-coordinates-of-address-from-python, https://www.geeksforgeeks.org/python-plotting-google-map-using-folium-package/?ref=lbp, https://stackoverflow.com/questions/11350770/filter-pandas-dataframe-by-substring-critera, https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html, https://stackoverflow.com/questions/20454120/how-to-remove-gaps-between-bars-in-matplotlib-bar-chart, program 15, program 25, Rahul, Dan and classmates reminding me of past assignments that may be useful for aggregating data
URL: https://github.com/WhosDerpy/deliVsfoodcart
"""

from geopy.geocoders import Nominatim
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import folium as fml

# Functions that do what the dew could not do
## finds coordinates from human directions/"locations" sometimes derps out and y'know that's what makes it special.
def addressToCoords(df):
    leng = []
    long = []
    for x in df['location']:
        geolocator = Nominatim(user_agent="tarea",timeout=None)
        location = geolocator.geocode(x)
        if location is not None:
            leng.append(location.latitude)
            long.append(location.longitude)
    return leng, long

## manipulates the dataframe to only include Food Carts
def cartSpecificDF(df):
    return df[(df['type_name'].str.contains('Food Cart'))|(df['type_name'].str.contains('Food Cart'))]

## dataframe gets changed to only have keywords DELI or Deli in it.
def deliSpecificDF(df):
    return df[(df['Store Name'].str.contains('DELI'))|(df['Store Name'].str.contains('Deli'))]

## Simple number crunching to figure out the total number of a given string.
def computeLocationNum(df, cName, val):
    leCounter = df[cName].str.count(val)
    return leCounter.sum()

# Reading Files
deliStartDf = pd.read_csv('Recognized_Shop_Healthy_Stores.csv')
freshZone = pd.read_csv('DCP_nyc_freshzoning.csv')
foodCarto = pd.read_json('DPR_Eateries_001.json', dtype=dict)
foodCarto = pd.DataFrame(foodCarto) # made into a dataframe after being made into a dictionary to make sure it doesn't combust

# Manipulating said files
## deli files
deliCoords = deliSpecificDF(deliStartDf)
deliCoords.dropna(subset=['Latitude'], inplace=True) # removing the NaNs so that they don't mess with the plotting later on
deliCoords.dropna(subset=['Longitude'], inplace=True) # making sure to remove EVERY NaN so that no errors pop up
delilat = list(deliCoords['Latitude']) # made into list for simpler interation (for me)
delilon = list(deliCoords['Longitude']) # same reason for it being made into a list, listed 1 line above.


## food cart files
foodCarto = cartSpecificDF(foodCarto)
cartCoordsLat, cartCoordsLon = addressToCoords(foodCarto) # grabbing whatever coordinates we can grab given the .json file

#Crunching numbers
## Deli
numDeli = computeLocationNum(deliStartDf, 'Store Name', 'Deli') + computeLocationNum(deliStartDf, 'Store Name', 'DELI')
numGroceries = computeLocationNum(deliStartDf, 'Store Name','Grocery') + computeLocationNum(deliStartDf, 'Store Name','GROCERY')

## Food Carts
numFoodCart = computeLocationNum(foodCarto, 'type_name', 'Food Cart')
numAllCarts = computeLocationNum(foodCarto, 'type_name', 'Cart')

# Grafing
normalMapu = fml.Map(location = [40.777190, -73.969219])

## deli
map_O_Deli = fml.Map(location = [40.777190, -73.969219])
for i in range(0,len(delilat)): # plotting all points for delis in the city
    fml.Marker([delilat[i], delilon[i]], popup = ' Deli ').add_to(map_O_Deli)
    fml.Marker([delilat[i], delilon[i]], popup = ' Deli ').add_to(normalMapu)

## carts
mpCarts = fml.Map(location = [40.777190, -73.969219])
for i in range(0,len(cartCoordsLon)): # going through the entire list to graphy the specific points of carts onto both the cart specific map and the main map
    fml.Marker([cartCoordsLat[i], cartCoordsLon[i]], popup = ' Food Cart ').add_to(mpCarts)
    fml.Marker([cartCoordsLat[i], cartCoordsLon[i]], popup = ' Food Cart ').add_to(normalMapu)

normalMapu.save("normalMap.html")
mpCarts.save("FoodCartsMap.html")
map_O_Deli.save("deliMap.html")

# Bar Grafs
colorsObars = ['purple','orange']
## deli vs Carts
firstComparison = [numDeli, numFoodCart]
oneGraf = plt.bar([0,2], height=firstComparison, tick_label=['Delis', 'Food Carts'], width=1, color=colorsObars)
plt.title('Number of Deli Vs. Food Cart')
plt.savefig('deliVcart.png')
plt.show()


## Grocery vs All Carts
secondComparions = [numGroceries, numAllCarts]
secondGraf = plt.bar([0,2], height=secondComparions, tick_label=['Groceries', 'All "Carts"'],width=1,color=colorsObars)
plt.title('Number of Grocery Vs. Carts')
plt.savefig('groceryVcart.png')
plt.show()
