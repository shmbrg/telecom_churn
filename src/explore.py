import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv("./data/telecom_customer_churn.csv")
profile = ProfileReport(df, title="Telecom Customer Churn Profiling Report")
profile.to_file("tcc_profiling.html")
