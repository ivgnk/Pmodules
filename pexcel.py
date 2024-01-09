'''
Different functions for MS Excel
'''
import pandas as pd

def split_large_excel_file(xls_fn:str,part_size:int,dest_dir:str,res_fn_prfix:str, is_view:bool=False):
    '''
    for excel_file with 1 sheet !!!!
    https://stackoverflow.com/questions/41321082/pandas-split-large-excel-file
    https://stackoverflow.com/questions/41321082/pandas-split-large-excel-file/68982536#68982536
    dest_dir - without slash at end
    '''
    l = pd.read_excel(xls_fn)
    # https://stackoverflow.com/questions/15943769/how-do-i-get-the-row-count-of-a-pandas-dataframe

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
    res_fn_prfix = 'part_'
    split_large_excel_file(xls_fn, part_size, dest_dir, res_fn_prfix, is_view=True)

if __name__ == "__main__":
    thetest_split_large_excel_file()
