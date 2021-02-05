FROM debian:buster-slim
LABEL maintainer="idealista <labs@idealista.com>"

RUN apt-get update && \
    apt-get install -y python sudo bash ca-certificates iproute2 systemd systemd-sysv python-pip && \
    apt-get clean

EXPOSE 80

CMD ["/lib/systemd/systemd"]
