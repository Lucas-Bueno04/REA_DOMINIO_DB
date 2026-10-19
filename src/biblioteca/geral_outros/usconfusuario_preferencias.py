# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela usconfusuario_preferencias (Tabela para armazenar as preferências do usuário) - módulo geral_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "usconfusuario_preferencias"
MODULO = "geral_outros"
ENTIDADES = ['usconfusuario_preferencias']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
