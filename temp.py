import pandas as pd #for read csv
import matplotlib.pyplot as plt # for Histograms (plt.hist() Scatter plots (plt.scatter()) Box plots (data.boxplot()) Line plots (plt.plot()) Displaying plots (plt.show())
from scipy.stats import pearsonr # is used to calculate the Pearson correlation
 

# Load the dataset
data = pd.read_csv(r"C:\Users\PC\Desktop\archive\calories.csv")
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
data.boxplot(by='Age', column=['Calories'], fontsize=8)
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

# Line Plot of Duration vs Calories Assuming 'Calories' and 'Duration' have an ordering (like timestamps)
plt.plot(data['Duration'], 
         data['Calories'], 
         color='purple', marker='o')
plt.title("Line Plot of Duration vs Calories")
plt.xlabel('Duration')
plt.ylabel('Calories')
plt.show()

# Scatter plot of actual vs predicted values
plt.scatter(list1, list2)
plt.xlabel('Actual Calories')
plt.ylabel('Predicted Calories')
plt.title('Actual vs Predicted Calories')
plt.plot([list1.min(), list1.max()], [list1.min(), list1.max()], color='red')  # Line for perfect predictions
plt.show()




