uno  = [1,1,1,1,1,1,1,1]
two  = [1,1,1,1,1,1,1,1]
tree = [1,1,1,1,1,1,1,1]
four = [1,1,1,1,1,1,1,1]
import math

def eliff(n,element):
    for i in range(1,n+1):
            i = i*-1
            element[i]=0
    return element  
def proceso(n,uno,two,tree,four):
    if n<=8:
        four = eliff(n,four)
        return four   
        
            
    elif 8<n<=16:
        n = n - 8
        if n<=8:
            tree = eliff(n,tree)
            for i in range(0,8):
                four[i]=0
            return tree,four
            
        
        
    elif 16<n<=24:
        n = n - 16
        if n<=8:
            two = eliff(n,two) 
            for i in range(0,8):
                four[i]=0
                tree[i]=0
            return two,tree,four  
        
    elif 24<n<=32:
        n = n - 24
        if n<=8:
            uno = eliff(n,uno) 
            for i in range(0,8):
                four[i]=0
                tree[i]=0
                two[i]=0 
            return uno,two,tree,four



while True:
    desicion = input("""QUE DESEA?
1 - Saber la mascara de subred de un numero determinado de hosts
2 - Saber la cantidad de hosts que puede albergar una Mascara determinada?
:""")
    if desicion == "1":
        host = int(input("Diga cuantos host quiere y le dire su mascara mas optima: "))
        resultado = host+2
        base = 2
        n = math.log(resultado, base)
        n = math.ceil(n)
        proceso(n,uno,two,tree,four)
        lista_de_beats = [uno,two,tree,four]
        lista = []
        for i in lista_de_beats:
            bits = i
            numero_decimal = int("".join(str(bit) for bit in bits),2)
            lista.append(numero_decimal)
        ip = (".".join(str(num)for num in lista))
        print(f"\n\n\nLa mascara de red para asignar a una red que contenga {host} hosts es: {ip}...\n\n\n\n")
      
    elif desicion == "2":
        mascara_user = input("Introduzca la Mascara de la cual desea saber la cantidad de hosts que puede albergar... : ")
        mascara_user = mascara_user.split(".")
        one = int(mascara_user[0])
        two = int(mascara_user[1])
        tree= int(mascara_user[2])
        four= int(mascara_user[3])
        print(f"{one}")
        #lista_decimal = [one,two,tree,four]
        def conversor(decimal):
            elemento = bin(decimal)[2:]
            cadena = str(elemento).zfill(8)
            return cadena
        one_bin = conversor(one)
        two_bin = conversor(two)
        tree_bin= conversor(tree)
        four_bin= conversor(four)
        print(f"{one_bin}.{two_bin}.{tree_bin}.{four_bin}")
        cadena_str_binario = str(one_bin)+str(two_bin)+str(tree_bin)+str(four_bin)
        num = cadena_str_binario.count("0")
        hosts_final = (2**num)-2
        print(f"Tu Mascara de red es capaz de albergar hasta {hosts_final} hosts")