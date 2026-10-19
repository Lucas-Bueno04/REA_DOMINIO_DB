# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fofilhos_plano_saude (Cadastro de dependentes - Plano de saúde) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fofilhos_plano_saude"
MODULO = "pessoal_outros"
ENTIDADES = ['fofilhos_plano_saude']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
