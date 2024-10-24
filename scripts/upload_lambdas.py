import boto3
import os

# Configuración
BUCKET_NAME = 'testing-bucket-plazoleta'
BUCKET_TARGET_DIR = '/'

LAMBDA_FILES = [
    r'C:\pragma\IAC\lambdas\crearUsuarioLambda-1.0-SNAPSHOT.jar',
    r'C:\pragma\IAC\lambdas\listarUsuariosJavaLambda2-1.0-SNAPSHOT.jar',
    r'C:\pragma\IAC\lambdas\eliminarUsuarios.mjs',
    r'C:\pragma\IAC\lambdas\actualizarUsuarios.mjs'
]



def upload_to_s3(file_path, bucket_name, target_dir):
    # Crear un cliente de S3
    s3_client = boto3.client('s3')
    
    # Obtener el nombre del archivo
    file_name = os.path.basename(file_path)
    s3_key = os.path.join(target_dir, file_name)
    
    # Comprobar si el archivo ya existe en S3
    try:
        s3_client.head_object(Bucket=bucket_name, Key=s3_key)
        print(f'El archivo {file_name} ya existe en {bucket_name}/{target_dir}. No se subirá.')
        return  # Salir si el archivo existe
    except Exception as e:
        # Si el archivo no existe, se lanza una excepción
        if e.response['Error']['Code'] != '404':
            print(f'Error al verificar {file_name}: {e}')
            return
    
    # Subir el archivo
    try:
        s3_client.upload_file(file_path, bucket_name, s3_key)
        print(f'Subido {file_name} a {bucket_name}/{target_dir}')
    except Exception as e:
        print(f'Error al subir {file_name}: {e}')



if __name__ == "__main__":
    for file_path in LAMBDA_FILES:
        upload_to_s3(file_path, BUCKET_NAME, BUCKET_TARGET_DIR)