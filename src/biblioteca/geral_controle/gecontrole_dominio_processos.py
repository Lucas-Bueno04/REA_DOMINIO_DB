# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gecontrole_dominio_processos (Controla se o escritorio possui ou não permissão para utilizar o Domínio Processos) - módulo geral_controle."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gecontrole_dominio_processos"
MODULO = "geral_controle"
ENTIDADES = ['gecontrole_dominio_processos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
