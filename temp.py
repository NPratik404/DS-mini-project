import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
 

# Load the dataset
data = pd.read_csv(r"E:\csv files\calories.csv")
print(data.head())
print(data.tail())

# Histogram of 'Age'
plt.hist(data['Age'], bins=10, color='skyblue', edgecolor='black')
plt.title("Histogram of Age")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Sample data for scatter plot
Calories = data['Calories'].sample(n=50) #to get random 50 values
Duration = data['Duration'].sample(n=50) #to get random 50 values
plt.scatter(Calories, Duration, edgecolors='g')
plt.xlabel('Calories')
plt.ylabel('Duration')
plt.title("Scatter Plot of Calories vs Duration")
plt.show()

# Box plot of 'Calories' grouped by 'Age'
data.boxplot(by='Age', column=['Calories'], grid=False, fontsize=8)
plt.title("Box Plot of Calories by Age")
plt.suptitle("")  # Remove the automatic 'Boxplot grouped by Age' title
plt.xlabel("Age")
plt.ylabel("Calories")
plt.show()

# Pearson Correlation between 'Age' and 'Calories'
list1 = data["Age"]
list2 = data["Calories"]
corr, _ = pearsonr(list1, list2)
print(f"Pearson correlation between Age and Calories: {corr}")

# Assuming 'Calories' and 'Duration' have an ordering (like timestamps)
plt.plot(data['Duration'], 
         data['Calories'], 
         color='purple', marker='o')
plt.xlabel('Duration')
plt.ylabel('Calories')
plt.show()






