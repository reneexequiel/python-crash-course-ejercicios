
import pandas as pd

def exportar_txt(filename):
    try:
        with open(filename) as file:
            contents = file.read()
    except Exception:
        print("Ha habido un error, revisa el codigo.")
    
    else:
        filename = pd.read_csv(r'/home/rene/Documentos/Progamacion/Python/Proyectos/Software de registro de constraseñas/dist/registro.txt',delimiter='\t')
        
        print("El archivo", filename, " fue exportado exitosamente.")

filename = 'registro.csv'
exportar_txt(filename)