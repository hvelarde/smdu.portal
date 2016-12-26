***********
SMDU Portal
***********

.. contents:: Conteúdos
   :depth: 2

Introdução
==========

.. image:: https://img.shields.io/travis/hvelarde/smdu.portal/master.svg
    :target: http://travis-ci.org/hvelarde/smdu.portal

.. image:: https://img.shields.io/coveralls/hvelarde/smdu.portal/master.svg
    :target: https://coveralls.io/r/hvelarde/smdu.portal

TBD

Instalação
==========

A instalação da plataforma requere de uma série de pré-requisitos de software e hardware que devem ser satisfeitos.

Hardware e software
-------------------

Para portais pequenos (milhares de visitantes por dia),
a sugestão é utilizar servidores com pelo menos 1 processador e 1GB de memória RAM;
o espaço em disco depende da quantidade de conteúdo armazenada no portal e,
como sugestão,
nunca deve ser menor a 3 vezes o tamanho do banco de dados e o blobstorage somados,
para evitar problemas após backups.

Para portais maiores (dezenas de milhares de visitantes por dia ou mais),
a sugestão é utilizar servidores com múltiplos processadores y memória RAM suficiente para rodar o acelerador web Varnish 5.

O sistema operacional recomendado é Ubuntu Server 16.04.1 LTS,
mas a plataforma pode rodar também em servidores que utilizem diferentes versões do CentOS.

Outros pré-requisitos
---------------------

Se recomenda sempre atualizar os pacotes do sistema operacional antes de instalar as dependências.

Instalação no Ubuntu Server 16.04.1 LTS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    sudo apt update && sudo apt upgrade
    sudo apt install -y build-essential libssl-dev libxml2-dev libxslt1-dev libbz2-dev zlib1g-dev python-setuptools python-dev python-virtualenv libjpeg62-turbo-dev libreadline-gplv2-dev python-imaging python-pip wv poppler-utils git libldap2-dev libsasl2-dev libssl-dev

Instalação no CentOS 7
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: console

    sudo yum install -y epel-release && sudo yum update -y
    sudo yum install -y gcc gcc-g++ make tar bzip2 gzip openssl-devel libxml2-devel libxml2 libxslt-devel bzip2-libs zlib-devel python-setuptools python-devel python-virtualenv libjpeg-turbo-devel readline-devel python-imaging python-pip wv poppler-utils git openldap-devel
