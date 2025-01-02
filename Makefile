deploy-frontend-prod:
	rsync -av --progress --delete _site/ serveur:~/cedric-portfolio
