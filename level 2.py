import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from folium.plugins import HeatMap
from geopandas.datasets import get_path
from geodatasets import get_path
import folium

data=pd.read_csv("C:\\Users\\ACER\\PycharmProjects\\internship project\\venv\\Lib\\dataset\\Data.csv")
print(data.head(5))
print(data.shape)
print(data.tail(9))

print(data.isnull())
print(data.iloc[0,9])

#level2 task1

common_rating=data['Aggregate rating'].value_counts()
print(common_rating)
print("Most Common rating for restaurant:")
print(common_rating.idxmax())

avg=round(data['Votes'].mean(),3)
print("average no votes:",avg)

#lavel 2 task2
common_combination=data.groupby('Cuisines')['Aggregate rating'].mean().sort_values(ascending=False)
print("most common cuisine combinaation:",common_combination.head(10))
maximun_rating=common_combination.iloc[0]
print("maximum rating for common cuisine is:",maximun_rating)
max_rated_resto=data.loc[data['Aggregate rating']==maximun_rating]
print("maximum rated resto:")
print(max_rated_resto['Restaurant Name'])


#level2 task3

print(data[["Longitude","Latitude"]])

gdf=gpd.GeoDataFrame(data,geometry=gpd.points_from_xy(data.Longitude,data.Latitude))
print(gdf.head())


# Create a folium map centered at a general location
m = folium.Map(location=[14.565443, 41.022793], zoom_start=10)

# Loop through the DataFrame and add CircleMarkers
for lat, lon in zip(data['Latitude'], data['Longitude']):
    folium.CircleMarker(
        location=[lat, lon],  # Latitude and longitude as individual values
        radius=3,
        color="blue",
        fill=True,
        fill_color="blue"
    ).add_to(m)

# Save or display the map
m.save("map.html")
world_map=folium.Map(location=[data['Latitude'].mean(),data['Longitude'].mean()],zoom_start=10,height='100%',width='100%')
heat_marker=[[row['Latitude'],row['Longitude']]for i ,row in data.iterrows()]
HeatMap(heat_marker,radius=10).add_to(world_map)
world_map.save('heatmap.html')

#level2 task4

#create restaurant chains
restaurant_chain=data.groupby('Restaurant Name').size().reset_index(name="OutletCount")
new=restaurant_chain[restaurant_chain["OutletCount"]>1]
restaurant_chain=new.sort_values(by="OutletCount",ascending=True)
print(restaurant_chain)
plt.bar(restaurant_chain["Restaurant Name"][:5],restaurant_chain["OutletCount"][:5])
plt.title("Restaurant chains outlets")
plt.xlabel("Restaurant name")
plt.ylabel("Outlets")
plt.show()

#Avg rating
avg_rating=data.groupby("Restaurant Name")["Aggregate rating"].mean().reset_index(name="average rating").sort_values(by="average rating",ascending=False)
print(avg_rating)
votes=data.groupby("Restaurant Name")["Votes"].mean().reset_index(name="votes").sort_values(by="votes",ascending=False)
print(votes)
plt.bar(avg_rating["Restaurant Name"][:5],avg_rating["average rating"][:5])
plt.xlabel("restaurant names")
plt.ylabel("average rating")
plt.title("Average Rating for Chains")
plt.show()
plt.bar(votes["Restaurant Name"][:5],votes["votes"][:5])
plt.xlabel("restaurant name")
plt.ylabel("votes")
plt.title("Average votes for Chains")
plt.show()
