import argparse

# costruisce ed inizializza un oggetto ArgumentParser e lo assegna alla variabilie parser
parser =  argparse.ArgumentParser()

parser.add_argument('-n','--nome_esteso', help='Descrizione del parametro')
parser.add_argument('-b','--boolean_value', action='store_true', help="imposta il valore 'True' se trova il parametro")
parser.add_argument('-d','--con_default',  default='riferimento', help="Parametro che ha già un valore di default se non viene fornito l'argomento")

args = parser.parse_args() # fa il parsing degli argomenti da linea di comando

print(args.nome_esteso)
print(args.boolean_value)
print(args.con_default)