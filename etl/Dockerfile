FROM python:3-onbuild
LABEL maintainer="Jeremy Davis <jeremyadamdavis@gmail.com>"

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.5.0/wait /wait
RUN chmod +x /wait

## Launch the wait tool and then your application
CMD /wait && python ./app.py

# CMD ["python", "./app.py"]