# tree_menu
To include the dependency installation step in your README.md file, update the Installation section as follows:

# Tree Menu Django App

Tree Menu is a Django app that allows you to create and manage hierarchical menus through the Django admin panel. Menus are rendered using a single database query, and the active menu item is determined based on the current page's URL.

## Installation

1. Clone this repository or copy the `tree_menu` folder to your Django project directory.

2. Install the required dependencies by running the following command:

pip install -r requirements.txt

3. Add `'mptt'` and `'tree_menu'` to your `INSTALLED_APPS` in your `settings.py`:

```python
INSTALLED_APPS = [
    # ...
    'mptt',
    'tree_menu',
]
```
4.  Apply migrations to create the necessary database tables:

`python manage.py makemigrations tree_menu`
`python manage.py migrate`

## Usage
1. In the Django admin panel, create menu items under the Menu Items section. You can set the title, url, named_url, and menu fields as required. For hierarchical menus, set the parent field.
2. In your template, load the draw_menu template tag and use it to render the menu:

```html
{% load draw_menu %}
{% draw_menu 'main_menu' %}
```
Replace 'main_menu' with the name of the menu you want to render.

3. The tree-menu app is now ready to use. The menu will be displayed on the specified page, and the active menu item will be determined based on the URL of the current page.
