import os
import pandas as pd
from sqlalchemy import create_engine
import psycopg2


def combine_sheets() -> pd.DataFrame:
    # combine all sheets into one and save to a new file
    df = pd.read_excel('budgetLesh_years.xlsx', sheet_name=None, usecols='A:E')
    # print(dfs.keys())
    # print(dfs['2020']) - list of sheets
    one_sheet_df = pd.concat(df)

    with pd.ExcelWriter('budgetLesh.xlsx') as writer:
        one_sheet_df.to_excel(writer)
    return one_sheet_df


def df_db_format():
    # read one_sheet excel file and create structure to send to database
    df = pd.read_excel('budgetLesh.xlsx')

    # combine year, month, days to one column date
    columns = ['year', 'month', 'day']
    df['date'] = df[columns].astype(str).agg('-'.join, axis=1)

    # convert to datetime format
    df['date'] = pd.to_datetime(df['date'])

    # set column date as an index column
    df = df.set_index('date')

    # delete column we don't need
    df = df.drop(columns=columns, axis=1)
    with pd.ExcelWriter('result_file.xlsx') as writer:
        df.to_excel(writer)


def names_to_ids():
    engine = create_engine('postgresql://postgres:1111@localhost:5432/budget_django')

    # read id's from section and currency tables
    sections = pd.read_sql_table('budget_section', con=engine)
    currencies = pd.read_sql_table('budget_currency', con=engine)

    df = pd.read_excel('result_file.xlsx')

    for currency in currencies[['currency', 'id']].iterrows():
        df.loc[(df['currency'] == currency[1][0]), 'currency'] = currency[1][1]

    for section in sections[['section', 'id']].iterrows():
        df.loc[(df['section'] == section[1][0]), 'section'] = section[1][1]

    df = df.set_index('date')

    with pd.ExcelWriter('result_file2.xlsx') as writer:
        df.to_excel(writer)


names_to_ids()


# engine = create_engine('postgresql://postgres:1111@localhost:5432/budget_django')
#
# dfs2.to_sql('budget_budget', con=engine, if_exists='append')

# with pd.ExcelWriter('result_file.xlsx') as writer:
#     dfs2.to_excel(writer)


# result.shape[0] - number of rows
# result.shape[1] - number of columns


