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
print('')
for y in zhejiang_neighbours:
    print(y,'has',zhejiang_neighbours[y],'million people')

UK_countries = [57.11, 3.13, 1.91, 5.45]
CN_provinces = [65.77, 41.88, 45.28, 61.27, 5.15]

import matplotlib.pyplot as plt
