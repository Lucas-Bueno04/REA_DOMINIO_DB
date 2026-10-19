# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrtabela_mensagem_inconsistencia_importacao_remessa (Mensagens de inconsistências de arquivos de retorno de boleto bancário) - módulo financeiro_tabela."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrtabela_mensagem_inconsistencia_importacao_remessa"
MODULO = "financeiro_tabela"
ENTIDADES = ['hrtabela_mensagem_inconsistencia_importacao_remessa']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
