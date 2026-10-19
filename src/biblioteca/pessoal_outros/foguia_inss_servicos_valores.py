# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela foguia_inss_servicos_valores (Valores de encargos de INSS pagos por serviço.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "foguia_inss_servicos_valores"
MODULO = "pessoal_outros"
ENTIDADES = ['foguia_inss_servicos_valores']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
