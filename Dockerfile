FROM centos:centos7

RUN yum -y update
RUN yum -y install https://repo.ius.io/ius-release-el7.rpm
RUN yum -y install python36

WORKDIR /srv/ctf
ADD ./ /srv/ctf/

RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]

EXPOSE 8080

