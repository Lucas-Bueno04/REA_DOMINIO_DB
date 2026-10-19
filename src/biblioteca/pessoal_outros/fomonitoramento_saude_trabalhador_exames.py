# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela fomonitoramento_saude_trabalhador_exames (Monitoramento da Saúde do Trabalhador - Exames realizados.) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "fomonitoramento_saude_trabalhador_exames"
MODULO = "pessoal_outros"
ENTIDADES = ['fomonitoramento_saude_trabalhador_exames']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
