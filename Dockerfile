FROM python

WORKDIR /app

COPY . .

# Instala as dependências com pip
RUN pip install -r requirements.txt


CMD [ "python3","-B", "-m" , "cursos_online" ]
ENTRYPOINT [ "echo", "cursos_online com streamlit" ]