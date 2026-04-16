# week 9 code along 3
import matplotlib.pyplot as plt
import pandas as pd

mypandas = pd.read_csv("week9/consumables.csv")
mypandas.info()
# print(mypandas.head())

group = mypandas.groupby("year")
df1 = group.mean(numeric_only=True)
print(df1)

df1["Cocoa and cocoa preparations"] = df1["Cocoa and cocoa preparations  "]
print(df1)

df1 = df1.drop(["Cocoa and cocoa preparations  "], axis=1)
print(df1)

tea_series = df1["Tea, mate and spices"]
cocoa_series = df1["Cocoa and cocoa preparations"]
coffee_series = df1["Coffee, roasted or unroasted, decaf"]

plt.plot(tea_series, marker="^", label=tea_series.name)
plt.plot(cocoa_series, marker="o", label=cocoa_series.name)
plt.plot(coffee_series, marker="<", label=coffee_series.name)

ax = plt.gca()
plt.title("Coffee, Tea, and Cocoa\nMonthly Averages by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Exported pounds (millions)")
plt.legend()
plt.show()
