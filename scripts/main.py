import pandas as pd
import matplotlib.pyplot as plt

print("Starting Business Analytics Dashboard Project...")

# Sample data
sales_data = pd.DataFrame({
    "Month": ["Jan","Feb","Mar","Apr","May"],
    "Revenue": [1000,1200,1100,1500,1700],
    "Expenses": [500,600,550,700,800]
})

# Compute profit
sales_data["Profit"] = sales_data["Revenue"] - sales_data["Expenses"]

# Plot revenue vs expenses
plt.figure(figsize=(8,5))
plt.plot(sales_data["Month"], sales_data["Revenue"], label="Revenue")
plt.plot(sales_data["Month"], sales_data["Expenses"], label="Expenses")
plt.plot(sales_data["Month"], sales_data["Profit"], label="Profit")
plt.title("Business Analytics Dashboard")
plt.legend()
plt.savefig("revenue_vs_expenses.png")
plt.close()

# Print summary
print("Sales data:")
print(sales_data)
print("\nBusiness Analytics Dashboard Completed!")
