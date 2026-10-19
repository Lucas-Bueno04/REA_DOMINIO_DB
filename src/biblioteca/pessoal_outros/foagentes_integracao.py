# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foagentes_integracao (Cadastro de agentes de integração.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foagentes_integracao"
MODULO = "pessoal_outros"
ENTIDADES = ['foagentes_integracao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
