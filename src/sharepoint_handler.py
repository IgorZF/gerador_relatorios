from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File
from .logger import setup_logger

logger = setup_logger()


class SharePointHandler:
    def __init__(self, site_url, username, password):
        self.site_url = site_url
        self.username = username
        self.password = password

    def connect(self):
        try:
            ctx_auth = AuthenticationContext(self.site_url)
            if ctx_auth.acquire_token_for_user(self.username, self.password):
                return ClientContext(self.site_url, ctx_auth)
            else:
                logger.error("Falha na autenticação com o SharePoint")
                return None
        except Exception as e:
            logger.error(f"Erro ao conectar ao SharePoint: {e}")
            return None

    def download_file(self, ctx, file_url, local_path):
        try:
            response = File.open_binary(ctx, file_url)
            with open(local_path, "wb") as local_file:
                local_file.write(response.content)
            return True
        except Exception as e:
            logger.error(f"Erro ao baixar arquivo do SharePoint: {e}")
            return False

    def upload_file(self, ctx, local_path, file_url):
        try:
            with open(local_path, 'rb') as content_file:
                file_content = content_file.read()
            File.save_binary(ctx, file_url, file_content)
            return True
        except Exception as e:
            logger.error(f"Erro ao enviar arquivo para o SharePoint: {e}")
            return False
