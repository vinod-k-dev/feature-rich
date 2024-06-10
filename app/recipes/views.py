from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from app import db
from app.recipes import bp
from app.recipes.forms import RecipeForm
from app.models import Recipe

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    recipes = Recipe.query.paginate(page=page, per_page=10)
    next_url = url_for('recipes.index', page=recipes.next_num) if recipes.has_next else None
    prev_url = url_for('recipes.index', page=recipes.prev_num) if recipes.has_prev else None
    return render_template('index.html', title='Home', recipes=recipes.items, next_url=next_url, prev_url=prev_url)

@bp.route('/recipe/new', methods=['GET', 'POST'])
@login_required
def create_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(title=form.title.data, description=form.description.data, ingredients=form.ingredients.data, instructions=form.instructions.data, author=current_user)
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for('recipes.index'))
    return render_template('create_recipe.html', form=form)

@bp.route('/recipe/<int:recipe_id>')
@login_required
def recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template('recipe.html', title=recipe.title, recipe=recipe)

@bp.route('/recipe/<int:recipe_id>/update', methods=['GET', 'POST'])
@login_required
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.author != current_user:
        return redirect(url_for('index'))
    form = RecipeForm()
    if form.validate_on_submit():
        recipe.title = form.title.data
        recipe.description = form.description.data
        recipe.ingredients = form.ingredients.data
        recipe.instructions = form.instructions.data
        db.session.commit()
        return redirect(url_for('recipes.index', recipe_id=recipe.id))
    elif request.method == 'GET':
        form.title.data = recipe.title
        form.description.data = recipe.description
        form.ingredients.data = recipe.ingredients
        form.instructions.data = recipe.instructions
    return render_template('create_recipe.html', form=form, legend='Update Recipe')

@bp.route('/recipe/<int:recipe_id>/delete', methods=['POST'])
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.author != current_user:
        return redirect(url_for('index'))
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for('index'))
