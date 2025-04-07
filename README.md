# pySorts

pySorts was designed to fill the gap between a textbook explanation of algorithmic
complexity and websites or videos that show each animated step of a sorting algorithm.

The goal of the app is to demonstrate what the response curve of a simple algorithm
looks like when run on actual hardware, and to expose the natural variations in real
runtimes to students.

Over time more features have been added but the core purpose of the tool is still
to provide a responsive view into the asymptotic runtimes of a few common algorithms.

Features:

- Compare sort algorithms
- Compare languages
- Compare input array types
- Apply smoothing filters to graphs
- Apply frequency analysis filters to graphs

## Set Up

All of the following assumes you are set up in a unix-like environment. All common
Linux, Mac-Os and WSL (windows) users should have minimal errata required for
setting up.

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
docker compose up --build
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
