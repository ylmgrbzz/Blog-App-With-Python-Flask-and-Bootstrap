from flask import Blueprint, render_template, request
from flaskblog.models import Post
from datetime import datetime

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')


# payment_information() fonksiyonu
@main.route('/payment_information')
def payment_information():
    post_id = request.args.get('post_id', type=int)
    post = Post.query.get_or_404(post_id)
    # Fiyatı hesaplamak için, post id'sini 10 ile çarpın ve tarihin rakamlarının toplamını ekleyin
    date_digits = [int(d) for d in datetime.strftime(post.date_posted, '%Y%m%d%H%M%S')]
    price = post.id * 10 + sum(date_digits)

    # payment_information.html dosyasını render_template() fonksiyonuyla geri döndürün
    return render_template('payment_information.html', post=post, price=price)


@main.route('/process_payment', methods=['POST'])
def process_payment():
    # Ödeme işlemleri burada gerçekleştirilecek
    # ...
    return "Payment processed successfully!"
