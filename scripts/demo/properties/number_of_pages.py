# coding:utf-8
"""Definition of pages number property."""
from .property_func import get_property_schema, get_property_form, set_post_data
from . import property_config as config

property_id = config.NUMBER_OF_PAGES
multiple_flag = False
name_ja = 'ページ数'
name_en = 'Number of Pages'


def add(post_data, key, **kwargs):
    """Add to a item type."""
    option = kwargs.pop('option')
    set_post_data(post_data, property_id, name_ja, key, option, form, schema, **kwargs)

    if kwargs.pop('mapping', True):
        post_data['table_row_map']['mapping'][key] = {
            'display_lang_type': '',
            'jpcoar_v1_mapping': {
                'numPages': {
                    '@value': 'subitem_number_of_pages'
                }
            },
            'jpcoar_mapping': {
                'numPages': {
                    '@value': 'subitem_number_of_pages'
                }
            },
            'junii2_mapping': '',
            'lido_mapping': '',
            'lom_mapping': '',
            'oai_dc_mapping': '',
            'spase_mapping': ''
        }
    else:
        post_data['table_row_map']['mapping'][key] = config.DEFAULT_MAPPING


def schema(title='', multi_flag=multiple_flag):
    """Get schema text of item type."""

    def _schema():
        _d = {
            'type': 'object',
            'properties': {
                'subitem_number_of_pages': {
                    'format': 'text',
                    'title': 'ページ数',
                    'type': 'string'
                }
            }
        }
        return _d

    return get_property_schema(title, _schema, multi_flag)


def form(key='', title='', title_ja=name_ja, title_en=name_en, multi_flag=multiple_flag):
    """Get form text of item type."""

    def _form(key):
        """Form text."""
        _d = {
            'items': [
                {
                    'key': '{}.subitem_number_of_pages'.format(key),
                    'title': 'ページ数',
                    'title_i18n': {
                        'ja': 'ページ数',
                        'en': 'Number of Pages'
                    },
                    'type': 'text'
                }
            ],
            'key': key.replace('[]', '')
        }
        return _d

    return get_property_form(key, title, title_ja, title_en, multi_flag, _form)
