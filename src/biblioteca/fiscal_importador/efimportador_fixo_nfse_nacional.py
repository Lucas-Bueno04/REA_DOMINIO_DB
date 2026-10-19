# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimportador_fixo_nfse_nacional (Configuração de Importação de NFS-e Arquivo XML - Padrão Nacional) - módulo fiscal_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimportador_fixo_nfse_nacional"
MODULO = "fiscal_importador"
ENTIDADES = ['efimportador_fixo_nfse_nacional']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
