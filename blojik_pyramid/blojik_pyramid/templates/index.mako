<%inherit file="blojik_pyramid:templates/layout.mako"/>
<% link_attr={"class": "btn btn-default btn-xs"} %>
<% curpage_attr={"class": "btn btn-default btn-xs disabled"} %>
<% dotdot_attr={"class": "btn btn-default btn-xs disabled"} %>


% if paginator:

    <h2>Blog entries</h2>

    <ul>
        % for entry in paginator:
            <li>
                <a href="${request.route_url('blog', id=entry.id, slug=entry.slug)}">
                    ${entry.title}</a>
            </li>
        % endfor
    </ul>

    ${paginator.pager(link_attr=link_attr, curpage_attr=curpage_attr, dotdot_attr=dotdot_attr) |n}

% else:

    <p>No blog entries found.</p>

%endif

<p><a href="${request.route_url('blog_action',action='create')}">
    Create a new blog entry</a></p>
