@echo off
rem Lançador do servidor MCP do banco Domínio (SOMENTE LEITURA). Não depende do diretório atual nem de variáveis de ambiente:
rem as credenciais vêm de config\.env. Uso: executar_servidor.cmd [--transport streamable-http --host 127.0.0.1 --port 8765]
set "PYTHONPATH=%~dp0src"
"%~dp0.venv\Scripts\python.exe" -m server.mcp_server %*
