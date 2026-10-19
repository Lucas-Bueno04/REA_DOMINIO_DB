# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foconfiguracoes_etiquetas_ctps (Configuração das etiquetas de atualização da CTPS.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foconfiguracoes_etiquetas_ctps"
MODULO = "pessoal_outros"
ENTIDADES = ['foconfiguracoes_etiquetas_ctps']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
