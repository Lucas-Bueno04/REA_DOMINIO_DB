# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fotrocas_informacoes_pessoais (Alterações das informações pessoais do empregado.) - módulo pessoal_trocas."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fotrocas_informacoes_pessoais"
MODULO = "pessoal_trocas"
ENTIDADES = ['fotrocas_informacoes_pessoais']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
