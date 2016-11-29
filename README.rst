***********
SMDU Portal
***********

.. contents:: Conteúdos
   :depth: 2

Introduction
============

TBD

Instalação
==========

Dependencias
------------

Na sequência se descreve como instalar as dependências do SO Debian/Ubuntu.
Estas dependências devem ser instaladas antes de rodar o buildout pela primeira vez.

O suporte LDAP/Active Directory depende do ``python-ldap``:

.. code-block:: console

    sudo apt install python-dev libldap2-dev libsasl2-dev libssl-dev

Configuração do servidor web
============================

Dentro do repositório do pacote policy se inclui uma configuração para o servidor web nginx que pode ser usada em produção.
A configuração está composta por dos arquivos (``nginx.conf`` e ``default``) e foi testada com a versão 1.10.2 do nginx.

O arquivo ``nginx.conf`` deve substituir o arquivo com esse mesmo nome localizado na pasta ``/etc/nginx``;
um link simbólico pode ser criado para simplificar o processo de manutenção da configuração.

A configuração nesse arquivo está dividida em várias diretivas:

* configuração do processo
* events: define o número máximo de conexões
* http: define parâmetros do servidor web como configuração dos logs, configuração do módulo GZip, e configuração do módulo de caching

O arquivo ``default`` deve substituir o arquivo com esse mesmo nome na pasta ``/etc/nginx/sites-enabled``;
um link simbólico pode ser criado para simplificar o processo de manutenção da configuração.

A configuração nesse arquivo está dividida em várias diretivas:

* configuração do balanceador de carga (caso precisar)
* server: define a configuração do servidor web

O funcionamento é o seguinte:

Ao iniciar o nginx é configurado com um máximo de 4096 conexões e um keep alive de 30 segundos ativo.
Os logs de acesso e erros serão armazenados na pasta ``/var/log/nginx/``.

O GZip será ativado com um nível 5 de compressão e uma lista de tipos MIME que devem ser processados.
Qualquer arquivo cujo tamanho seja menor de 256 bytes não será comprimido.

Um cache para conteúdo estático é configurado utilizando a URI do request e qualquer argumento incluso;
qualquer resposta ao requests com pelo menos 2 solicitações vai ser armazenada nele.
Status code 301, 302 e 404 são também cacheados para diminuir o número de request no backend.

Todos os request vão ser avaliados: se o método utilizado não é GET, POST ou HEAD, o request vai ser ignorado com um status code 405 (Method Not Allowed).

O nginx vai funcionar como servidor proxy: todos os requests são rescritos e reenviados ao Plone na porta 8080.
Qualquer request incluindo um cookie cujo nome inicia com ``__ac`` não vai ser cacheado.
Esse tipo de cookies estão associadas a usuários autenticados.

Qualquer request de arquivos estáticos vai incluir um header ``Expires`` na resposta com uma data de 7 dias no futuro.

No final se inclui uma configuração que aumenta a segurança do site bloqueando qualquer acesso à ZMI.
Também se inclui um bloqueio de requests associados a portais WordPress com status code 410 (Gone).

Configuração do acelerador web Varnish
======================================

Também dentro do repositório do pacote policy (na pasta ``/etc/varnish``) se inclui uma  configuração para o acelerador web Varnish que pode ser usada em produção.
A configuração inclui unicamente o arquivo VCL necessário e foi testada na versão 4.0.3 do Varnish.

O arquivo ``default.vcl`` deve substituir o arquivo com esse mesmo nome localizado na pasta ``/etc/varnish``;
um link simbólico pode ser criado para simplificar o processo de manutenção da configuração.

A configuração nesse arquivo está dividida em as seguintes partes:

* importações iniciais
* configuração do health check
* definição dos backends
* configuração das rotinas padrão
* definição de subrotinas auxiliares

A inicialização do Varnish precisa da configuração adicional localizada no arquivo ``/etc/default/varnish``;
ai se define o tamanho do cache utilizando o parâmetro ``-s malloc``,

É importante sinalar que nesta configuração o Varnish deve ser usado em conjunto com o nginx,
pois é este último quem faz o processo de rescrita das URL que precisamos para trabalhar com proxies.

Também devemos lembrar que o Varnish sempre adiciona a configuração padrão a nossa configuração em qualquer rotina que não finalize com uma diretiva return explícita.

O funcionamento é o seguinte:

Ao iniciar o Varnish configuramos dos backends (um para cada instância de Plone) e utilizamos um health check que faz uma consulta na raiz do Zope utilizando o método HEAD a cada 10 segundos.
Se após 3 segundos o Varnish não obteve resposta,
o check se considera como falido;
para evitar falsos positivos,
o backend se considera como fora de serviço (sick) se são registradas 5 falhas nos últimos 8 checks.

A rotina ``vcl_init`` adiciona diretivas que configuram o balanceador de carga (director);
o método selecionado é o hash,
pois ele permite utilizar de forma mais racional o cache de objetos de cada uma das instâncias do Plone no backend,
evitando armazenar objetos repetidos neles.

A rotina ``vcl_recv`` adiciona diretivas para indicar qual backend deve ser utilizado para servir o request caso este não se encontre no cache;
o método hash do director utiliza as URL dos requests como chave.
Adicionalmente executamos a sub-rotina ``clean_up_cookies`` que se encarrega de eliminar do request qualquer cookie não relacionada com o mecanismo de autenticação do Zope.
A utilização de esta sub-rotina é muito importante para aumentar o hit rate do cache,
pois devemos lembrar que Varnish não vai cachear nenhum request com cookies.

A rotina ``vcl_hit garante`` o time-to-live (ttl) dos objetos no cache e adiciona diretivas para aumentar a resiliência do portal,
definindo que objetos expirados possam ser entregues caso de falhas nos backend.

Finalmente, a rotina ``vcl_backend_response`` define o tempo de graça dos objetos expirados mencionados acima.
