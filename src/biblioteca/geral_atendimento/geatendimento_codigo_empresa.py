# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela geatendimento_codigo_empresa (Relação de empresas no Contábil e Domínio Atendimento) - módulo geral_atendimento."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "geatendimento_codigo_empresa"
MODULO = "geral_atendimento"
ENTIDADES = ['geatendimento_codigo_empresa']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
