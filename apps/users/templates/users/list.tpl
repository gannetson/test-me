{% extends 'base.tpl' %}

{% block header %}
    <h1>Users</h1>
{% endblock %}

{% block content %}
    <table class="table table-hover">
        <thead>
            <tr class="table-success">
                <th scope='col'>Name</th>
                <th scope='col'>Email</t>
            </tr>
        </thead>
        <tbody>
            {% for user in object_list %}
                <tr class="{% cycle 'table-primary' 'table-secondary' %}>">
                    <td>{{user.full_name}}</td>
                    <td>{{user.email}}</td>
                </tr>
            {% endfor %}
        </tbody>
    </ul>
{% endblock %}
