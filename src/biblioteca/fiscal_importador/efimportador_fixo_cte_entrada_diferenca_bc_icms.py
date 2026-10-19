# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efimportador_fixo_cte_entrada_diferenca_bc_icms (Configuração do leiaute CT-e XML do Importador Fixo - Entrada - Diferença entre valor contábil e base de cálculo ICMS) - módulo fiscal_importador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efimportador_fixo_cte_entrada_diferenca_bc_icms"
MODULO = "fiscal_importador"
ENTIDADES = ['efimportador_fixo_cte_entrada_diferenca_bc_icms']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
