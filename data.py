from pathlib import Path
import pandas as pd
import streamlit as st

def load_file(path: str) -> pd.DataFrame:
    dataset = pd.read_csv(path)
    return dataset

@st.cache_data
def load_data(folder: str) -> pd.DataFrame:
    all_datasets = [load_file(file) for file in Path(folder).iterdir()]
    df = pd.concat(all_datasets)
    return df
