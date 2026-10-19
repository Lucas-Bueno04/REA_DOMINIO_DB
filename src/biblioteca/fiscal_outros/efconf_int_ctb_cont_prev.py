# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela efconf_int_ctb_cont_prev (Configuração Integração Contábil das Contribuições Previdenciárias) - módulo fiscal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "efconf_int_ctb_cont_prev"
MODULO = "fiscal_outros"
ENTIDADES = ['efconf_int_ctb_cont_prev']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
