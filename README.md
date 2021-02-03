# Rock, Paper, Scissors Application

These files, when run correctly, will produce a game of rock, paper, scissors in the Terminal (Command Prompt) for the user to play against a computer. The user is able to input their user name and choice of "rock", "paper", or "scissors". The computer then makes a random selection and the application determines a winner. 

The rest of this README file will list instructions on how to setup and run this application.

## Setting up the Application

### Repo Setup

Use the GitHub website to fork this remote repository (https://github.com/acataldo29/rock-paper-scissors) into your account. Before cloning the repository, ensure that your working directory is correct/suitable. Check and change your working directory using the following commands:

```sh
pwd
cd your/desired/path
```

Then clone the respository to your local device by navigating to the Terminal (Command Prompt) and entering the following command:

```sh
git clone https://github.com/acataldo29/rock-paper-scissors.git
```

Your repository will save to your desired working directory. 

## Contents of the Repository

Navigate to the repository by changing your working directory in the command line. Use the same command as above to accomplish this. You can see the files inside by running the following command:

```sh
ls
```

You should see two files: README.md (this file) and game.py. The second file, game.py, contains the code that is executed to play the game. 

## Playing the Game

To start the game, simply input the following command:

```sh
python game.py
```

You will then be prompted to enter a user name, which can be anything you'd like. Then, the application will prompt you to enter your choice. You must type either "rock", "paper", or "scissors