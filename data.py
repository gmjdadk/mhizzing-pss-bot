import pandas as pd
from pathlib import Path

engines = {
    1 : 0.08,
    2 : 0.10,
    3 : 0.12,
    4 : 0.14,
    5 : 0.16,
    6 : 0.18,
    7 : 0.19,
    8 : 0.20,
    9 : 0.21,
    10 : 0.23
}

wpn_data_file = Path.cwd() / 'data' / 'wpn_data.csv'

with open(wpn_data_file) as file:
    wpn_data = pd.read_csv(file, index_col=0)

if __name__ == "__main__":
    print(Path.cwd() / 'data' / 'wpn_data.csv')