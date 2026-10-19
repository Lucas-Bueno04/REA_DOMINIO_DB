# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fosindicatosaviso (Sindicato - Cadastro - Aviso Previo) - módulo pessoal_nucleo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fosindicatosaviso"
MODULO = "pessoal_nucleo"
ENTIDADES = ['fosindicatosaviso']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
