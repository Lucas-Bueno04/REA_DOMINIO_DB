# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pcatividade_modulo_menu_submenu (Módulos - Menu - Submenu) - módulo processos_atividade."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pcatividade_modulo_menu_submenu"
MODULO = "processos_atividade"
ENTIDADES = ['pcatividade_modulo_menu_submenu']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
