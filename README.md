**Splatoon 3 Tournament Stats Manager (WIP)** is a set of scripts intended to upload data for Splatoon 3 private battles played during tournament sets from the Splatnet 3 service to a host service.
This project is currently a work in progress. 

Plan Statement: I want to make a tool that Splatoon 3 Tournament Organizers (TOs) can use in high-production stats-focused tournaments to easily compile and access information about each match played, and to cut down on data entry for those tournaments that previously took volunteers up to hundreds of combined hours for season-type tournaments. 

The goal is to eliminate as much work for the user as possible so that a TO can run the service and players can run the submission program either during or directly after a tournament and have the data automatically processed and easily accessed. 

# Completed Features: 
- Data structures and methods to store and access information about a tournament
- A module that accesses the API of the tournament website Battlefy and returns lists of objects corresponding to tournament data
- A command line interface and set of functions to print the created lists or search them for specific entries or sublists
- Modular design for clarity of project structure

# Planned Functionality: 
- Support for tournament websites other than Battlefy (Start.gg, Challonge)
- A process to update data for a tournament as it is played rather than only building a completed tournament
- SQL Database design rather than the list-based design to improve efficiency of search functions and make data both more accessible and more publishable
- A server/client design so that s3tsm can be run by a tournament organizer and automatically receive data from players
- A second app that imports data from the Splatnet 3 app and sends it to a host running the manager application
- Data structures and methods to store and access information received from the Splatnet 3 app
- Logic to identify which match data was received and store it as a property of the corresponding match
- An improved interface for a general userbase to replace the shell-style terminal

Credit to: 
s3s by frozenpandaman: https://github.com/frozenpandaman/s3s/blob/master/s3s.py

The portion of s3tsm that accesses the Splatnet 3 API will be based on s3s, which inspired me to make this project by showing me what was already possible.
