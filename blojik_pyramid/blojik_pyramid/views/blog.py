from pyramid.view import view_config
from pyramid.security import authenticated_userid
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from ..models.meta import DBSession
from ..models.blog_record import BlogRecord
from ..models.services.blog_record import BlogRecordService
from ..forms import BlogCreateForm, BlogUpdateForm


@view_config(route_name='blog', renderer='blojik_pyramid:templates/view_blog.jinja2')
def blog_view(request):
    blog_id = int(request.matchdict.get('id', -1))
    entry = BlogRecordService.by_id(blog_id)
    if not entry:
        return HTTPNotFound()
    return {'entry': entry}


@view_config(route_name='blog_action', match_param='action=create', renderer='blojik_pyramid:templates/edit_blog.jinja2', permission='create')
def blog_create(request):
    entry = BlogRecord()
    form = BlogCreateForm(request.POST)
    entry.user_create = authenticated_userid(request)
    if request.method == 'POST' and form.validate():
        form.populate_obj(entry)
        DBSession.add(entry)
        return HTTPFound(location=request.route_url('home'))
    return {'form': form, 'action': request.matchdict.get('action')}


@view_config(route_name='blog_action', match_param='action=edit', renderer='blojik_pyramid:templates/edit_blog.jinja2', permission='edit')
def blog_update(request):
    blog_id = int(request.params.get('id', -1))
    entry = BlogRecordService.by_id(blog_id)
    if not entry:
        return HTTPNotFound()
    form = BlogUpdateForm(request.POST, entry)
    if request.method == 'POST' and form.validate():
        form.populate_obj(entry)
        return HTTPFound(location=request.route_url('blog', id=entry.id, slug=entry.slug))
    return {'form': form, 'action': request.matchdict.get('action')}


@view_config(route_name='blog_action', match_param='action=del', renderer='blojik_pyramid:templates/edit_blog.jinja2')
def delete(request):
    blog_id = int(request.params.get('id', -1))
    entry = DBSession.query(BlogRecord).filter(BlogRecord.id == blog_id).first()
    DBSession.delete(entry)
    return HTTPFound(location=request.route_url('home'))