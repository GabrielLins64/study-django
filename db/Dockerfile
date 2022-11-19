FROM postgres:14.4

# Environment variables
ENV PGUSER=docker
ENV PGPASSWORD=docker
ENV PGDATABASE=django_tutorial_db
ENV PGPORT=5432
ENV TZ='America/Sao_Paulo'

# Create database
COPY ./create_db.sql /docker-entrypoint-initdb.d/

# Language configuration
RUN echo "America/Sao_Paulo" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata
