# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efparametro_vigencia_aproveita_credito (Parametros - Cadastro - Escrita Fiscal - Aproveitamento Crédito) - módulo fiscal_parametro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efparametro_vigencia_aproveita_credito"
MODULO = "fiscal_parametro"
ENTIDADES = ['efparametro_vigencia_aproveita_credito']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
