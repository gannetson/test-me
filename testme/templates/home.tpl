{% extends 'base.tpl' %}

{% block content %}
    <a href="{% url 'user_list' %}">Users</a>
    <a href="{% url 'ticket_list' %}">Tickets</a>

{% endblock %}
