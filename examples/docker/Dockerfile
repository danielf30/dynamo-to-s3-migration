# Utiliza la imagen base de Python 3.9 de AWS SAM
FROM amazon/aws-sam-cli-build-image-python3.9

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de tu proyecto al directorio de trabajo
COPY . .

# Instala las dependencias usando pip
RUN python3.9 -m pip install --no-cache-dir -r requirements.txt

# Establece el comando para ejecutar tu función Lambda localmente
CMD sam local invoke
