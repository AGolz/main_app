from django import template
from mptt.templatetags.mptt_tags import cache_tree_children
from tree_menu.models import MenuItem

register = template.Library()

def render_menu_items(items, current_path):
    output = '<ul>'
    for item in items:
        if item.url == current_path or (item.named_url and reverse(item.named_url) == current_path):
            output += f'<li class="active">{item.title}'
        else:
            output += f'<li><a href="{item.url or reverse(item.named_url)}">{item.title}</a>'
        if item.children:
            output += render_menu_items(item.children, current_path)
        output += '</li>'
    output += '</ul>'
    return output

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    root_items = cache_tree_children(MenuItem.objects.filter(menu=menu_name, parent=None))
    return render_menu_items(root_items, request.path)