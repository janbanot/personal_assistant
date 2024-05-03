FROM assistant_env
WORKDIR /usr/src/app
COPY .env .env
COPY api ./api
COPY tests ./tests
COPY alembic.ini .
COPY alembic ./alembic
EXPOSE 8080
CMD [ "gunicorn", "--bind", "0.0.0.0:8080", "--timeout", "180", "api.wsgi:app" ]