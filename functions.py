import pandas as pd

def describe_with_na(data, percentiles=None, include=None, exclude=None,):
    '''Describe metod from Pandas library with additional NA count and percentage of NA in pd.Series or each column of pd.DataFrame.'''
    
    #execute Pandas describe method
    try:
        df_describe = data.describe(percentiles=percentiles, include=include, exclude=exclude)
    except:
        return 'Function doesn\'t work, because Pandas method describe does not work. Try to execite describe method to see potential errors.'
    
    #add NA_COUNT and NA% for Series
    if isinstance(data, pd.Series):
        df_describe.loc['na_count'] = data.isna().sum()
        df_describe.loc['na%'] = 100*df_describe['na_count'] / data.shape[0]

    #add NA_COUNT and NA% for DataFrames
    elif isinstance(data, pd.DataFrame):
        df_null_count = {}
        for col_name in df_describe.columns:
            df_null_count[col_name] = data[col_name].isna().sum()

        df_describe.loc['na_count'] = list(df_null_count.values())
        df_describe.loc['na%'] = (100*df_describe.loc['na_count', :] / data.shape[0]).to_list()

    return df_describe.reindex(df_describe.index.to_list()[0:1]+ df_describe.index.to_list()[-2:]+ df_describe.index.to_list()[1:-2])