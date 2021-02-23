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

<h3 align="center">Django Backend</h3>

  <p align="center">
    Usage example of Django Rest Framework.
    <br />
    👽&nbsp;&nbsp;<a href="https://github.com/christianalcantara/book_backend">View Demo</a>&nbsp;&nbsp;
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
        <li><a href="#prerequisites">Deploy Heroku</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

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

[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge

[contributors-url]: https://github.com/christianalcantara/book_backend/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge

[forks-url]: https://github.com/christianalcantara/book_backend/network/members

[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge

[stars-url]: https://github.com/christianalcantara/book_backend/stargazers

[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge

[issues-url]: https://github.com/christianalcantara/book_backend/issues

[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge

[license-url]: https://github.com/christianalcantara/book_backend/blob/master/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://linkedin.com/in/othneildrew

[product-screenshot]: docs/images/screenshot.png
