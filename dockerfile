FROM ubuntu:26.04
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		openssh-server \
		sudo \
		python3 \
		python3-pip \
		python3-venv \
		# vim.tiny is for editing files during testing
		vim.tiny \ 
	&& rm -rf /var/lib/apt/lists/*

# default sshuser
RUN useradd -rm --create-home --shell /bin/bash --groups sudo sshuser
RUN echo 'sshuser:password' | chpasswd

# 'test' user added for testing
RUN useradd -rm --create-home --shell /bin/bash --groups sudo test
RUN echo 'test:test' | chpasswd

RUN mkdir -p /run/sshd \
	&& mkdir -p /home/sshuser/.ssh \
	&& touch /home/sshuser/.ssh/config

RUN chown -R sshuser:sshuser /home/sshuser
RUN mkdir -p /opt/jumpserver/venv

RUN python3 -m venv /opt/jumpserver/venv/.venv
RUN /opt/jumpserver/venv/.venv/bin/pip install flask

RUN mkdir -p /opt/jumpserver/menu
COPY ./ssh-script.py /opt/jumpserver/menu/jumpserver.py

COPY ./resources/web/ /opt/jumpserver/web/

EXPOSE 22
EXPOSE 5000

CMD ["/usr/sbin/sshd", "-D"]

