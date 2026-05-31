#metodo para escribir cadenas
filename = 'programming.txt'



with open(filename, 'a') as file_object:
    #contenido = file_object.read()
    file_object.write('I also love finding meaning in large datasets.\n')
    file_object.write('I love creating apps that can run in a browser.\n')



#metodo para escribir numeros
# filename = 'programming.txt'

# with open(filename, 'w') as file_object:
#     for i in range(1,34):
#         file_object.write(str(i) + ',')