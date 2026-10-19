# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foesocial_avisos_vencimento_fechamento_periodo (Armazena os avisos de vencimentos para os períodos sem fechamentos no eSocial) - módulo pessoal_esocial."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foesocial_avisos_vencimento_fechamento_periodo"
MODULO = "pessoal_esocial"
ENTIDADES = ['foesocial_avisos_vencimento_fechamento_periodo']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
