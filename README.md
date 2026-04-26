# Distributed Dictionary System using XML-RPC

## Overview
This project demonstrates a simple client–server architecture using XML-RPC in Python.  
It allows a client to upload a dictionary of words and retrieve meanings remotely from a server.

---

## System Design
- Server stores a dictionary in memory
- Client communicates with server using XML-RPC protocol
- Data is transferred over HTTP locally

---

## Features
- Upload dictionary from client to server
- Retrieve meaning of a word remotely
- Simple distributed system communication

---

## Server Side
- Implements XML-RPC server
- Stores dictionary in memory
- Provides two functions:
  - upload_dictionary()
  - get_meaning()

---

## Client Side
- Connects to server using ServerProxy
- Sends dictionary data
- Requests word meanings

---

## Concepts Covered
- Client–Server Architecture
- Remote Procedure Call (RPC)
- XML-RPC in Python
- Network communication basics

---

## Tools Used
- Python
- xmlrpc.server
- xmlrpc.client

---

## How It Works
1. Server starts on localhost
2. Client connects to server
3. Client uploads dictionary
4. Client requests word meanings
5. Server responds with stored data

---

## Example Output
- ocean → Large body of salt water
- mountain → Large natural elevation
- forest → Area covered with trees
- desert → Dry barren land

---

## Author
Arwaa Mamdoh
