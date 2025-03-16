def shellsort(input_list):
    gap = len(input_list)//2
    while gap > 0:
        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j= i
            # ordena la sublista para este gap
            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j-gap
            input_list[j] = temp
        # reduce el gap para el elemento que sigue
        gap = gap//2
            
list = []
n = int(input("¿Cuántos valores desea agregar a la lista?: "))
for i in range(0,n):
    list.append(int(input("Teclee el siguiente valor a ingresar: ")))
print("Lista desordenada: ", list)
shellsort(list)
print("\nLista ordenada: ",list)