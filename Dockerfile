FROM redhat/ubi8

RUN yum install -y python3 python3-pip && \
    yum clean all

RUN pip3 install flask

COPY app.py /app.py

WORKDIR /

CMD ["python3", "/app.py"]
