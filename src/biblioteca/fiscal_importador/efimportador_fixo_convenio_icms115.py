# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimportador_fixo_convenio_icms115 (Configuração do leiaute Convênio ICMS 115/03) - módulo fiscal_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimportador_fixo_convenio_icms115"
MODULO = "fiscal_importador"
ENTIDADES = ['efimportador_fixo_convenio_icms115']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
