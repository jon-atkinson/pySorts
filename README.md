# pySorts v1

This branch contains the first stable iteration of pySorts.
It depricates the tkinter gui due to instability on some OS configurations and a dependance on tk-tcl which makes it impossible to run in some environments.
V1 is fully containerized using docker-compose and can be deployed in any environment with a working docker-compose configuration.
Alteratively, running the database, backend and frontend in that order in seperate local terminals is also supported.

Simple collection of sorts, testing and comparison CLI for comparing the
implementations of many commonly used and some more complex sorting algorithms.
Algorithm implementations available only in python and C for the moment.

## Getting pySorts Running

### Deploying with Docker

Ensure you have docker-compose installed and working by running the following command.

```
docker-compose version
```

Start by cloning this repo into a local directory.

```
git clone https://github.com/jon-atkinson/pySorts.git
```

Then run the following command from the pySorts directory to build the containers, create the image and start the server.

```
docker-compose up --build
```

### Running in Local Environment Without Containers

Start by cloning this repo into a local directory.

```
git clone https://github.com/jon-atkinson/pySorts.git
```

#### Build the components

Ensure the C binaries are built for your archtecture by running the following command (this may require installing build dependencies).

```
cd backend && chmod +x ./compile.sh && ./compile
```

Install redis-server using one of the following commands depending on your package manager.

```
brew install redis
```

```
sudo snap apt update
sudo apt install redis-tools
sudo snap install redis
```

```
sudo apt-get install lsb-release curl gpg
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
sudo chmod 644 /usr/share/keyrings/redis-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
sudo apt-get update
sudo apt-get install redis
```

Install dependencies for pySorts/backend. This will be different depending on your package manager (uv and pip examples shown).

```
uv sync
```

```
pip install .
```

Install dependencies for pySorts/frontend.

```
npm i
```

#### Running the different components

Start the database server.

```
redis-server
```

```
sudo snap start redis
```

```
sudo systemctl enable redis-server
sudo systemctl start redis-server
```

Start the backend server in a new terminal from pySorts/backend (again, this is different depending on the python package manager you're using).

```
uv run fastapi run src/main.py
```

```
python3 src/main.py
```

Start the React frontend server in a new terminal from pySorts/frontend.

```
npm run start
```

## Using the Application

Once you have a database, backend and frontend server running, navigate to
`localhost:3000` or `127.0.0.1:3000` in a browser.

The important options are located in the sidebar. There are seperate pages for
comparing different algorithm implementations and comparing the performance of
a single algorithm on differently sorted arrays.

Generating results is also relatively expensive so results of previous runs are
cached in the Redis database and an outline of all stored results is located on
another page. Here you can delete or choose to graph any stored result.

### Troubleshooting

If you see `Error: Network Error` in the frontend UI, the frontend can't connect
to the backend to get a config packet that tells it what algorithms and arrays
are available.

Redis uses the default port, if you already run Redis for something else and have
key clashes, a non-containerized method may require some tweaking of environment
variables or source code.

In general, the containerized method is much simpler and more robust and as such
is the recommended approach if local setup has specific and challenging issues

## Testing the Application

Currently all backend modules are fully tested (including mocking Redis DB
interactions) but the frontend is not.

### Running the backend tests

Depending on your python manager run one of the following from pySorts root.

```
cd backend && uv run pytest
```

```
cd backend && python3 pytest
```
