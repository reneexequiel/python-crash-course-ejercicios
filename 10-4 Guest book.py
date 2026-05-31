#Archivo: guest book.py
#Autor: Rene Marambio
#Fecha: 30-01-24
#Descripcion: #crear un ciclo while que pide al usuario su nombre. Una vez que lo haga se mostrara un saludo.
#ademas, se le recuerde que se registren en el libro de visitas, pero esto ultimo
#tiene que ir en una nueva linea.



#se crea bandera para ciclo while
bandera = True
#se crea variable que contendra el archivo de texto guest_book.txt
filename= 'guest_book.txt'

while bandera:
    with open(filename, 'a') as file_object:
        #file_object.write('Bienvenido' + '\n')
        file_object.write('Bienvenido ' + (input('Escribe tu nombre') + '!!' + '\n'))
        file_object.write('No olvide registrarse en el libro de visitas !!' + '\n')