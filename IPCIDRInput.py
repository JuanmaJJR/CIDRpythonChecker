__author__ = "jjusue"

import netaddr
import sys

print("\nIntroduce 0 para salir del programa\n")
while True:
    try:
        print("Introduce la IP con su CIDR en formato 'X.X.X.X/CIDR': \n")
        ip = raw_input()
        if ip !="0":
            ip = ip.split("/")[0]
            contador = 0
            contador2 = 0
            tempList = ""

            #IP a binario y obtencion de los host libres
            binaryip = '.'.join([bin(int(x)+256)[3:] for x in ip.split('.')])
            temporal = binaryip.split("1")
            cambio = temporal[len(temporal)-1]
            cambio= cambio.replace("0","1")
            difLen = len(binaryip)-len(cambio)
            listIp = list(binaryip)
            listCambio = list(cambio)

            #cambiamos los 0 de los host libres por 1 en binario
            for x in listIp:
                if(contador==difLen or contador > difLen):
                    listIp[contador]=listIp[contador].replace(listIp[contador],listCambio[contador2])
                    contador2 += 1
                contador += 1

            #creamos la IP con los host ocupados
            for y in listIp:
                tempList = tempList + y
            tempList = tempList.split(".")

            #cambiamos la IP nueva de binario a decimal, y obetenemos el CIDR del rango.
            lastIp = str(int(tempList[0],2))+"."+str(int(tempList[1],2))+"."+str(int(tempList[2],2))+"."+str(int(tempList[3],2))
            cidrs = netaddr.iprange_to_cidrs(ip, lastIp)
            #[IPNetwork('10.0.5.0/24')]
            cidrs = str(cidrs[0])
            print cidrs
    except ValueError:
        print 'Formato de IP no valido\n'
    else:
        sys.exit(0)
