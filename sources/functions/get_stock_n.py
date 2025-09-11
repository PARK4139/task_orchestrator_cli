

def get_stock_n(ticker):
    
    df = MySqlUtil.execute(f"""select * from finance_stock_ticker where ticker="{ticker}" """)
    return df
