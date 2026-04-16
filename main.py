import json

data = {
  "Paolino Paperino": {
      "giorno": 9,
      "mese": "giugno",
      "anno": 1934,
      "età": 89,
      "sesso": "M",
      "mail": "paolino.paperin0@disney.org"}
  }

with open('mio_dizionario.json', 'r') as f:
    dati_paperino = json.load(f)

print(dati_paperino)
