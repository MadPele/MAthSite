deps:
	pip install -r requirements.txt
run:
	python app.py
docker_build:
	docker build -t madpele/math-site .
docker_run: docker_build
	docker run --name math-site -p 5000:5000 madpele/math-site