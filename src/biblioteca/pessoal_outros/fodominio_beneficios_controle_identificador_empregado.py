# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fodominio_beneficios_controle_identificador_empregado (Controle de alterações dos identificadores de empregados para integração com Fintech) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fodominio_beneficios_controle_identificador_empregado"
MODULO = "pessoal_outros"
ENTIDADES = ['fodominio_beneficios_controle_identificador_empregado']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
