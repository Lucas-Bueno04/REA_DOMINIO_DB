# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foempregados_chave_pix (Cadastro de empregados - Chave Pix) - módulo pessoal_empregados."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foempregados_chave_pix"
MODULO = "pessoal_empregados"
ENTIDADES = ['foempregados_chave_pix']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
