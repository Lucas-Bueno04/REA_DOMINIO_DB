# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pcresponsavel_empresa (Responsáveis empresas) - módulo processos_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pcresponsavel_empresa"
MODULO = "processos_outros"
ENTIDADES = ['pcresponsavel_empresa']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
