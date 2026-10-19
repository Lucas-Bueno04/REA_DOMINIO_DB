# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foesocial_controle_periodos (Controle de envio de reabertura e fechamento de período da empresa no eSocial.) - módulo pessoal_esocial."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foesocial_controle_periodos"
MODULO = "pessoal_esocial"
ENTIDADES = ['foesocial_controle_periodos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
