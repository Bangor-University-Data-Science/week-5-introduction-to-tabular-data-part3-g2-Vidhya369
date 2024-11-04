import pandas as pd

def import_data(filename: str) -> pd.DataFrame:
     
    return pd.read_excel(filename)
data = import_data_from_excel('Customer_Behavior.xlsx')  
data.head ('Customer_Behavior.xlsx')


def filter_data(df: pd.DataFrame) -> pd.DataFrame:
   
    df_filtered = df[df['CustomerID'].notna()]

    df_filtered = df_filtered[(df_filtered['Quantity'] >= 0) & (df_filtered['UnitPrice'] >= 0)]
    
    return df_filtered

def loyalty_customers(df: pd.DataFrame, min_purchases: int) -> pd.DataFrame:
    
    purchase_counts = df.groupby('CustomerID').size().reset_index(name='PurchaseCount')
    

    loyal_customers = purchase_counts[purchase_counts['PurchaseCount'] >= min_purchases]
    
    return loyal_customers
def quarterly_revenue(df: pd.DataFrame) -> pd.DataFrame:
 
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    df['Year'] = df['InvoiceDate'].dt.year
    df['Quarter'] = df['InvoiceDate'].dt.to_period('Q')
    quarterly_revenue = df.groupby(['Year', 'Quarter'])['Revenue'].sum().reset_index()
    quarterly_revenue.columns = ['Year', 'Quarter', 'Total_Revenue']
    return quarterly_revenue

def high_demand_products(df: pd.DataFrame, top_n: int) -> pd.DataFrame:

    product_demand = df.groupby('Description')['Quantity'].sum().reset_index()
    top_products = product_demand.sort_values(by='Quantity', ascending=False).head(top_n)
    top_products.columns = ['Product_Description', 'Total_Quantity_Sold']
    
    return top_products
def purchase_patterns(df: pd.DataFrame) -> pd.DataFrame:
   
    summary = df.groupby('Description').agg(
        avg_quantity=('Quantity', 'mean'),
        avg_unit_price=('UnitPrice', 'mean')
    ).reset_index()
    
    summary.rename(columns={'Description': 'product'}, inplace=True)
    
    return summary
def answer_conceptual_questions() -> dict:

    answers = {
        "Q1": {"A"},  
        "Q2": {"B"},       
        "Q3": {"C"},  
        "Q4": {"A", "B"}, 
        "Q5": {"A"},     
    }  
    
    return answers