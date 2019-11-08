# RTask

## Running (simplified)

1. Clone the repo, if you haven't already, and `cd` to it
`git clone https://github.com/RTask/RTask.git`
`cd RTask/`

2. Create a virtual environment for python, so that
packages are not installed globally.
`python3 -m venv .`

3. Install dependencies.
`pip install -r requirements.txt`

4. Database: This is an optional way to do it (for now), with docker:

   `docker run --rm --name rtask-db -e POSTGRES_PASSWORD=RobedCoder -e POSTGRES_DB=rtask -p5432:5432 -d postgres`

   Explanation of that command line:
   * docker run: tells docker to run an image
   * --rm: remove this container when it is stopped, so that resources aren't being held on to
   * --name rtask-db: name this container 'rtask-db'. It could be anything.
   * -e POSTGRES_PASSWORD=... -e POSTGRES_DB=rtask : environment variables set inside the container,
     so that we have a database set up for us
   * -p5432:5432 : expose port 5432 from inside the container to port 5432 on the host system
   * postgres : the name of the docker image to run. This will run the latest version, which for
     our sake is fine. Docker will pull the image the first time if it's not already located locally.

