# Usa una imagen base de Python
FROM python:3.12-slim

# Actualiza el gestor de paquetes y instala git
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Clona el repositorio en el directorio de trabajo
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-AdrianBrito8.git

# Establece el directorio de trabajo
WORKDIR /ajedrez-2024-AdrianBrito8

#  Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar tu aplicación
CMD ["sh", "-c", "coverage run -m unittest && coverage report -m && python -m game.cli"]
