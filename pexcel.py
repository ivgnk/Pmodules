'''
Different functions for MS Excel
'''
import pandas as pd
import sys

def split_large_excel_file(xls_fn:str,part_size:int,dest_dir:str,res_fn_prfix:str, is_view:bool=False):
    '''
    for excel_file with 1 sheet !!!!
    https://stackoverflow.com/questions/41321082/pandas-split-large-excel-file
    https://stackoverflow.com/questions/41321082/pandas-split-large-excel-file/68982536#68982536
    dest_dir - without slash at end
    '''
    l = pd.read_excel(xls_fn)
    # https://stackoverflow.com/questions/15943769/how-do-i-get-the-row-count-of-a-pandas-dataframe
    # print(type(l));  print(pd.DataFrame == type(l));     sys.exit(0)

    count_row = l.shape[0]  # Gives number of rows
    count_col = l.shape[1]  # Gives number of columns
    if is_view: print(f' total rows {count_row}')
    total_size = count_row
    print('splitting')
    for i in range(0, total_size, part_size):
        if is_view: print('part ',i)
        df = l[i:i + part_size]
        df.to_excel(dest_dir +'/'+ res_fn_prfix+str(i) + '.xlsx')

def thetest_split_large_excel_file():
    xls_fn = 'J:/Work-Lang2/Python/PyCharm/GTimeSeries/dat/127.xlsx'
    part_size = 10_000
    dest_dir = 'J:/Work-Lang2/Python/PyCharm/GTimeSeries/dat'
    res_fn_prfix = '127_part_'
    split_large_excel_file(xls_fn, part_size, dest_dir, res_fn_prfix, is_view=True)

def get_part_from_large_excel_file(xls_fn:str,beg_:int, end_:int, is_view:bool=False)->pd.DataFrame:
    '''
    on the base of def split_large_excel_file(xls_fn:str,part_size:int,dest_dir:str,res_fn_prfix:str, is_view:bool=False):
    '''
    df = pd.read_excel(xls_fn)
    count_row = df.shape[0]  # Gives number of rows
    res_df = df.iloc[beg_: end_]
    if is_view:
        print(f' total rows =\n {count_row}')
        col_name = list(df.columns)
        print('col_name=\n',col_name)
        view_df = res_df[['GRAV.', 'SD.', 'TIME', 'Дата-Время']]
        print(view_df)
    return res_df

def thetest_get_part_from_large_excel_file():
    xls_fn = 'J:/Work-Lang2/Python/PyCharm/GTimeSeries/dat/127.xlsx'
    get_part_from_large_excel_file(xls_fn, 5,10, is_view = True)
    # www.geeksforgeeks.org/python-extracting-rows-using-pandas-iloc/

if __name__ == "__main__":
    # thetest_split_large_excel_file()
    thetest_get_part_from_large_excel_file()
