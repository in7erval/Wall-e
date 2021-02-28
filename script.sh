heroku git:clone -a wall-e-telegram-bot
git add .
git commit -m "."
git push heroku master
heroku ps:scale worker=1
