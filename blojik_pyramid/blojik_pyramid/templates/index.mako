<%inherit file="blojik_pyramid:templates/layout.mako"/>

<header>
% if request.authenticated_userid:
    Welcome <strong>${request.authenticated_userid}</strong>
    <a href="${request.route_url('auth',action='out')}">Sign Out</a>
%else:
    <div class="form-inline">
    <form action="${request.route_url('auth',action='in')}" method="post" >
        <div class="form-group">
            <label>User</label> <input type="text" name="username" class="form-control">
        </div>
        <div class="form-group">
        <label>Password</label> <input type="password" name="password" class="form-control">
        <input type="submit" value="Sign in" class="btn btn-default">
        </div>
    </form>
    <form action="${request.route_url('auth',action='register')}"method="post" >
            <input type="submit" value="Register" class="btn btn-default">
    </form>
    </div>
%endif
</header>

% if paginator.items:

    <h2>Blog entries</h2>

    <ul>
        % for entry in paginator.items:
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
