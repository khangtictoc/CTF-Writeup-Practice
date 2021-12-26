FROM ubuntu:20.04

RUN /usr/sbin/useradd -u 1000 user

RUN apt-get update && apt-get install -y socat

WORKDIR /home/user/

USER user

COPY PhaPhaKhongCoDon.txt .

COPY shellcode .

EXPOSE 13337

CMD socat \
      TCP-LISTEN:13337,reuseaddr,fork \
      EXEC:"/home/user/shellcode"