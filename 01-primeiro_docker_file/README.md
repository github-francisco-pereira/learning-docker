# O Primeiro Dockerfile a gente nunca esquece

- Usamos Docker por um motivo bem específico. Você consegue responder por quê?
- Não é necessário responder isso agora :)
- Link da apresentação: https://docs.google.com/presentation/d/1aUlGXF_l1fBQlJoskgjhtaDm7bVqhw-BlmlSzkY2Jhg/edit?usp=sharing
- Link dos vídeos:
    - Parte 1 - https://vimeo.com/279769552
    - Parte 2 - https://vimeo.com/279773556

# Fazendo o tutorial
- Primeiro `construa` sua imagem:
```sh
    docker build . --network=host -t meuflask:latest
```
- Agora `rode` um `container`com sua imagem:
```sh
    docker run --net=host -p 5000:5000 meuflask:latest
```
- Tente acessar http://localhost:5000/ no seu navegador :)