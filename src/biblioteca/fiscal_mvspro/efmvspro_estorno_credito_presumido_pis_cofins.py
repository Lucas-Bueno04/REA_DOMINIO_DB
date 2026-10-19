# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efmvspro_estorno_credito_presumido_pis_cofins (Notas Fiscais de Saída - Produtos - Estorno Crédito Presumido PIS/COFINS) - módulo fiscal_mvspro."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efmvspro_estorno_credito_presumido_pis_cofins"
MODULO = "fiscal_mvspro"
ENTIDADES = ['efmvspro_estorno_credito_presumido_pis_cofins']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
