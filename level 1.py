import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("C:\\Users\\ACER\\PycharmProjects\\internship project\\venv\\Lib\\dataset\\Data.csv")
print(data.head(5))
print(data.shape)
print(data.tail(9))

print(data.isnull())
print(data.iloc[0,9])

#level1 task 1
top_cuisine= data['Cuisines'].str.split(',').explode('Cuisines').value_counts()

print("Top 3 most common Cuisine are:")
print(top_cuisine.head(3))

total_restaurant=len(data)
percentage=(top_cuisine/total_restaurant)*100
print("percentage of restaurants that serve each of the top three cuisines are:")
print(percentage.head(3))
print()
print()

#level1 task2
max_resto_city=data['City'].value_counts()
print("City with highest restaurants:")
print(max_resto_city.head(1))

avg_rating=data.groupby('City')["Aggregate rating"].mean().reset_index()
print("Average rating for reastaurant:")
print(avg_rating)

print("City with highest average rating:")
print(avg_rating.max())


#level 1 task 3
plt.figure(figsize=(10,15))
data.hist(column='Price range')
plt.title("Distribution of Price range")
plt.xlabel("Price range")
plt.ylabel("count")
plt.show()

count_of_Price_range=data['Price range'].value_counts()
total_count=len(data)
percentage=((count_of_Price_range/total_count)*100)
percentage_c=pd.merge(count_of_Price_range,percentage,on='Price range')

print("percentage of price range over the restaurant:")
print(percentage_c)

#level 1 task4
count_of_resto_online_delivery=data['Has Online delivery'].value_counts()
print(count_of_resto_online_delivery)
total_resto=len(data)
Yes_count=count_of_resto_online_delivery.get('Yes')
print(Yes_count)
percentage_yes=((Yes_count/total_resto)*100)
print("Percentage of resto that offers online delivery:",percentage_yes,"%")

resto_online_delivery_yes=(data[data['Has Online delivery']=='Yes']['Aggregate rating'].mean())
resto_online_delivry_no=(data[data['Has Online delivery']=='No']['Aggregate rating'].mean())
print("avg rating for resto with online delivery:",resto_online_delivery_yes)
print("avg rating for resto without online delivery:",resto_online_delivry_no)

avg_rating=[resto_online_delivery_yes,resto_online_delivry_no]
labels=['Online delivery','No online delivery']
colors="blue","Green"
plt.barh(labels,avg_rating,color=colors)
plt.title("comparision of avg rating with online delivery")
plt.xlabel('online delivery')
plt.ylabel('Avg Rating')
plt.show()
plt.figure(figsize=(10,15))
data.hist(column='Aggregate rating')
plt.title("Distribution of Avg Rating for resto")
plt.xlabel("Ratings")
plt.ylabel("count")
plt.show()
