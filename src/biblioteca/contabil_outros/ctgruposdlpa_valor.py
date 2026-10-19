# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela ctgruposdlpa_valor (Estrutura do DLPA - Valores informados) - módulo contabil_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "ctgruposdlpa_valor"
MODULO = "contabil_outros"
ENTIDADES = ['ctgruposdlpa_valor']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
