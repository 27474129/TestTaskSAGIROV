FROM python:3.9.2

RUN mkdir /sources
COPY . /sources/
WORKDIR /sources

CMD cd /sources/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]
