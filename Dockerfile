FROM assistant_env
WORKDIR /usr/src/app
COPY /api .
COPY alembic.ini .
COPY alembic ./alembic
EXPOSE 8080
CMD [ "gunicorn", "--bind", "0.0.0.0:8080", "wsgi:app" ]