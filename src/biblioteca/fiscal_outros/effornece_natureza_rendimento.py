# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela effornece_natureza_rendimento (Fornecedores - Cadastro - Natureza de Rendimento) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "effornece_natureza_rendimento"
MODULO = "fiscal_outros"
ENTIDADES = ['effornece_natureza_rendimento']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
