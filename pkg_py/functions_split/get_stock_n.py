

def get_stock_n(ticker):
    # from project_database.test_project_database import MySqlUtil
    df = MySqlUtil.execute(f"""select * from finance_stock_ticker where ticker="{ticker}" """)
    return df
