install: #установка
	poetry install

brain-games: #запуск brain-games
	poetry run brain-games

build: #Сборка дистрибутива
	poetry build

publish: 
	poetry publish --dry-run

package-install: #установка пакета из ос
	python3 -m pip install --user dist/*.whl

lint: #запуск flake8
	poetry run flake8 brain_games
