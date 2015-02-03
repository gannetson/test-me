{% extends 'base.tpl' %}

{% block content %}
    <a href="{% url 'home_view' %}">&laquo; Home</a>
    <h2>Tickets</h2>
    <ul>
        {% for ticket in object_list %}
            <li>{{ticket.name}} <i>{{ticket.price}} (early bird {{ticket.early_bird_price}})</i> </li>
        {% endfor %}
    </ul>
{% endblock %}
