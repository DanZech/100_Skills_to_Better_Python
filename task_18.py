import zlib

s = "Hello world! Python is great!"
t = zlib.compress(s.encode("utf-8"))
print(t)
print(zlib.decompress(t))

'''
O método "zlib.compress()" é usado para comprimir uma string em bytes
usando o algoritmo de compressão zlib. No exemplo acima, 
a string "s" é primeiro codificada em bytes usando o método "encode()" 
com o parâmetro "utf-8", e em seguida é comprimida usando o método "zlib.compress()".

O resultado da compressão é armazenado na variável "t", que contém os bytes comprimidos. 
Em seguida, o programa descomprime os bytes usando o método "zlib.decompress()" 
e exibe o resultado na saída padrão. O resultado esperado é a string original "Hello world! Python is great!".
'''