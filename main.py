import pandas as pd

def main():
    """main関数
    """
    df = pd.read_csv('./resources/sample.csv')

    # CSVのヘッダーを取得
    df_header = df.columns

    table_name = 'hoge'
    columns_list = ','.join(df_header)

    result = []
    
    for row in df.itertuples(index=False):
        values_list = ','.join(str(x) for x in row)
        result.append(f'INSERT INTO {table_name} ({columns_list}) VALUES ({values_list})')
    
    print(result)


if __name__ == '__main__':
    main()
