FROM continuumio/miniconda3

RUN mkdir /flask
WORKDIR /flask
RUN conda init && conda install -y flask sqlalchemy flask-sqlalchemy
RUN wget -O ~/vsls-reqs https://aka.ms/vsls-linux-prereq-script && chmod +x ~/vsls-reqs && ~/vsls-reqs

CMD ["python","app.py"]