# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foguiainss_dados_serv (Dados da guias de inss por servico) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foguiainss_dados_serv"
MODULO = "pessoal_outros"
ENTIDADES = ['foguiainss_dados_serv']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
