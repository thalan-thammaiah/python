import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


d = pd.read_csv('liquor.csv')
print(d)

print(d.info())

# Bar plot
plt.figure(figsize=(6, 10))
plt.title('Most Popular Categories')
plt.xlabel('Count')
plt.xticks(rotation=45) 
sns.countplot(y='category_name', data=d)
plt.ylabel('Category')
plt.xticks(fontsize=8)
plt.show()