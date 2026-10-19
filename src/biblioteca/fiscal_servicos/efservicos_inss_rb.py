# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efservicos_inss_rb (Notas Fiscais de Serviço - INSS Receita Bruta) - módulo fiscal_servicos."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efservicos_inss_rb"
MODULO = "fiscal_servicos"
ENTIDADES = ['efservicos_inss_rb']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
