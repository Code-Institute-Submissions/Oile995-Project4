Bugs:

- Images does not load in Heroku.    
Fixed by remove disable static flag in settings, then load static in all templates that need it and change src to {% static 'images/placeholder.jpg' %}

- Create form page did not load No Workout matches the given query: 
Fixed by moving path url above display workout path

- if Workout has less than 3 exercises update crashes website
Fixed by checking if parent number of exercies is less than the generic (3)-1 and if so the indexing is updated to parents number.

- bug when updating workout, if statement had no else and caused return of html =None
Fixed by changing the if logic to check if creator or superuser

- bug user img didnt load if placeholder in first image in workout details.
fixed by changing and adding if logic in html






Source:
- F expression
https://stackoverflow.com/questions/42061353/django-queryset-update-in-way