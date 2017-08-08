import pandas as pd
q = 'select exhibitionid from exhibitions;'
chunk_iter = pd.read_sql(q, conn, chunksize=100)
for chunk in chunk_iter:
    # Process each chunk.