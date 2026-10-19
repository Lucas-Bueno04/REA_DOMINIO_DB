# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fofilhos_alteracao (Registros de alteração de dependentes.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fofilhos_alteracao"
MODULO = "pessoal_outros"
ENTIDADES = ['fofilhos_alteracao']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
