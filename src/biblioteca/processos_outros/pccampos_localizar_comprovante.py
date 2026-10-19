# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pccampos_localizar_comprovante (Campos utilizados para localizador comprovantes) - módulo processos_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pccampos_localizar_comprovante"
MODULO = "processos_outros"
ENTIDADES = ['pccampos_localizar_comprovante']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
