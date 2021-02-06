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

### Contents of the Repository

Navigate to the repository by changing your working directory in the command line. Use the same command as above to accomplish this. 

You can see the files inside by running the following command:

```sh
ls
```

You should see a few files. This file is the 'README' file, which explains the setup and instructions to play the game. The file called 'game.py' contains the code that is executed to play the game.  The '__init__' file allows all of the files to work with each other in order to execute the program. The final document, 'requirements' we will discuss later.

### Creating a new Environment

You will need to create a new environment in which to store environment variables. Your PLAYER_NAME variable, which I will discuss later, is an environment variable that is a part of the application.

To create and activate a new environment, enter the following commands into your command prompt:

```sh
conda create -n my-game-env python=3.8
conda activate my-game-env
```
You only need to create the environment the first time you run the application, however you may need to activate the environment more than once.

Now that our environment is created, we will need a document that can store our environment variable, PLAYER_NAME. We satisfy this by entering the following command into the command line:

```sh
touch .env
```
This will create a blank '.env' file. Open the '.env' file and enter your desired username, following the exact syntax below. Any misspellings of the variable name, missing quotation marks, or wrong capitalizations will result in the application failing.

    PLAYER_NAME="John Smith"

Please remember to save the '.env' file once your player name is correct.

### Installing Necessary Packages

Now we will use the 'requirements' file to download and install any necessary third-party python packages. This file contains a package called 'dotenv', which will read the information in our '.env' file and store it as an environment variable.

To install the package within the 'requirements' file, enter the following command into your command line:

```sh
pip install -r requirements.txt
```
Now, your set up is complete, and you are ready to play the game!

## Playing the Game

To start the game, simply input the following command:

```sh
python game.py
```

If everything is set up correctly, you should now see this:

```
------------------------------
Rock, Paper, Scissors, Shoot!
-----------------------------
Welcome John Smith! Please select either 'rock', 'paper', or 'scissors':
```

Now, input either 'rock', 'paper', or 'scissors' exactly as shown above. Once again, any misspellings, wrongly capitalized letters, or different inputs will cause the game to fail, and you will have to restart.

Once you make your input, the computer will randomly select a choice, and the application will determine a winner. 
