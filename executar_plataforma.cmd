@echo off
rem Plataforma de progresso do mapeamento (web local). Abre em http://127.0.0.1:8800
rem Uso: executar_plataforma.cmd [--port 8800]
set "PYTHONPATH=%~dp0src"
start "" "http://127.0.0.1:8800"
"%~dp0.venv\Scripts\python.exe" -m plataforma.servidor %*
