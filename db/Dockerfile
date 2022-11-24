FROM postgres:14.4

# Environment variables
ENV PGUSER=djuser
ENV PGPASSWORD=djuser
ENV PGDATABASE=django_tutorial_db
ENV PGPORT=5432
ENV TZ='America/Sao_Paulo'

# Language configuration
RUN echo "America/Sao_Paulo" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata
