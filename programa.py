n = int(input("ingrese el número de la cara: "))

if n==1 :

    msj = "La cara contraria es: 6"

else :
    if n==2 :

        msj = "La cara contraria es: 5"

    else :
        if n==3 :

            msj = "La cara contraria es: 4"

        else :
            if n==4 :

                msj = "La cara contraria es: 3"

            else :
                if n==5 :

                    msj = "La cara contraria es: 2"

                else:
                    if n==6 :

                        msj = "La cara contraria es: 1"

                    else :

                        msj = "no joda, ese número nisiquiera es del dado"

print (msj)