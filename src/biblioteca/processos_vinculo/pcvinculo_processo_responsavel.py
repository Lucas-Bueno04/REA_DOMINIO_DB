# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela pcvinculo_processo_responsavel (Vínculo entre processos e empresas - Responsáveis) - módulo processos_vinculo."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "pcvinculo_processo_responsavel"
MODULO = "processos_vinculo"
ENTIDADES = ['pcvinculo_processo_responsavel']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
