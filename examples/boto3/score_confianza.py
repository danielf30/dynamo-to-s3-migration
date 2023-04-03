import boto3

def lambda_handler(event, context):
    # Crear un cliente S3 utilizando las credenciales predeterminadas de la sesión de AWS
    s3 = boto3.client('s3')
    
    # Listar todos los buckets en tu cuenta de AWS
    response = s3.list_buckets()
    
    # Contar la cantidad de buckets y almacenarla en una variable
    bucket_count = len(response['Buckets'])
    
    # Imprimir un mensaje con la cantidad de buckets
    print(f"Encontrados {bucket_count} buckets en tu cuenta de AWS.")
