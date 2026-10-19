# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrparametro_imagem (Parametro Honorarios - Imagem para relatorios personalizados) - módulo financeiro_parametro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrparametro_imagem"
MODULO = "financeiro_parametro"
ENTIDADES = ['hrparametro_imagem']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
