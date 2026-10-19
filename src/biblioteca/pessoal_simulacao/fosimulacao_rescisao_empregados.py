# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fosimulacao_rescisao_empregados (Simulação de rescisão - Empregados) - módulo pessoal_simulacao."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fosimulacao_rescisao_empregados"
MODULO = "pessoal_simulacao"
ENTIDADES = ['fosimulacao_rescisao_empregados']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
