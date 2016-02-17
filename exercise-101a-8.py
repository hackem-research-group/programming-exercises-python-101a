def numeros(A, B, C):
    if(A==B or A==C or B==C):
        print "Hay valores iguales"
    else:
        if A > B and A>C:
            primero =A
            if B>C:
                segundo=B
                tercero=C
            else:
                segundo=C
                tercero=B
        if B > A and B >C:
            primero=B
            if A>C:
                segundo=A
                tercero=C
            else:
                segundo=C
                tercero=A
        if C > A and C >B:
            primero=C
            if A>B:
                segundo=A
                tercero=B
            else:
                segundo=B
                tercero=A
        print "El mayor es ", primero
        print "El menos mayor es ",segundo
        print "El menos menisimos mayor es ",tercero

numeros(9,7,6)
