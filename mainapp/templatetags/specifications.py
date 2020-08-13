from django import template
from django.utils.safestring import mark_safe

from mainapp.models import Smartphone


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
    'notebook': {
        'Diagonal': 'diagonal',
        'Display type': 'display_type',
        'Processor frequency': 'processor_freq',
        'RAM': 'ram',
        'Video card': 'video',
        'Time without charge': 'time_without_charge',
    },
    'smartphone': {
        'Diagonal': 'diagonal',
        'Display type': 'display_type',
        'Resolution': 'resolution',
        'Accumulator volume': 'accum_volume',
        'RAM': 'ram',
        'SD': 'sd',
        'SD volume max': 'sd_volume_max',
        'Main camera (mp)': 'main_cam_mp',
        'Front camera (mp)': 'front_cam_mp',
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
    if isinstance(product, Smartphone):
        if not product.sd:
            PRODUCT_SPEC['smartphone'].pop('SD volume max')
        else:
            PRODUCT_SPEC['smartphone']['SD volume max'] = 'sd_volume_max'
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)
