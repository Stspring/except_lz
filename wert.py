# Необходимо написать класс, который будет обрабатывать полученный датасет: проверять его наличие в дириктории, пытаться открыть,
# свериться с ожидаемой структурой и выдать сообщение, если все успешно выполнилось. В противном случа - обработать с помощью
# исключений все возникшие ошибки, сопроводить каждую из них понятным сообщением об ошибке.


#--------------------------------------------------------------------------------------------------------------------------------



import os 
import pandas as pd  

class DatasetHandler:
    def __init__(self, file_path, expected_columns):
       
        self.file_path = file_path  
        self.expected_columns = expected_columns  

    def process_dataset(self):
        
        try:
           
            if not os.path.exists(self.file_path):
                raise FileNotFoundError(f"Возникла следующая ошибка: файл '{self.file_path}' отсутствует")

            self.data = pd.read_csv(self.file_path)        
            print("Датасет успешно загружен.")

            df = pd.read_csv(self.file_path)
            actual_columns = list(df.columns)

            for col in self.expected_columns:
                if col not in actual_columns:
                    raise ValueError(f"Отсутствует ожидаемая колонка: '{col}'")
            print("Чтение датафрейма завершено успешно.")

        except FileNotFoundError as fnf_error:
            print(f"Ошибка: {fnf_error}")
        except pd.errors.EmptyDataError:
            print("Ошибка: Файл пустой.")
        except ValueError as ve:
            print(f"Ошибка: {ve}")
        # except Exception as e:
        #     print(f"Произошла непредвиденная ошибка: {e}")

