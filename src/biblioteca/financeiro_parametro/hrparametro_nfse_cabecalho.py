# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrparametro_nfse_cabecalho (Parametro Honorarios - Imagem e textos para NFSe) - módulo financeiro_parametro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrparametro_nfse_cabecalho"
MODULO = "financeiro_parametro"
ENTIDADES = ['hrparametro_nfse_cabecalho']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
