# Piechart using matplotlib in Python 
# pip install matplotlib 

from matplotlib import pyplot as plt

labels = ['Python', ' Java' , 'HTML' , 'C++' , 'JavaScript'] 
data = [95, 80, 65, 80, 95] 
explode = [0.0, 0.0, 0.1, 0.0, 0.0] 
plt.pie(data, labels=labels, explode=explode) 
plt.title('Programming Language Popularity')
plt.show()
