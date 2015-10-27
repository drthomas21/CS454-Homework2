CS454 Multiplayer - Homework 2
==============================
## Members:
- Julian Parmentier-Berlin
- Manish Purohit
- Vatsal Sevak
- David Thomas

## How To Run:
*will be added later*

## Database Scheme:
![alt tag](https://github.com/drthomas21/CS454-Homework2/blob/master/model.png)

## Protocols **return order matters**:

- Code: 101 = Authentication request
  - String: username
  - String: password
  - *Return values* **Code: 201**
    - Short : 1 for successful authentication
    - Short : 0 for failure
- Code: 103 = Register request (+Authentication)
  - String: username
  - String: password
  - *Return values* **Code: 203**
    - Short : 1 for successful register and authentication
    - Short : 0 for failure
- Code: 105 = Moving request (let other clients know that this player moved)
  - String: position (formated as "x, y, z")
  - *Return values* **Code: 205**
    - *To all other clients* String : username
    - *To all other clients* String : position
- Code: 106 = Character selection request
  - String: character name
  - *Return values*
    - **Code: 206** String : position (Last position of this character, empty for the first time)
    - **Code: 207** *To all other clients* String : character (Let everyone know this client is online)
- Code: 112 = Chat request (from a user to every connected player)
  - String: message
  - *Return values* **Code 212**
    - *To all other clients* String : username
    - *To all other clients* String : message
- Code: 113 = Heartbeat request (demanding all the queue)
  - *Return values*
    - All the responses in the queue
    - **Code: 213** Hearthbeat response
- Code: 115 = Privatechat request (from a user to an other player)
  - String: message
  - *Return values* **Code 215**
    - *To the target user* String : username
    - *To the target user* String : message
- Code: 119 = Save and exit request
  - String: position
  - *Return values* **Code 219**
    - Short : 1 for success
    - Short : 0 for failure
