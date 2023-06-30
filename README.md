Bugs:

- Images does not load in Heroku.    
Fixed by remove disable static flag in settings, then load static in all templates that need it and change src to {% static 'images/placeholder.jpg' %}

- Create form page did not load No Workout matches the given query: 
Fixed by moving path url above display workout path






Source:
- F expression
https://stackoverflow.com/questions/42061353/django-queryset-update-in-way