{% extends 'base.tpl' %}


{% block header %}
    <h1>Tickets</h1>
{% endblock %}


{% block content %}
    <table class="table table-hover">
        <thead>
            <tr class="table-warning">
                <th scope='col'>Name</th>
                <th scope='col'>Price</t>
                <th scope='col'>Early bird</t>
            </tr>
        </thead>
        <tbody>
            {% for ticket in object_list %}
                <tr class="{% cycle 'table-primary' 'table-secondary' %}>">
                    <td>{{ticket.name}}</td>
                    <td>{{ticket.price}}</td>
                    <td>{{ticket.early_bird_price}}</td>
                </tr>
            {% endfor %}
        </tbody>
    </ul>
{% endblock %}
