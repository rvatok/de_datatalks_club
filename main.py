import pandas as pd
from sqlalchemy import create_engine


csv_name = 'yellow_tripdata_2019-01.csv'
df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

df = next(df_iter)

# df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
# df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)



engine = create_engine('postgresql://root:root@localhost:5433/ny_taxi')
print (df.head(n=0) )