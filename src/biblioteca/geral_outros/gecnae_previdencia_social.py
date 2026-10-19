# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gecnae_previdencia_social (Tabela de CNAE da previdência social) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gecnae_previdencia_social"
MODULO = "geral_outros"
ENTIDADES = ['gecnae_previdencia_social']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
