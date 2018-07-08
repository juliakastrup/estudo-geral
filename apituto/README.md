Tutorial disponível em:

- https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-1
- https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-2

Status:

2018-07-08:

- Problema anterior resolvido deletando o arquivo 'db.sqlite3' e rodando 'makemigrations' e 'migrate' de novo. 
 
- Outros problemas encontrados, que tinham a ver com o tutorial utilizar o Django antigo, como, por exemplo, o 'django.core.urlresolvers', que foi substituído por 'django.urls' no Django 2.0

- Último problema encontrado e não resolvido:

    ```
    IntegrityError at /bucketlists/
NOT NULL constraint failed: api_bucketlist.owner_id
    ```

- Parei em: https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-2#toc-how-to-pass-those-tests

- Por ora, vou retomar outro tutorial (projeto `django-puppy-store`), que gostei mais por ser mais recente e também por ter exemplos mais elucidativos.


2018-07-04:

- Parte 1 finalizada.

- Parte 2 não finalizada.
   
   Feito até esse ponto: https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-2#toc-implementing-it
   
   Migrações geradas e rodadas.
   
   Quando tomei erro:
   
    ```
    OperationalError at /bucketlists/
    no such column: api_bucketlist.owner_id
    ```

Última tentativa em: 2018-07-08 17h18