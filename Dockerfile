FROM python

WORKDIR /app
RUN apt update -y
RUN apt upgrade -y
RUN apt install curl -y
RUN apt install net-tools -y
RUN pip install -r requirements.txt

COPY . .





CMD [ "python3","-B", "-m" , "cursos_online" ]
ENTRYPOINT [ "echo", "cursos_online com streamlit" ]