#importing packages
import pandas as pd


# reads the dataset csv files
dataset0 = pd.read_csv('data/daily_sales_data_0.csv')
dataset1 = pd.read_csv('data/daily_sales_data_1.csv')
dataset2 = pd.read_csv('data/daily_sales_data_2.csv')

# this function merges the dataset and creates a new csv file for it
merged_dataset = pd.concat([dataset0,dataset1,dataset2],axis=0)
merged_dataset.to_csv('data/merged_dataset.csv',index=False)

# this function isolates the pink morsel data and stores it in another csv file
product_data = merged_dataset[merged_dataset['product'] == 'pink morsel']
product_data.to_csv('data/product_data.csv', index=False)

final_data = pd.read_csv('data/product_data.csv')
# as the '$' sign prevents the multiplication of the data, it is removed to prevent that
final_data['price'] = final_data['price'].str.replace('$', '').astype(float)
#  sales = price * quantity
final_data['sales'] = final_data['quantity'] * final_data['price']

# these columns are dropped to just have the region, date and sales
final_data = final_data.drop(['product','price','quantity'], axis=1)

final_data.to_csv('data/pink_morsel_final.csv' , index=False)

