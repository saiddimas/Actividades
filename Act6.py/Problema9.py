dic = {"feliz": "contento", "triste": "infeliz", "enojado": "furioso", "asustado": "aterrorizado"}
palabra = input("Escribe una palabra para saber su sinónimo: ")
if palabra in dic:
    print(f"El sinónimo de {palabra} es {dic[palabra]}")