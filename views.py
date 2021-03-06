from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from personalpage.models import Post

posts = Blueprint('posts', __name__, template_folder='templates')

class Index(MethodView):

	def get(self):
		return render_template('index.html')

class Posts(MethodView):
	def get(self):
		entries = Post.objects.all()
		return render_template('notes.html', entries=entries)


posts.add_url_rule('/', view_func=Index.as_view('index'))
posts.add_url_rule('/notes', view_func=Posts.as_view('notes'))