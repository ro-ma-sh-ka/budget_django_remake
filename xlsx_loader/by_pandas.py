import os
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

# dfs = pd.read_excel('budgetLesh.xlsx', sheet_name=None, usecols='A:E')
# # print(dfs.keys())
# # print(dfs['2020']) - list of sheets
# result = pd.concat(dfs)
#
#
# with pd.ExcelWriter('result_file.xlsx') as writer:
#     result.to_excel(writer)

dfs2 = pd.read_excel('budgetLesh.xlsx')
columns = ['year', 'month', 'day']
dfs2['date'] = dfs2[columns].astype(str).agg('-'.join, axis=1)
dfs2['date'] = pd.to_datetime(dfs2['date'])
dfs2 = dfs2.set_index('date')
dfs2 = dfs2.drop(columns=columns, axis=1)

engine = create_engine('postgresql://postgres:1111@localhost:5432/budget_django')

# read id's from section from currency
sections_id = pd.read_sql_table('budget_section', con=engine)
currencies_id = pd.read_sql_table('budget_currency', con=engine)

print(currencies_id)
# engine = create_engine('postgresql://postgres:1111@localhost:5432/budget_django')
#
# dfs2.to_sql('budget_budget', con=engine, if_exists='append')

# with pd.ExcelWriter('result_file.xlsx') as writer:
#     dfs2.to_excel(writer)


# result.shape[0] - number of rows
# result.shape[1] - number of columns


