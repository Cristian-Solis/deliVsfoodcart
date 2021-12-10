# Deli Vs. Food Cart
$10 in our pocket. Aight, where to go to eat? the food cart or the deli. 

### baconeggandcheese or gyro? 

<img src="https://static01.nyt.com/images/2015/04/15/dining/15BREAKFAST_SUB/15BREAKFAST_SUB-superJumbo.jpg" width = "250"> <img src="https://howtofeedaloon.com/wp-content/uploads/2020/06/gryo-instagram.jpg" width="250" height="165"> 
### a hero or chicken over rice?
<img src="https://www.aviglatt.com/imagesc//deluxe-t.jpg_H1782.jpg" width ="250" height="165"> <img src="https://stuarte.co/wp-content/uploads/2019/10/Halal-cart-chicken-packed-with-rice-and-sauce-1.jpg" width= "250" height="165">

## Overview
I wanted to find out a map of all delis/groceries originally and look. However, the dataset being limited I decided to pin food carts against the original deli idea. I was able to find two data sets but each had their own challenges. Trying to use all sorts of methods to extract and manipulating the data: from numpy, psql, to even folium/gmplot (though i soon found out gmplot requires payment so I quickly switched over to only folium).

### Maps
#### Deli Map
<img src="https://github.com/WhosDerpy/deliVsfoodcart/blob/main/Images/delimap.png" width = "450"> 

#### Food Cart Map
<img src="https://github.com/WhosDerpy/deliVsfoodcart/blob/main/Images/foodcartmap.png" width = "450"> 

#### Combined Map
<img src="https://github.com/WhosDerpy/deliVsfoodcart/blob/main/Images/combinedmap.png" width = "450"> 

### Graphs
<img src="https://github.com/WhosDerpy/deliVsfoodcart/blob/main/Images/deliVcart.png" width = "400"> <img src="https://github.com/WhosDerpy/deliVsfoodcart/blob/main/Images/groceryVcart.png" width = "400">

## Data
 A challenge they both share is that the dataset is very limiting. Had to use geopy to get coordinates for `DPR_Eateries_001.json` because there were no coordinates. Ontop of that a lot of the instructions were human instructions so only some of the points were able to be used. My second dataset was easier though and I was able to breeze through it due to the lessons learned in 39542. Such as only picking rows that contained the word 'Deli'/'DELI' in it. Afterwards it was as easy as taking out the latitude/longitude columns from the data frame and plotting all points on a folium map.

## Techinque!
Looking at how I can use previous assignments to manipulate my data. Taking inspirations from assignments 17, 15, and 28. As well as browsing our assignment page to see how i can further help out my data and visualizations. Had to automate finding coordinates because my .json file didn't have any (even though on the page it said it did. it didn't). Singled out rows that contained keywords and made that the primary dataframe. Manipulted matplotlib values to make sure my graphs were presentable.

## Citations
### Code related links (refreshers to me)
1. https://geopy.readthedocs.io/en/stable/#nominatim,https://stackoverflow.com/questions/5807195/how-to-get-coordinates-of-address-from-python
2. https://www.geeksforgeeks.org/python-plotting-google-map-using-folium-package/?ref=lbp
3. https://stackoverflow.com/questions/11350770/filter-pandas-dataframe-by-substring-critera
4. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html
5. https://stackoverflow.com/questions/20454120/how-to-remove-gaps-between-bars-in-matplotlib-bar-chart

### Youtube video that helped me make this page
- https://www.youtube.com/watch?v=hHbWF1Bvgf4
    - just taught me how to generally style images

### CSVs/Data
1. https://data.cityofnewyork.us/Recreation/Directory-of-Eateries/8792-ebcp
2. https://data.cityofnewyork.us/Health/Recognized-Shop-Healthy-Stores/ud4g-9x9z

### Peers
- Dan
- Rahul

## Work done on the project/Closing thoughts
made comparison between number of Delis vs. Food Carts
- checked to see if there are different terms within the same category
   - .a.k.a deli, grocery, food cart, cart etc.

downloaded necessary files
- data to be sorted out or visualized so that the project isn't in complete shambles

Drew 2 graphs
- compared number of delis to food carts
    - alongside grocery vs carts

Maps!
- Made 3 total
    - Combined, food carts only, and delis only

a lesson in data
- too little leaves you feeling sad trying to make connections using minor leads like a conspiracy theorist.
