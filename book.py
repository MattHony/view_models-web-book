# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/7/27 21:34
# @Author : '红文'
# @File : book.py
# @Software: PyCharm


class BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book

    @classmethod
    def __cut_books_data(cls, data):
        books = []
        for book in data['books']:
            r = {
                'title': data['title'],
                'publisher': data['publisher'],
                'pages': data['pages'],
                'author': '、'.join(data['author']),
                'price': data['price'],
                'summary': data['summary'],
                'image': data['image']
            }
            books.append(r)
        return books
