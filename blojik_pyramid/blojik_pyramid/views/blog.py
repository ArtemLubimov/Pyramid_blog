from pyramid.view import view_config
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from ..models.meta import DBSession
from ..models.blog_record import BlogRecord
from ..models.services.blog_record import BlogRecordService


@view_config(route_name='blog', renderer='blojik_pyramid:templates/view_blog.mako')
def blog_view(request):
    return {}


@view_config(route_name='blog_action', match_param='action=create', renderer='blojik_pyramid:templates/edit_blog.mako')
def blog_create(request):
    return {}


@view_config(route_name='blog_action', match_param='action=edit', renderer='blojik_pyramid:templates/edit_blog.mako')
def blog_update(request):
    return {}


@view_config(route_name='blog', renderer='blojik_pyramid:templates/view_blog.mako')
def blog_view(request):
    blog_id = int(request.matchdict.get('id', -1))
    entry = BlogRecordService.by_id(blog_id)
    if not entry:
        return HTTPNotFound()
    return {'entry': entry}
