#importing packages
import pandas as pd



dataset0 = pd.read_csv('data/daily_sales_data_0.csv')
dataset1 = pd.read_csv('data/daily_sales_data_1.csv')
dataset2 = pd.read_csv('data/daily_sales_data_2.csv')

merged_dataset = pd.concat([dataset0,dataset1,dataset2],axis=0)
merged_dataset.to_csv('data/merged_dataset.csv',index=False)

product_data = merged_dataset[merged_dataset['product'] == 'pink morsel']
product_data.to_csv('data/product_data.csv', index=False)

final_data = pd.read_csv('data/product_data.csv')

final_data['price'] = final_data['price'].str.replace('$', '').astype(float)
final_data['sales'] = final_data['quantity'] * final_data['price']


final_data = final_data.drop(['product','price','quantity'], axis=1)

final_data.to_csv('data/pink_morsel_final.csv' , index=False)

