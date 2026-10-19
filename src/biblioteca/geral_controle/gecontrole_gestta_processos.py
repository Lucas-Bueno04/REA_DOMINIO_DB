# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela gecontrole_gestta_processos (Controla Ativação do gestta processos) - módulo geral_controle."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "gecontrole_gestta_processos"
MODULO = "geral_controle"
ENTIDADES = ['gecontrole_gestta_processos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
