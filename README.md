# Scrapy-MongoAtlas
O código consiste em um web crawler que busca informações sobre marcas em um site e as armazena em um arquivo JSON e em um banco de dados MongoDB.

A função "urls_brands" cria uma lista de URLs para acessar cada letra do alfabeto no site de marcas.

A função "inserirmongo" se conecta ao banco de dados MongoDB e insere os dados contidos no arquivo "marcas.json" na coleção "brands".

A função "write_results" recebe uma lista de marcas, ordena-as por nome e as escreve em um arquivo JSON chamado "marcas.json".

A classe "BrandsSpider" é um spider do Scrapy que inicia as solicitações HTTP para cada URL gerada pela função "urls_brands". O método "parse" é chamado para cada resposta HTTP e extrai o nome de cada marca, adicionando-o à lista de marcas da classe. O método "close" é chamado quando a execução do spider é finalizada e chama as funções "write_results" e "inserirmongo" para armazenar as marcas no arquivo JSON e no banco de dados MongoDB, respectivamente.

Em resumo, este código automatiza a coleta de informações sobre marcas em um site, armazenando-as em um arquivo JSON e em um banco de dados MongoDB, tornando a coleta e o gerenciamento desses dados mais eficiente.
