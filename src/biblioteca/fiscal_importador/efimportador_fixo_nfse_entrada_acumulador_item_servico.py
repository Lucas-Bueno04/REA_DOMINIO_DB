# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimportador_fixo_nfse_entrada_acumulador_item_servico (Configuração do leiaute NFS-e XML do Importador Fixo - Entrada - Acumulador - Itens de serviço) - módulo fiscal_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimportador_fixo_nfse_entrada_acumulador_item_servico"
MODULO = "fiscal_importador"
ENTIDADES = ['efimportador_fixo_nfse_entrada_acumulador_item_servico']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
