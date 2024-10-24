import boto3
import os

# Configuración
BUCKET_NAME = 'testing-bucket-plazoleta'
BUCKET_TARGET_DIR = '/'

LAMBDA_FILES = [
    r'crearUsuarioLambda-1.0-SNAPSHOT.jar'
]
