from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember, forget
from ..models.services.user import UserService
from ..models.user import User
from ..models.services.blog_record import BlogRecordService
from ..models.meta import DBSession


@view_config(route_name='home', renderer='blojik_pyramid:templates/index.jinja2')
def index_page(request):
    page = int(request.params.get('page', 1))
    paginator = BlogRecordService.get_paginator(request, page)
    return {'paginator': paginator}


@view_config(route_name='auth', match_param='action=in', renderer='string', request_method='POST')
@view_config(route_name='auth', match_param='action=out', renderer='string')
def sign_in_out(request):
    username = request.POST.get('username')
    if username:
        user = UserService.by_name(username)
        if user and user.verify_password(request.POST.get('password')):
            headers = remember(request, user.name)
        else:
            headers = forget(request)
    else:
        headers = forget(request)
    return HTTPFound(location=request.route_url('home'), headers=headers)


@view_config(route_name='auth', match_param='action=reg', renderer='string', request_method='POST')
def registration(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    id = UserService.get_new_id()
    new = User()
    new.id = id
    query = DBSession.query(User)
    if username and password:
        for q in query:
            if q.name == username:
                return HTTPFound(location=request.route_url('home'))
        new.name= username
        new.password = password
    DBSession.add(new)
    headers = remember(request, username)
    return HTTPFound(location=request.route_url('home'), headers=headers)
