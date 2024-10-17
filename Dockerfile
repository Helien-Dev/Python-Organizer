FROM python:3.12-bookworm
RUN apt-get update && apt-get install -y git neofetch curl zsh zplug
