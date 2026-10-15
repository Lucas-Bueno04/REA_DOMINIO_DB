import sys, re, pathlib
f = pathlib.Path(sys.argv[1])
d = f.read_bytes()
print(f.name, len(d), "bytes; cabeçalho:", d[:16])
for nome, pat in [("bethadba ascii", b"bethadba"), ("BETHADBA ascii", b"BETHADBA"),
                  ("bethadba utf16", "bethadba".encode("utf-16-le")), ("BETHADBA utf16", "BETHADBA".encode("utf-16-le")),
                  ("select ascii", b"select"), ("SELECT ascii", b"SELECT"), ("select utf16", "select".encode("utf-16-le")),
                  ("SELECT utf16", "SELECT".encode("utf-16-le")), ("retrieve", b"retrieve"), ("PBSELECT", b"PBSELECT"),
                  ("DAT*", b"DAT*"), ("HDR*", b"HDR*"), ("NOD*", b"NOD*"), ("ENT*", b"ENT*")]:
    print(f"  {nome:<16}{d.count(pat):>8}")
i = d.find(b"HDR*")
print("HDR*:", d[i:i+60] if i >= 0 else None)
# amostra de nomes de entradas (ENT*)
ents = re.findall(rb"ENT\*.{0,40}?([A-Za-z0-9_]+\.(?:srd|sru|srw|srf|srm|srs|srq|sra|srj|srx|srp))", d)
print("entradas (amostra):", [e.decode() for e in ents[:15]], "total", len(ents))
