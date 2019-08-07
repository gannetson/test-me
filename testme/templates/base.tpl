{% load static %}
<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="{% static '/css/bootstrap.min.css' %}">
    <link href="{% static '/css/bootstrap-darkly.min.css' %}" rel="stylesheet"`>
    <title>Basic Django Testing</title>
</head>
<body>

<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Django Testing</a>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="{% url 'home_view' %}">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="{% url 'user_list' %}">Users</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="{% url 'ticket_list' %}">Tickets</a>
      </li>
    </ul>
  </div>
</nav>

<div class="container">
    <div class="page-header" id="banner">
        <div class="row">
          <div class="col-lg-8 col-md-7 col-sm-6">
            {% block header %}
                <h1>Welcome</h1>
            {% endblock %}
          </div>
        </div>
      </div>

    <div class="bs-docs-section">
        {% block content %}
            Start testing!
        {% endblock %}
    </div>
</div>
<!-- Optional JavaScript -->
<!-- jQuery first, then Popper.js, then Bootstrap JS -->
<script src="{% static '/js/jquery-3.3.1.slim.min.js' %}"></script>
<script src="{% static '/js//popper.min.js' %}"></script>
<script src="{% static '/js/bootstrap.min.js' %}"></script>
</body>
</html>
