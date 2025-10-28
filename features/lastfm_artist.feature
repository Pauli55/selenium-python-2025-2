Feature: Buscar un artista en last.fm y validar la fecha de su ultimo lanzamiento
    Scenario: Validar la fecha del ultimo lanzamiento de Katseye
        Given el usuario está en el home page de last.fm
        When el usuario busca el artista "Katseye"
        And presiona el link del primer resultado
        Then la fecha del ultimo release debe ser "5 September 2025"
