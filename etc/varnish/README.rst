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
