import sys
from collections import defaultdict

LOWEST = 3
HIGHEST = 11
MAX_PY = (3.6)


def pyiter(maxpy):
    yield 2, 7
    i = 3
    while True:
        yield 3, i
        i += 1
        if (3, i) > maxpy:
            break


def get_pythons(django, minpys, maxpys):
    minpy = minpys[django]
    maxpy = maxpys[django]
    for py in pyiter(maxpy):
        if minpy <= py:
            yield py


def iter_version():
    max_pythons = {}
    for dj in range(LOWEST, 6):
        max_pythons[dj] = (2, 7)
    for dj in range(6, 8):
        max_pythons[dj] = (3, 4)
    for dj in range(8, HIGHEST + 1):
        max_pythons[dj] = (3, 6)

    min_pythons = {}
    for dj in range(LOWEST, 9):
        min_pythons[dj] = (2, 7)
    for dj in range(9, HIGHEST + 1):
        min_pythons[dj] = (3, 4)

    for dj in range(LOWEST, HIGHEST + 1):
        for py in get_pythons(dj, min_pythons, max_pythons):
            yield dj, py


def build_circleci():
    with open('.circleci/config.yml', 'w') as fobj:
        fobj.write('\n'.join(config()))
    with open('docker-compose.yml', 'w') as fobj:
        fobj.write('\n'.join(compose()))
    for py, data in dockerfiles():
        with open('.circleci/dockerfiles/{py}/Dockerfile'.format(py=py), 'w') as fobj:
            fobj.write('\n'.join(data))


def dockerfile(py):
    yield 'FROM python:{py}'.format(py=py)
    yield 'ADD ./setup.py /code/setup.py'
    yield 'ADD ./MANIFEST.in /code/MANIFEST.in'
    yield 'ADD ./tests/ /code/tests/'
    yield 'ADD ./sekizai/ /code/sekizai/'
    yield 'ARG DJANGO'
    yield 'RUN pip install django-classy-tags pep8 backport-collections $DJANGO /code/'
    yield 'CMD cd /code/tests && python runtests.py'


def dockerfiles():
    for py in pyiter(MAX_PY):
        spy = '.'.join(map(str, py))
        yield spy, dockerfile(spy)
    
    
def compose():
    yield 'version: \'2\''
    yield 'services:'
    for dj, py in iter_version():
        version = 'django>=1.{min},<1.{max}'.format(min=dj, max=dj + 1)
        python = '.'.join(map(str, py))
        tag = 'p{py[0]}{py[1]}d1{dj}'.format(py=py, dj=dj)
        yield '  ' + tag + ':'
        yield '    build:'
        yield '      context: .'
        yield '      dockerfile: .circleci/dockerfiles/{py}/Dockerfile'.format(py=python)
        yield '      args:'
        yield '        - DJANGO={version}'.format(version=version)


def config():
    yield 'version: \'2\''
    yield 'jobs:'
    yield '  build:'
    yield '    docker:'
    yield '      - image: docker/compose:1.9.0'
    yield '    working_directory: /home/'
    yield '    steps:'
    yield '      - setup_remote_docker'
    yield '      - checkout'
    yield '      - run: docker-compose build'
    for dj, py in iter_version():
        tag = 'p{py[0]}{py[1]}d1{dj}'.format(py=py, dj=dj)
        yield '      - run: docker-compose run --rm {tag}'.format(tag=tag)


def build_docs_table():
    '''
=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======
    :return: 
    '''
    data = defaultdict(list)
    for dj, py in iter_version():
        data[dj].append(py)
    print('============== =========================')
    print('Django Version Supported Python Versions')
    print('============== =========================')
    for dj, pys in sorted(data.items()):
        pys = ', '.join(map(lambda x: '.'.join(map(str, x)), pys))
        sdj = '1.{dj}'.format(dj=dj)
        if len(sdj) < 4:
            sdj += ' '
        print('{dj}           {pys}'.format(pys=pys, dj=sdj))
    print('============== =========================')


def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    if sys.argv[1] == 'circleci':
        build_circleci()
    elif sys.argv[1] == 'docs':
        build_docs_table()
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
