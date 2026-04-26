
import xmlrpc.client
# Set up client proxy to connect to server

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/RPC2")
dictionary_data = {
  "ocean": "A large body of salt water that covers most of Earth's surface.",
    "mountain": "A large natural elevation of the Earth's surface rising abruptly from the surrounding level.",
    "forest": "A large area covered chiefly with trees and undergrowth.",
    "desert": "A barren area of land where little precipitation occurs and living conditions are hostile for plant and animal life."
}

response = proxy.upload_dictionary(dictionary_data)
print(response)
word = "ocean"
meaning = proxy.get_meaning(word)
print(f"The meaning of '{word}' is: {meaning}")
word = "mountain"
meaning = proxy.get_meaning(word)
print(f"The meaning of '{word}' is: {meaning}")
word = "forest"
print(f"The meaning of '{word}' is: {meaning}")
word = "desert"
meaning = proxy.get_meaning(word)
print(f"The meaning of '{word}' is: {meaning}")