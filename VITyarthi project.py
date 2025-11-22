import pandas as pd

# Load the Excel file
df1 = pd.read_excel('Price.xlsx')
df2 = pd.read_excel('Rating.xlsx')
# Set the index
df1.set_index('Dish', inplace=True)
df2.set_index('Dish', inplace=True)

Compare=int(input("Enter the no. to comparison price and ratings: 1.Price 2.Ratings "))
if Compare==1:
    # Compare prices across messes
    for dish in df1.index:
        prices = df1.loc[dish]
        min_price = prices.min()
        cheapest_mess = prices.idxmin()
        print(f"{dish}: Cheapest at {cheapest_mess} (₹{min_price})")
elif Compare==2:
    # Compare ratings across messes
    for dish in df2.index:
        ratings = df2.loc[dish]
        max_rating = ratings.max()
        best_mess = ratings.idxmax()
        print(f"{dish}: Best rated at {best_mess} ({max_rating} stars)")