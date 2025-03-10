from datetime import datetime
from .movidesk_api import MovideskAPI
from .excel_handler import ExcelHandler
from .sharepoint_handler import SharePointHandler
from .logger import setup_logger

logger = setup_logger()


def main():
    # Configurações
    movidesk_token = "SEU_TOKEN_AQUI"
    sharepoint_site_url = "https://seusite.sharepoint.com"
    sharepoint_username = "seu_usuario"
    sharepoint_password = "sua_senha"
    sharepoint_file_url = "/sites/seusite/Documentos/0-Modelo_Relatorios.xlsx"
    local_file_path = "0-Modelo_Relatorios.xlsx"

    # Conectar ao SharePoint e baixar o arquivo
    sharepoint = SharePointHandler(
        sharepoint_site_url, sharepoint_username, sharepoint_password)
    ctx = sharepoint.connect()
    if ctx:
        sharepoint.download_file(ctx, sharepoint_file_url, local_file_path)

    # Carregar dados do Movidesk
    movidesk = MovideskAPI(movidesk_token)
    tickets = movidesk.get_tickets()

    # Processar dados e criar nova aba no Excel
    excel = ExcelHandler(local_file_path)
    wb = excel.load_excel()
    if wb:
        current_month = datetime.now().strftime("%B_%Y")
        data = []  # Aqui você deve processar os tickets e apontamentos para criar a lista de dados
        excel.create_new_sheet(wb, current_month, data)

        # Enviar arquivo atualizado de volta ao SharePoint
        sharepoint.upload_file(ctx, local_file_path, sharepoint_file_url)


if __name__ == "__main__":
    main()
