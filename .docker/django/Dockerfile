FROM python:3.8-slim as base

RUN adduser --disabled-password --disabled-login sc_user
USER sc_user

WORKDIR /home/sc_user/app

ENV PATH="/home/sc_user/.local/bin:${PATH}"

COPY --chown=sc_user:sc_user requirements.txt requirements.txt

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --user -r requirements.txt

COPY --chown=sc_user:sc_user . /home/sc_user/app/
