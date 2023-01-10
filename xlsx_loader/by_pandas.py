import os
import pandas as pd

dfs = pd.read_excel('budgetLesh.xlsx', sheet_name=None, usecols='A:E')
print(dfs.keys())
# print(dfs['2020'])
result = pd.concat(dfs)
print(result)

# workbook = pd.read_excel(excel_file, sheet_name=pattern_sheet, skiprows=[0, 2])
# combiner = pd.DataFrame()
# workbook.at[0:workbook.shape[0], 'Шаблон озон'] = file
# print(f'{counter}/{len(files)} - {file}')
# counter += 1
# # concatenate dataframes
# combiner = pd.concat([combiner, workbook], sort=False, axis=0, ignore_index=True)
# result_file = os.path.join(work_dir, '_combiner_result.xlsx')
# write_to_excel(result_file, pattern_sheet, combiner)
#
# combiner.to_excel(writer, sheet_name=pattern_sheet)
