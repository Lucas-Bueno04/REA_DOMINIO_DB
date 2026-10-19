# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gebuscanfe_controle_acesso (Controla acesso ao Busca NFE) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gebuscanfe_controle_acesso"
MODULO = "geral_outros"
ENTIDADES = ['gebuscanfe_controle_acesso']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
