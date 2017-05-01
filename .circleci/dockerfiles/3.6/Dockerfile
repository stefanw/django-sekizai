FROM python:3.6

ADD ./setup.py /code/setup.py
ADD ./MANIFEST.in /code/MANIFEST.in
ADD ./tests/ /code/tests/
ADD ./sekizai/ /code/sekizai/

ARG DJANGO

RUN pip install django-classy-tags pep8 backport-collections $DJANGO /code/

CMD cd /code/tests && python runtests.py
