Feature: Buscar una pelicula en imdb.com/es-es/ para validar el nombre de la pelicula y el raiting de esta misma
    Scenario: Validar el nombre y el rating de Inception
        Given el usuario está en el home page de imdb.com
        When el usuario busca la pelicula "Inception"
        And presiona el link del primer resultado de la pelicula
        Then el nombre de la pelicula debe ser "Origen" y el raiting de la pelicula debe ser "8.8"