{% extends 'base.tpl' %}

{% block content %}
    <a href="{% url 'home_view' %}">&laquo; Home</a>
    <h2>Users</h2>
    <ul>
        {% for user in object_list %}
            <li>
                <b>{{user.full_name}}</b>
                <i>{{user.email}}</i>
            </li>
        {% endfor %}
    </ul>
{% endblock %}
