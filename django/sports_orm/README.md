###Clone this repo for the CodingDojo Sports ORM assignments in the Django Level 2 curriculum.

`git clone https://github.com/madjaqk/sports_orm.git`

When you `python manage.py runserver` and naviate to localhost:8000, you should see a list of leagues, teams, and players.  Modify `apps/leagues/views.py` and/or `apps/leagues/templates/leagues/index.html` to change the displayed list.

####Questions:

[Simple finds](level_1.md)

[ForeignKey relationships](level_2.md)

[ManyToMany relationships](level_3.md)

Assignment: Sports ORM

Using the sports_orm, complete all the following queries and show their results on index.html.

The purpose of this assignment is to practice using the Django ORM to make queries on a pre-existing database. You MUST install the sports_orm before you can complete this assignment. In your Django folder, run this terminal command: git clone https://github.com/madjaqk/sports_orm.git This will create a folder named sports_orm; if you cd into this new folder and python manage.py runserver, you should see lists of sports leagues, teams, and players. Your goal for this assignment is to modify apps/leagues/views.py and/or apps/leagues/templates/leagues/index.html so that instead the page shows:

    ...all baseball leagues
    ...all womens' leagues
    ...all leagues where sport is any type of hockey
    ...all leagues where sport is something OTHER THAN football
    ...all leagues that call themselves "conferences"
    ...all leagues in the Atlantic region
    ...all teams based in Dallas
    ...all teams named the Raptors
    ...all teams whose location includes "City"
    ...all teams whose names begin with "T"
    ...all teams, ordered alphabetically by location
    ...all teams, ordered by team name in reverse alphabetical order
    ...every player with last name "Cooper"
    ...every player with first name "Joshua"
    ...every player with last name "Cooper" EXCEPT those with "Joshua" as the first name
    ...all players with first name "Alexander" OR first name "Wyatt"

Hint: Try editing the context dictionary for these queries!
context = {
	# commenting out the "leagues" key so they don't conflict
	# "leagues": League.objects.all(),
	"teams": Team.objects.all(),
	"players": Player.objects.all(),
	# query 1: All baseball leagues
	"leagues": League.objects.something(something=something),
}
