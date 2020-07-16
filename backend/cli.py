import click

from app import app, CACHE_CONFIG
from flask_caching import Cache

cache = Cache()


@click.group()
def cli():
    pass


@cli.command()
def flush_cache():
    """Flush cache"""
    cache.init_app(app, config=CACHE_CONFIG)
    with app.app_context():
        cache.clear()
    print('Done.')


if __name__ == "__main__":
    cli()
