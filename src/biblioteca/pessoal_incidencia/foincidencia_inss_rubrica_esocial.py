# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foincidencia_inss_rubrica_esocial (Tabela de códigos de incidência de INSS para o eSocial.) - módulo pessoal_incidencia."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foincidencia_inss_rubrica_esocial"
MODULO = "pessoal_incidencia"
ENTIDADES = ['foincidencia_inss_rubrica_esocial']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
