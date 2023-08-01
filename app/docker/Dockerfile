ARG PYTHON_IMAGE=python:3.10-slim-buster
ARG BASE_IMAGE=${PYTHON_IMAGE}

# define an alias for the specfic python version used in this file.
FROM ${BASE_IMAGE} as python

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PYSETUP_PATH="/opt/pysetup" \
    POETRY_HOME="/opt/pysetup/poetry" \
    POETRY_CACHE_DIR="/opt/pysetup/poetry_cache" \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    VENV_PATH="/opt/pysetup/.venv" \
    POETRY_VERSION="1.4.1"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"
# Extend PYTHONPATH with project
ENV PYTHONPATH="${PYTHONPATH}:/app"

WORKDIR $PYSETUP_PATH
# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # psycopg2 dependencies
  libpq-dev \
  curl \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/* \
  # Install poetry
  && curl -sSL https://install.python-poetry.org | python -

# Install base requirements
COPY poetry.lock pyproject.toml ./

# Project initialization:
RUN poetry install --with dev

WORKDIR /app
COPY . /app

COPY ./docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./docker/start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 8000
ENTRYPOINT /entrypoint.sh $0 $@
CMD ["/start.sh"]

