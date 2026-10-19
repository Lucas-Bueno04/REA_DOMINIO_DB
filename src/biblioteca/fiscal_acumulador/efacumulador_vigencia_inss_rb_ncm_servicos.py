# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efacumulador_vigencia_inss_rb_ncm_servicos (Acumuladores - Cadastro - INSS Receita Bruta - NCM e Serviços) - módulo fiscal_acumulador."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efacumulador_vigencia_inss_rb_ncm_servicos"
MODULO = "fiscal_acumulador"
ENTIDADES = ['efacumulador_vigencia_inss_rb_ncm_servicos']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
