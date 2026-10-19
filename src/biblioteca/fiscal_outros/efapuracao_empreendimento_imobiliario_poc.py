# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efapuracao_empreendimento_imobiliario_poc (Empreendimentos imobiliários - Percentual de Obra Concluída) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efapuracao_empreendimento_imobiliario_poc"
MODULO = "fiscal_outros"
ENTIDADES = ['efapuracao_empreendimento_imobiliario_poc']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
