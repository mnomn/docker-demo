# Run docker container based on image

#delete container after run (-rm)
#docker run -d --rm --name python-app -p 54322:54322 my-python-app

#Normal docker run
#docker run --name python-app -p 5000:5000 my-python-app

#docker run interactive
docker run --name python-app --rm -p 5000:80 my-python-app
