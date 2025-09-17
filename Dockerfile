FROM python

WORKDIR /app

COPY . .
RUN apt update -y
RUN apt ugrade -y 
RUN pip install -r requirements.txt


CMD [ "python3","-B", "-m" , "cursos_online" ]
ENTRYPOINT [ "echo", "cursos_online com streamlit" ]
