import pandas as pd

def getCsvData(link: str, save_location: str, with_header: bool = False):
    df = pd.read_csv(link)
    if with_header:
        df.columns = ['age', 'sex', 'cp', 'trestbps', 'chol',
              'fbs', 'restecg', 'thalach', 'exang', 
              'oldpeak', 'slope', 'ca', 'thal', 'target']
    df.to_csv(save_location, index=False)

if __name__== "__main__":
    saveLocation: str = "./data/cleaveland.csv"
    source : str = "https://raw.githubusercontent.com/ShubhankarRawat/Heart-Disease-Prediction/master/cleveland.csv"
    getCsvData(link=source,
                save_location=input("Enter the save location : ") or saveLocation)
