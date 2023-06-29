Bugs:

- Images does not load in Heroku.    
Fixed by remove disable static flag in settings, then load static in all templates that need it and change src to {% static 'images/placeholder.jpg' %}