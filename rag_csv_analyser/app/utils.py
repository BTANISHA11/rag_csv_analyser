import pandas as pd
from fastapi import HTTPException

def read_csv(file_path: str) -> str:
    try:
        df = pd.read_csv(file_path)
        return df.to_json(orient='records')
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))