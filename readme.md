# Event Calendar

Time to create another CRUD app. This time, we're going to make a basic list
of events, to keep track of your busy social schedule.

Unlike the TODO challenge, this challenge won't provide you with the test stubs
for your implementation. The goal here is for you to start to remember each of
the actions for your view on your own. Try creating as much of the app as
you can from memory, using tests to guide your implementation.

Once you've completed the app (or when you get totally stuck), take a look back
at the previous challenge and see if you hit all the requirements for a CRUD
view and implement any that are missing.

## Release 0: Getting Ready
Start by creating a new virtual environment and then activate it. 
`python3 -m venv venv`
`source venv/bin/activate`

One you have your virtual environment up and running you can tell pip to download all the requirements for this app so far by running `pip install -r requirements.txt`. Make sure you are in the main directory of the repo (the one with the readme in it).

Next set up the database `djangoeventcalendar` by running `createdb djangoeventcalendar`. 

Remember to run your migrations before you get started on your routes. 

As with the previous challenge, the model and migration for this activity have
already been created for you.  Our model is fairly similar to the last time: we
have a title and a description, but this time we also have a starting and
ending date and time. 

## Release 1-N: Complete the CRUD App

You're on your own for the rest of this exercise! Hopefully creating django
routes is starting to get more familiar, but don't worry if it's still all a
blur. Over time, this process will become second nature.

Good luck!
