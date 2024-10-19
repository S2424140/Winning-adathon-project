import pandas as pd

class CSVReader:
    def __init__(self, filepath: str = 'Assets/Data/'):
        self.filepath = filepath
        self.read_data()

    def read_data(self):
        self.ibm = pd.read_csv(self.filepath+"daily_adjusted_IBM.csv")["close"]
        self.msft = pd.read_csv(self.filepath+"daily_adjusted_MSFT.csv")["close"]

    def get_stock(self, stock: str) -> pd.Series | None:
        if stock == "IBM":
            return self.ibm
        elif stock == "MSFT":
            return self.msft
        else:
            return None