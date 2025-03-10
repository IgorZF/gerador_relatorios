import pandas as pd
from openpyxl import load_workbook
from .logger import setup_logger

logger = setup_logger()


class ExcelHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_excel(self):
        try:
            return load_workbook(self.file_path)
        except Exception as e:
            logger.error(f"Erro ao carregar arquivo Excel: {e}")
            return None

    def create_new_sheet(self, wb, sheet_name, data):
        try:
            df = pd.DataFrame(data)
            with pd.ExcelWriter(self.file_path, engine='openpyxl') as writer:
                writer.book = wb
                df.to_excel(writer, sheet_name=sheet_name, index=False)
            return True
        except Exception as e:
            logger.error(f"Erro ao criar nova aba no Excel: {e}")
            return False

    def get_previous_month_data(self, wb, sheet_name):
        try:
            sheet = wb[sheet_name]
            data = sheet.values
            df = pd.DataFrame(data)
            return df
        except Exception as e:
            logger.error(f"Erro ao obter dados do mês anterior: {e}")
            return None
