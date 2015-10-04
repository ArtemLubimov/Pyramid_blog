<!DOCTYPE html>
<html lang="${request.locale_name}">
  <head>
    <!-- Bootstrap core CSS -->
    <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this scaffold -->
    <link href="${request.static_url('blojik_pyramid:static/theme.css')}" rel="stylesheet">
    <style type="text/css">
    a, a:link, a:visited{
        color: #ffcc00;
        font-weight: bold;
    }
    a:hover{
        color: #ffff00
    }

    </style>
    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="//oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="//oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->

    <div class="row">
        <div class="col-md-10">
            <div class="content">
              <p class="lead">Welcome to <span class="font-normal">Pyramid Blojik</span></p>
                <div>
                    <!-- this is where contents of template inheriting from this layout will be inserted -->
                  ${next.body()}
                    <!-- this is where contents of template inheriting from this layout will be inserted -->
                </div>
            </div>
        </div>
    </div>

  </head>

  <body>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="//oss.maxcdn.com/libs/jquery/1.10.2/jquery.min.js"></script>
    <script src="//oss.maxcdn.com/libs/twitter-bootstrap/3.0.3/js/bootstrap.min.js"></script>
  </body>
</html>
