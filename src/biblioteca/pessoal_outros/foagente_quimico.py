# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foagente_quimico (Cadastro de agente químico) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foagente_quimico"
MODULO = "pessoal_outros"
ENTIDADES = ['foagente_quimico']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
