import requests
from .logger import setup_logger

logger = setup_logger()


class MovideskAPI:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://api.movidesk.com/public/v1"

    def get_tickets(self):
        url = f"{self.base_url}/tickets"
        headers = {"Authorization": f"Bearer {self.token}"}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro ao buscar tickets: {e}")
            return None

    def get_time_entries(self, ticket_id):
        url = f"{self.base_url}/tickets/{ticket_id}/timeEntries"
        headers = {"Authorization": f"Bearer {self.token}"}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(
                f"Erro ao buscar apontamentos do ticket {ticket_id}: {e}")
            return None
