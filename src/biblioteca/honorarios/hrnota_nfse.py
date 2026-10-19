# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela hrnota_nfse (Notas fiscais de serviço eletrônicas emitidas pelo escritório) - módulo honorarios."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "hrnota_nfse"
MODULO = "honorarios"
ENTIDADES = ['nfse']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
