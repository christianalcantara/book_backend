[![Updates](https://pyup.io/repos/github/christianalcantara/book_backend/shield.svg)](https://pyup.io/repos/github/christianalcantara/book_backend/)
[![Python 3](https://pyup.io/repos/github/christianalcantara/book_backend/python-3-shield.svg)](https://pyup.io/repos/github/christianalcantara/book_backend/)
[![GitHub issues](https://img.shields.io/github/issues/christianalcantara/book_backend)](https://github.com/christianalcantara/book_backend/issues)
[![GitHub forks](https://img.shields.io/github/forks/christianalcantara/book_backend)](https://github.com/christianalcantara/book_backend/network)
[![GitHub stars](https://img.shields.io/github/stars/christianalcantara/book_backend)](https://github.com/christianalcantara/book_backend/stargazers)
[![GitHub license](https://img.shields.io/github/license/christianalcantara/book_backend)](https://github.com/christianalcantara/book_backend/blob/main/LICENSE)
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/christianalcantara/book_backend">
    <img src="docs/images/django-logo.png" alt="Logo" height="80">
  </a>
</p>
<h3 align="center">Django Backend</h3>

  <p align="center">
    Usage example of Django Rest Framework.
    <br />
    👽&nbsp;&nbsp;<a href="https://book-backend-rest.herokuapp.com/">View Demo</a>&nbsp;&nbsp;
    🐛&nbsp;&nbsp;<a href="https://github.com/christianalcantara/book_backend/issues">Report Bug</a>&nbsp;&nbsp;
    ✳&nbsp;&nbsp;<a href="https://github.com/christianalcantara/book_backend/issues">Request Feature</a>
  </p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#deploy-heroku">Deploy Heroku</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#authorization-token">Authorization Token</a></li>
        <li><a href="#get-customers">Get Customers</a></li>
        <li><a href="#get-books">Get Books</a></li>
      </ul>
    </li>
    <li>
       <a href="#roadmap">Roadmap</a>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://book-backend-rest.herokuapp.com/)

- Modern Python development with Python 3.8+
- Bleeding edge Django 3.0+
- PostgreSQL 11.6+
- Complete [Django Rest Framework](http://www.django-rest-framework.org/) integration
- Always current dependencies and security updates enforced by [pyup.io](https://pyup.io/).
- A slim but robust foundation -- just enough to maximize your productivity, nothing more.

<!-- GETTING STARTED -->

## Getting Started

This is an example of how you may give instructions on setting up your project locally. To get a local copy up and
running follow these simple example steps.

### Deploy Heroku

Use Heroku button to deploy

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Installation

<p align="center">

[![asciicast](https://asciinema.org/a/Q1GGnI1ZfcT5WJxCCvBBoiobN.svg)](https://asciinema.org/a/Q1GGnI1ZfcT5WJxCCvBBoiobN)
</p>

1. Clone the repo
   ```bash
   $ git clone https://github.com/christianalcantara/book_backend.git

   # jump do path
   $ cd book_backend
   ```
2. Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).
    ```bash
    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    ```
3. Create dotenv file and define enviroment variables.
   ```bash
   $ touch .env
   $ echo "#Django
     DEBUG=True
     SECRET_KEY=YOUSECRETKEY
     DOMAIN=http://localhost:8000
     ALLOWED_HOSTS=*
     # PostgreSQL database url -> postgres://{user}:{password}@{hostname}:{port}/{database-name}
     DATABASE_URL=postgres://user:password@localhost:5432/database_name
     # Sentry
     SENTRY_DSN=https://youdnsexample.ingest.sentry.io/keyexample" > .env
   ```

4. Migrate the database and run
   ```shell
   $ python manage.py migrate

   # Optional: populate database
   $ python manage.py loaddata apps/users/fixtures/users.json apps/book/fixtures/books.json  apps/rent/fixtures/rents.json

   # run
   $ python manage.py runserver
   ```

4. Run tests
   ```shell
   $ python manage.py test
   ```

<!-- USAGE -->

## Usage

Clique [here](https://book-backend-rest.herokuapp.com/) to view complete API endpoints.

### Authorization Token

- curl

 ```bash
 curl -X POST "https://book-backend-rest.herokuapp.com/api-token-auth/" -H "accept: application/json" -H "Content-Type: application/json" -H "X-CSRFToken: uoQy2P3gGWwG3jPtI9puLIazKmvGBnmd9KYUK6bopcUuAdyxYaY5YRJOs4s5d22N" -d "{ \"username\": \"admin@gmail.com\", \"password\": \"adminpassword\"}"
 ```

- Response

```json
{
  "token": "71b3e6c42f5305a2ee4a1a2b46631662ab12a83b"
}
```

### Get Customers

 ```bash
 curl --location --request GET 'https://book-backend-rest.herokuapp.com/api/customers/' --header 'Authorization: Token 71b3e6c42f5305a2ee4a1a2b46631662ab12a83b'
 ```

<details>
<summary>Response</summary>

```json
[
  {
    "url": "https://book-backend-rest.herokuapp.com/api/customers/2",
    "email": "john.doe@gmail.com",
    "avatar": "012scw_ons_crd_02.jpg",
    "full_name": "John Doe",
    "short_name": "Doe J.",
    "rents_customer": []
  },
  {
    "url": "https://book-backend-rest.herokuapp.com/api/customers/1",
    "email": "admin@gmail.com",
    "avatar": "22267408.jpeg",
    "full_name": "Admin User",
    "short_name": "User A.",
    "rents_customer": [
      {
        "url": "https://book-backend-rest.herokuapp.com/api/rent/8",
        "fees": {
          "days": 1,
          "amount": 12.0,
          "late_fee": 0.0,
          "interest": 0.0
        },
        "rental_date": "21/02/2021 17:40:40",
        "return_date": null,
        "price": "12.00",
        "late_fee_value": null,
        "interest_value": null,
        "amount": null,
        "customer": "https://book-backend-rest.herokuapp.com/api/customers/1",
        "user": "https://book-backend-rest.herokuapp.com/api/customers/1",
        "book": "https://book-backend-rest.herokuapp.com/api/books/4"
      },
      {
        "url": "https://book-backend-rest.herokuapp.com/api/rent/1",
        "fees": {
          "days": 1,
          "amount": 12.0,
          "late_fee": 0.0,
          "interest": 0.0
        },
        "rental_date": "21/02/2021 05:04:29",
        "return_date": "21.02.2021 05:39:55",
        "price": "12.00",
        "late_fee_value": null,
        "interest_value": null,
        "amount": null,
        "customer": "https://book-backend-rest.herokuapp.com/api/customers/1",
        "user": "https://book-backend-rest.herokuapp.com/api/customers/1",
        "book": "https://book-backend-rest.herokuapp.com/api/books/4"
      },
      {
        "url": "https://book-backend-rest.herokuapp.com/api/rent/5",
        "fees": {
          "days": 2,
          "amount": 12.0,
          "late_fee": 0.0,
          "interest": 0.0
        },
        "rental_date": "20/02/2021 07:02:21",
        "return_date": null,
        "price": "12.00",
        "late_fee_value": null,
        "interest_value": null,
        "amount": "22.00",
        "customer": "https://book-backend-rest.herokuapp.com/api/customers/1",
        "user": "https://book-backend-rest.herokuapp.com/api/customers/2",
        "book": "https://book-backend-rest.herokuapp.com/api/books/3"
      },
      {
        "url": "https://book-backend-rest.herokuapp.com/api/rent/4",
        "fees": {
          "days": 3,
          "amount": 12.432,
          "late_fee": 0.36,
          "interest": 0.07200000000000001
        },
        "rental_date": "19/02/2021 07:02:21",
        "return_date": "22.02.2021 04:33:04",
        "price": "12.00",
        "late_fee_value": "0.00",
        "interest_value": "0.00",
        "amount": "12.00",
        "customer": "https://book-backend-rest.herokuapp.com/api/customers/1",
        "user": "https://book-backend-rest.herokuapp.com/api/customers/1",
        "book": "https://book-backend-rest.herokuapp.com/api/books/3"
      },
      {
        "url": "https://book-backend-rest.herokuapp.com/api/rent/3",
        "fees": {
          "days": 4,
          "amount": 12.792,
          "late_fee": 0.6,
          "interest": 0.192
        },
        "rental_date": "18/02/2021 07:02:21",
        "return_date": null,
        "price": "12.00",
        "late_fee_value": null,
        "interest_value": null,
        "amount": "22.00",
        "customer": "https://book-backend-rest.herokuapp.com/api/customers/1",
        "user": "https://book-backend-rest.herokuapp.com/api/customers/2",
        "book": "https://book-backend-rest.herokuapp.com/api/books/3"
      },
      {
        "url": "https://book-backend-rest.herokuapp.com/api/rent/6",
        "fees": {
          "days": 4,
          "amount": 12.792,
          "late_fee": 0.6,
          "interest": 0.192
        },
        "rental_date": "18/02/2021 07:02:21",
        "return_date": null,
        "price": "12.00",
        "late_fee_value": null,
        "interest_value": null,
        "amount": "22.00",
        "customer": "https://book-backend-rest.herokuapp.com/api/customers/1",
        "user": "https://book-backend-rest.herokuapp.com/api/customers/2",
        "book": "https://book-backend-rest.herokuapp.com/api/books/3"
      },
      {
        "url": "https://book-backend-rest.herokuapp.com/api/rent/7",
        "fees": {
          "days": 5,
          "amount": 12.84,
          "late_fee": 0.6,
          "interest": 0.24000000000000002
        },
        "rental_date": "17/02/2021 07:02:21",
        "return_date": null,
        "price": "12.00",
        "late_fee_value": null,
        "interest_value": null,
        "amount": "22.00",
        "customer": "https://book-backend-rest.herokuapp.com/api/customers/1",
        "user": "https://book-backend-rest.herokuapp.com/api/customers/2",
        "book": "https://book-backend-rest.herokuapp.com/api/books/3"
      },
      {
        "url": "https://book-backend-rest.herokuapp.com/api/rent/2",
        "fees": {
          "days": 7,
          "amount": 12.936,
          "late_fee": 0.6,
          "interest": 0.336
        },
        "rental_date": "15/02/2021 05:39:40",
        "return_date": null,
        "price": "12.00",
        "late_fee_value": null,
        "interest_value": null,
        "amount": null,
        "customer": "https://book-backend-rest.herokuapp.com/api/customers/1",
        "user": "https://book-backend-rest.herokuapp.com/api/customers/1",
        "book": "https://book-backend-rest.herokuapp.com/api/books/3"
      }
    ]
  }
]
```

</details>

### Get Books

 ```bash
 curl --location --request GET 'https://book-backend-rest.herokuapp.com/api/books'
 ```

<details>
<summary>Response</summary>

```json
[
    {
        "id": 4,
        "title": "Test Book",
        "description": "lorem ipsum",
        "authors": [
            {
                "id": 1,
                "name": "Vijaya Khisty Bodach",
                "books": [
                    "Test Book",
                    "Flowers"
                ],
                "created": "19/02/2021 21:17:47"
            }
        ],
        "available": false,
        "price": "48.00",
        "created": "21/02/2021 03:29:57",
        "modified": "21/02/2021 05:44:13"
    },
    {
        "id": 3,
        "title": "Flexible Query Answering Systems",
        "description": "This volume constitutes the Proceedings of the 8th International Conference on Flexible Query Answering Systems, FQAS 2009, held in Roskilde, Denmark, October 26–28, 2009. FQAS 2009 was preceded by the 1994, 1996 and 1998 editions held in Roskilde, Denmark, the FQAS 2000 held in Warsaw, Poland, the 2002 held in Copenhagen, Denmark, and the 2004 and 2006 editions held in Lyon, France, and in Milan, Italy, respectively. FQAS is the premier conference concerned with the very important issue of providing users of information systems with ?exible querying capabilities, and withaneasyandintuitiveaccesstoinformation.Themainobjectiveistoachieve more expressive, informative, cooperative, and productive systems which faci- tate retrieval from information repositories such as databases, libraries, hete- geneous archives and the World-Wide Web. In targeting this objective, the c- ference draws on several research areas, such as information retrieval, database management, information ?ltering, knowledge representation, soft computing, management of multimedia information, and human–computer interaction. The conference provides a unique opportunity for researchers, developers and pr- titioners to explore new ideas and approaches in a multidisciplinary forum. The overalltopic of the FQAS conferences is innovative query systems aimed at providing easy, ?exible and human-friendly access to information. Such s- tems arebecoming increasinglyimportantalsodue to the huge andalwaysgr- ing number of users as well as the growing amount of available information.",
        "authors": [
            {
                "id": 2,
                "name": "Gail Saunders-Smith",
                "books": [
                    "Flexible Query Answering Systems"
                ],
                "created": "19/02/2021 21:17:55"
            }
        ],
        "available": false,
        "price": "65.00",
        "created": "19/02/2021 21:26:35",
        "modified": "19/02/2021 21:26:35"
    },
    {
        "id": 2,
        "title": "The Contemporary Thesaurus of Search Terms and Synonyms",
        "description": "Whether your search is limited to a single database or is as expansive as all of cyberspace, you won't find the intended results unless you use the words that work. Now in its second edition, Sara Knapp has updated and expanded this invaluable resource. Unlike any other thesaurus available, this popular guide offers a wealth of natural language options in a convenient, A-to-Z format. It's ideal for helping users find the appropriate word or words for computer searches in the humanities, social sciences, and business. The second edition has added more than 9,000 entries to the first edition's extensive list. Now, the Thesaurus contains almost 21,000 search entries! New or expanded areas include broader coverage of business terms and humanities-including arts literature, philosophy, religion, and music.",
        "authors": [
            {
                "id": 3,
                "name": "Paul McEvoy",
                "books": [
                    "The Contemporary Thesaurus of Search Terms and Synonyms"
                ],
                "created": "19/02/2021 21:18:05"
            }
        ],
        "available": true,
        "price": "126.00",
        "created": "19/02/2021 21:26:09",
        "modified": "19/02/2021 21:26:09"
    },
    {
        "id": 1,
        "title": "Flowers",
        "description": "Discover the beautiful science of flowers! Through full-color photos and simple, easy-to-follow text, this nonfiction book introduces emergent readers to the basics of botany, including information on how flowers grow, along with their uses. All Pebble Plus books align with national and state standards and are designed to help new readers read independently, making them the perfect choice for every child.",
        "authors": [
            {
                "id": 1,
                "name": "Vijaya Khisty Bodach",
                "books": [
                    "Test Book",
                    "Flowers"
                ],
                "created": "19/02/2021 21:17:47"
            }
        ],
        "available": true,
        "price": "125.00",
        "created": "19/02/2021 21:21:22",
        "modified": "19/02/2021 21:21:22"
    }
]
```
</details>

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/christianalcantara/book_backend/issues) for a list of proposed features (and
known issues).

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

<a href="mailto:christian.douglas.alcantara@gmail.com">Christian Douglas Alcântara </a>

Project Link: [https://github.com/christianalcantara/book_backend](https://github.com/christianalcantara/book_backend)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[stars-url]: https://github.com/christianalcantara/book_backend/stargazers

[license-url]: https://github.com/christianalcantara/book_backend/blob/master/LICENSE.txt

[product-screenshot]: docs/images/screenshot.png
