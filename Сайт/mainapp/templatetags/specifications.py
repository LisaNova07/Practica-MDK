from django import template
from django.utils.safestring import mark_safe

from mainapp.models import Book, Magazine


register = template.Library()


TABLE_HEAD = """
                <table class="table">
                  <tbody>
             """

TABLE_TAIL = """
                  </tbody>
                </table>
             """

TABLE_CONTENT = """
                    <tr>
                      <td>{name}</td>
                      <td>{value}</td>
                    </tr>
                """

PRODUCT_SPEC = {
    'book': {
        'Автор': 'author',
        'Издательство': 'publisher',
        'Дата издания': 'creationdate',
    },
    'magazine': {
        'Издательство': 'publisher',
        'Дата издания': 'creationdate',
    }
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)

