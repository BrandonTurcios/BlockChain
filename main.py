import hashlib

class UNITECoin:

    def __init__(self,hash_bloque_anterior,lista_transaccion):
        self.hash_bloque_anterior = hash_bloque_anterior
        self.lista_transaccion = lista_transaccion
        self.datos_bloque = " - ".join(lista_transaccion) + " - " + hash_bloque_anterior
        self.hash_bloque = hashlib.sha256(self.datos_bloque.encode()).hexdigest ( )

t1 = " Juan le transfiere 3 UC a Ricardo"
t2 = " Ricardo le transfiere 6 UC a Miguel"
t3 = " Miguel le transfiere 4 UC a Brandon"
t4 = " Brandon le transfiere 5 UC a Juan"

initial_block = UNITECoin( "TRANSACCION",[t1,t2])
print(initial_block.datos_bloque)
print(initial_block.hash_bloque)


second_block = UNITECoin(initial_block.hash_bloque,[t3,t4])
print(second_block.datos_bloque)
print(second_block.hash_bloque)
