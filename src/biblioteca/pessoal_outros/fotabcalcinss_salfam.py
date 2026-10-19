# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fotabcalcinss_salfam (Tabela de INSS - Salário Família - Faixas) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fotabcalcinss_salfam"
MODULO = "pessoal_outros"
ENTIDADES = ['fotabcalcinss_salfam']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
