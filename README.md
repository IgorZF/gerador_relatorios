# Projeto Gerador de Relatorios

Este projeto tem como objetivo coletar informações do Movidesk (tickets e apontamentos por cliente) utilizando um token de acesso fornecido. Os dados são organizados em uma planilha do Excel e integrados com o SharePoint para armazenamento e recuperação de arquivos.

## Estrutura do Projeto

- `/logs/`: Contém os arquivos de log.
- `/src/`: Contém os módulos do projeto.
  - `main.py`: Script principal.
  - `movidesk_api.py`: Módulo para integração com a API do Movidesk.
  - `excel_handler.py`: Módulo para manipulação do arquivo Excel.
  - `sharepoint_handler.py`: Módulo para integração com o SharePoint.
  - `logger.py`: Módulo para geração de logs.
- `requirements.txt`: Dependências do projeto.

## Como Executar

1. Clone o repositório.
2. Instale as dependências com `pip install -r requirements.txt`.
3. Configure as variáveis de ambiente e tokens necessários.
4. Execute o script principal com `python src/main.py`.

## Agendamento

O código pode ser agendado para rodar automaticamente no dia 01 de cada mês usando o cron no Linux ou o Agendador de Tarefas no Windows.
