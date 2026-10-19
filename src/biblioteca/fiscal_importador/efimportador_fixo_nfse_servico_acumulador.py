# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimportador_fixo_nfse_servico_acumulador (Configuração do leiaute NFS-e XML do Importador Fixo - Serviço - Acumulador) - módulo fiscal_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimportador_fixo_nfse_servico_acumulador"
MODULO = "fiscal_importador"
ENTIDADES = ['efimportador_fixo_nfse_servico_acumulador']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
