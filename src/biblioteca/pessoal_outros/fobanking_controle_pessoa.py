# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fobanking_controle_pessoa (Controla o que deve ou não ser enviado ao banking em relação ao cadastro de pessoas.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fobanking_controle_pessoa"
MODULO = "pessoal_outros"
ENTIDADES = ['fobanking_controle_pessoa']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
