
FROM postgres:14.4

# Environment variables
ENV PGUSER=docker
ENV PGPASSWORD=docker
ENV PGDATABASE=django_study_db
ENV PGPORT=5432
ENV TZ='America/Sao_Paulo'

# Language configuration
RUN echo "America/Sao_Paulo" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata