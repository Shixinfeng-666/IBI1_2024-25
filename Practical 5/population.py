# Define population sizes for the UK countries and Zhejiang-neighbouring provinces
uk_countries = {
    'England': 57.11,
    'Wales': 3.13,
    'Northern Ireland': 1.91,
    'Scotland': 5.45
}

zhejiang_neighbours = {
    'Zhejiang': 65.77,
    'Fujian': 41.88,
    'Jiangxi': 45.28,
    'Anhui': 61.27,
    'Jiangsu': 85.15
}
# Print the population of each country/neighboured provences
for x in uk_countries:
    print(x,'has',uk_countries[x],'million people')
    #directly show all the data of UK in natrual language
print('')
for y in zhejiang_neighbours:
    print(y,'has',zhejiang_neighbours[y],'million people')
    #directly show all the adta of Zhejiang's neighbourhood in natrual language


UK_countries = [57.11, 3.13, 1.91, 5.45]
CN_provinces = [65.77, 41.88, 45.28, 61.27, 5.15]

import matplotlib.pyplot as plt

labels_uk = list(uk_countries.keys()) # use the name of countries as the labels of pie chart 1
sizes_uk = list(uk_countries.values()) # use the value of population as the sizes in the meaning of percentage
colors_uk = ['blue','green','red','yellow']
plt.pie(sizes_uk,labels = labels_uk, colors = colors_uk,autopct='%1.1f%%') # add the properties: sizes, labels, colors, and the exact number in it
plt.title('Population Distribution in UK countries') # to explain what's this chart shown for
plt.show() # out put the figure
# similar to the part above
labels_zj = list(zhejiang_neighbours.keys())
sizes_zj = list(zhejiang_neighbours.values())
colors_zj = colors_uk.append('purple')
plt.pie(sizes_zj,labels = labels_zj,colors = colors_zj,autopct='%1.1f%%')
plt.title('Population Distribution in Zhejiang_s neghibours')
plt.show()
