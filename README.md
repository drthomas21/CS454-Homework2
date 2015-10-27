CS454 Multiplayer - Homework 2
==============================
# Members:
- Julian Parmentier-Berlin
- Manish Purohit
- Vatsal Sevak
- David Thomas

# How To Run:
*will be added later*

# Database Scheme:
*will be added later*

# Protocols:
- Code: 101 = Send login information (Authentication)
  - String: username
  - String: password
    - *Return values* --> Short : 1 for successful authentication
                      --> Short : 0 for failure
- Code: 201 = login successful
- Code: 301 = login failure
- Code 102 = Send register information
  - String: username
  - String: password
- Code 202 = register success
- Code 302 = register failure
- Code 112 = Send chat message to server
  - String: message(?)
- Code 212 = Recieve chat message from server
  - String: message(?)
