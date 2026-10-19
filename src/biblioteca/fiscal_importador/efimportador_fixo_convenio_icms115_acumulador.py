# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimportador_fixo_convenio_icms115_acumulador (Configuração do leiaute Convênio ICMS 115/03 - Acumulador) - módulo fiscal_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimportador_fixo_convenio_icms115_acumulador"
MODULO = "fiscal_importador"
ENTIDADES = ['efimportador_fixo_convenio_icms115_acumulador']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
