# Flask SQLAlchemy Preview

## Getting Started

Fork and clone the repository. Inside the repo run

```bash
pipenv install
pipenv shell
```

You can find your `models.py` file inside the `server` directory.

## Deliverables

Create your models inside `models.py`. Once complete, you'll need to import them inside `app.py` in order to make things work correctly.

Once your basic models are complete, run these commands in order to create and upgrade your database:

```bash
flask db init
flask db migrate
flask db upgrade
```

You may now interact with your models by entering the flask shell:

```bash
flask shell
```