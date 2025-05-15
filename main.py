from wert import DatasetHandler

def main():
    dataset_path = "var1.csv"
    expected_columns = ["column1", "column2", "column3"]
      
    handler = DatasetHandler(dataset_path, expected_columns)
    handler.process_dataset()

if __name__ == "__main__":
    main()