from typing import List

import pandas as pd
from sklearn.feature_extraction import DictVectorizer

CATEGORICAL_COLS = ["cut", "color", "clarity"]

from sklearn.preprocessing import LabelEncoder
def encode_categorical_cols(df: pd.DataFrame) -> pd.DataFrame:
    # 处理所有分类列
    categorical_cols = [col for col in df.columns if col in CATEGORICAL_COLS]
    for col in categorical_cols:
        df[col] = df[col].fillna("Unknown")  # 用 "Unknown" 填充缺失值
    return df




