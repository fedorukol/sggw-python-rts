# Browser RTS Game 

## Opis

Ten projekt to API dla prostej gry przeglądarkowej, zbudowany przy użyciu Flask, Flask-RESTx, Flask-SQLAlchemy i Flask-JWT-Extended w ramach przedmiotu fakultatywnego "Python w praktyce - web & deep learning"

## Technologie

*   [Flask](https://flask.palletsprojects.com/): Mikroframework webowy dla Pythona.
*   [Flask-RESTx](https://flask-restx.readthedocs.io/): Rozszerzenie Flask ułatwiające budowanie API REST.
*   [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/): Rozszerzenie Flask dodające wsparcie dla SQLAlchemy.
*   [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/): Rozszerzenie Flask dodające obsługę JWT (JSON Web Tokens) do autentykacji.
*   [Alembic](https://alembic.sqlalchemy.org/en/latest/): Narzędzie do migracji bazy danych.

## Instalacja

1.  Sklonuj repozytorium:

    ```bash
    git clone <adres_repozytorium>
    cd <nazwa_projektu>
    ```

2.  Stwórz i aktywuj środowisko wirtualne:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  Zainstaluj zależności:

    ```bash
    pip install -r requirements.txt
    ```

## Uruchomienie

1.  Zainicjuj bazę danych:

    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

2.  Uruchom aplikację:

    ```bash
    cd backend
    flask run
    ```

API będzie dostępne pod adresem `http://127.0.0.1:5000/`.

## Endpointy API

### Autentykacja

*   `POST /auth/register`: Rejestracja nowego użytkownika.
    *   Wymagane pola: `username`, `password`.
*   `POST /auth/login`: Logowanie użytkownika.
    *   Wymagane pola: `username`, `password`.
    *   Zwraca token JWT w przypadku pomyślnego uwierzytelnienia.

## Modele Danych

*   [`Player`](backend/models/__init__.py): Reprezentuje użytkownika w grze.
    *   `username`: Nazwa użytkownika (unikalna).
    *   `password`: Hasło użytkownika.
    *    `towns`: Lista miast należących do gracza (relacja).
*   [`Town`](backend/models/__init__.py): Reprezentuje miasto w grze.
    *   `name`: Nazwa miasta.
    *   `player_id`: ID gracza, do którego należy miasto (klucz obcy).
    *   `population`: Populacja miasta.

## Migracje Bazy Danych

Projekt używa Alembic do zarządzania migracjami bazy danych. Pliki migracji znajdują się w katalogu [`backend/migrations`](backend/migrations).

*   [`a49fbf59f500_.py`](backend/migrations/versions/a49fbf59f500_.py): Tworzy tabelę `players`.
*   [`b977fb50d8f3_create_town_table.py`](backend/migrations/versions/b977fb50d8f3_create_town_table.py): Tworzy tabelę `towns` i dodaje relację z tabelą `players`.

## Bezpieczeństwo

API wymaga uwierzytelnienia za pomocą tokenów JWT. Aby uzyskać dostęp do chronionych zasobów, należy dodać nagłówek `Authorization` z wartością `Bearer <JWT>`, gdzie `<JWT>` to uzyskany token JWT.

## Licencja

[MIT](LICENSE)