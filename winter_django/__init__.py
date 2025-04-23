76f040b8a26a77cfb0bbbf30ab19427278c9c6bffrom winter.web import arguments_resolver
from .http_request_argument_resolver import HttpRequestArgumentResolver
from .output_template import output_template
from .view import create_django_urls_from_routes


def setup():
    arguments_resolver.add_argument_resolver(HttpRequestArgumentResolver())
