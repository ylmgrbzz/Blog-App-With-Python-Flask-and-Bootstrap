import os

from flask import (Blueprint, abort, flash, redirect, render_template, request,
                   url_for, current_app)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm
from werkzeug.utils import secure_filename

posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        image_file = None
        if form.image.data:
            image = form.image.data
            image_file = secure_filename(image.filename)
            image.save(os.path.join(current_app.root_path, 'static', 'post_images', image_file))
        post = Post(title=form.title.data, content=form.content.data, image_file=image_file, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        if form.image.data:
            image = form.image.data
            image_file = secure_filename(image.filename)
            image.save(os.path.join(current_app.root_path, 'static/post_images', image_file))
            post.image_file = image_file
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Yor post has been update!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
    form.title.data = post.title
    form.content.data = post.content
    return render_template('create_post.html', title='Update Post', 
                           form=form, legend='Update Post')
    
    
@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Yor post has been deleted!', 'success')
    return redirect(url_for('main.home'))


@posts.route("/post/<int:post_id>/purchase", methods=['PUT'])
@login_required
def purchase_post(post_id):
    post = Post.query.get_or_404(post_id)
    return redirect(url_for('main.payment_information'))
