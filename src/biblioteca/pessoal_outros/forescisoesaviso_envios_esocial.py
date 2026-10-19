# GERADO por scripts/gerar_biblioteca.py. Para curar este arquivo à mão, troque esta linha por '# CURADO' (o gerador não o sobrescreve mais).
"""Tabela forescisoesaviso_envios_esocial (Envios dos avisos das rescisões ao eSocial) - módulo pessoal_outros."""
from biblioteca.entidades import ferramentas_da_entidade

TABELA = "forescisoesaviso_envios_esocial"
MODULO = "pessoal_outros"
ENTIDADES = ['forescisoesaviso_envios_esocial']
TOOLS = [t for n in ENTIDADES for t in ferramentas_da_entidade(n)]
