***********
SMDU Portal
***********

.. contents:: Conteúdos
   :depth: 2

Introduction
============

.. image:: https://img.shields.io/travis/hvelarde/smdu.portal/master.svg
    :target: http://travis-ci.org/hvelarde/smdu.portal

.. image:: https://img.shields.io/coveralls/hvelarde/smdu.portal/master.svg
    :target: https://coveralls.io/r/hvelarde/smdu.portal

TBD

Instalação
==========

Dependencias
------------

Esta seção se descreve como instalar as dependências do projeto.
É importante sinalar que todas as dependências devem ser instaladas antes de rodar o buildout pela primeira vez.

O suporte LDAP/Active Directory depende do pacote ``python-ldap``.

No Debian/Ubuntu, é preciso instalar:

.. code-block:: console

    sudo apt install python-dev libldap2-dev libsasl2-dev libssl-dev

No CentOS/RHEL, é preciso instalar:

.. code-block:: console

    sudo yum install python-devel openldap-devel
