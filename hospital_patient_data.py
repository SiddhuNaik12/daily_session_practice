# Scenario 8: Hospital Patient Data
# Hospital management wants insights.
# Tasks:
# Generate patient age and recovery days.
# Group patients into age buckets.
# Calculate:
# Average recovery days per age group
# Plot:
# Scatter plot (age vs recovery days)
# Bar chart of average recovery per age group
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(42)
data={
    'patient_age':np.random.randint(1,60,20),
    'recovery_days':np.random.randint(1,10,20)
}
df=pd.DataFrame(data)
# Average recovery days per age group
group_kids=df[(df["patient_age"]>=1) &(df["patient_age"]<=18)]
group_adults=df[(df["patient_age"]>18) & (df["patient_age"]<=40)]
group_olds=df[(df['patient_age']>40)]
print(df)
print(group_kids)
print(group_adults)
print(group_olds)
#Average recovery days per age group
avg_kids_days=group_kids["recovery_days"].mean()
avg_adults_days=group_adults["recovery_days"].mean()
avg_olds_days=group_olds["recovery_days"].mean()
print(avg_kids_days)
print(avg_adults_days)
print(avg_olds_days)
#scatter plot
plt.scatter(df["patient_age"],df["recovery_days"],s=df["recovery_days"]*10)
plt.xlabel("Age")
plt.ylabel("recovery days")
plt.show()
#Bar chart
age_groups=['kids','adults','olds']
avg_recovery=[avg_kids_days,avg_adults_days,avg_olds_days]
plt.bar(age_groups,avg_recovery)
plt.xlabel("age groups")
plt.ylabel("average recovery")
plt.title("average recovery per age group")
plt.show()
