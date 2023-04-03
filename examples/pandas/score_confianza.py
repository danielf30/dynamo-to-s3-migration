import sys
import os

# Agregar la ruta de la librería NumPy al PATH de Python
numpy_path = os.path.join(os.getcwd(), "numpy")
print(numpy_path)
sys.path.append(numpy_path)
pandas_path = os.path.join(os.getcwd(), "pandas")
print(pandas_path)
sys.path.append(pandas_path)

import boto3
import os
import pandas as pd
from datetime import datetime

def lambda_handler(event, context):
    # Obtener las credenciales de AWS
    aws_access_key_id = os.environ.get('MY_AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.environ.get('MY_AWS_SECRET_ACCESS_KEY')

    dynamo_client = boto3.client('dynamodb', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    dynamo_response = dynamo_client.scan(TableName='sample')
    print(dynamo_response)
    df = pd.DataFrame.from_dict(dynamo_response['Items'])
    df = df.applymap(lambda x: list(x.values())[0]).astype(str)

    # Define el nombre del archivo CSV de salida
    filename = f'archivo-salida-{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv'
    s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    s3_client.put_object(Body=df.to_csv(index=False), Bucket='sample-s3-dynamo', Key=filename)
