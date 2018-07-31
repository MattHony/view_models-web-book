from flask import jsonify, request, current_app

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key

from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel
from . import web


# @web.route('/book/search/<q>/<page>')
@web.route('/book/search')
def search():
    """
        q :普通关键字 （keyword) isbn
        page
    """
    # 第一种方式 验证方法q,page
    # q = request.args['q']
    # page = request.args['page']
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()     # strip()除去q前后存在空格
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
            result = BookViewModel.package_single(result, q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
            result = BookViewModel.package_collection(result, q)
        return jsonify(result)
    else:
        return jsonify(form.errors)
    # return json.dumps(result), 200, {'content-type': 'application/json'}


@web.route('/test')
def test1():
    print(id(current_app))
