"""
=========================================================
Topic : Requests API in Python
=========================================================

This program demonstrates:
1. GET Request
2. POST Request
3. PUT Request
4. DELETE Request
5. Query Parameters
6. Headers
7. JSON Response
8. Status Codes
9. Exception Handling
10. Practical Examples

Install requests module:
pip install requests
"""

import requests

print("=" * 60)
print("REQUESTS API IN PYTHON")
print("=" * 60)

# =======================================================
# GET REQUEST
# =======================================================

print("\n1. GET Request")

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print("Status Code:", response.status_code)

print("Title:", response.json()["title"])

# =======================================================
# JSON RESPONSE
# =======================================================

print("\n2. JSON Response")

data = response.json()

print("User ID :", data["userId"])
print("Post ID :", data["id"])
print("Body    :", data["body"])

# =======================================================
# QUERY PARAMETERS
# =======================================================

print("\n3. Query Parameters")

params = {
    "userId": 1
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
)

posts = response.json()

print("Posts Found:", len(posts))

# =======================================================
# HEADERS
# =======================================================

print("\n4. Custom Headers")

headers = {
    "User-Agent": "Python Requests Demo"
}

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/2",
    headers=headers
)

print("Status:", response.status_code)

# =======================================================
# POST REQUEST
# =======================================================

print("\n5. POST Request")

new_post = {
    "title": "Python Tutorial",
    "body": "Learning Requests Library",
    "userId": 101
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post
)

print("Created:", response.status_code)
print(response.json())

# =======================================================
# PUT REQUEST
# =======================================================

print("\n6. PUT Request")

updated_post = {
    "id": 1,
    "title": "Updated Title",
    "body": "Updated Content",
    "userId": 1
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json=updated_post
)

print("Updated:", response.status_code)

# =======================================================
# DELETE REQUEST
# =======================================================

print("\n7. DELETE Request")

response = requests.delete(
    "https://jsonplaceholder.typicode.com/posts/1"
)

print("Delete Status:", response.status_code)

# =======================================================
# RESPONSE HEADERS
# =======================================================

print("\n8. Response Headers")

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1"
)

print("Content Type:",
      response.headers["Content-Type"])

# =======================================================
# EXCEPTION HANDLING
# =======================================================

print("\n9. Exception Handling")

try:

    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        timeout=5
    )

    response.raise_for_status()

    print("Request Successful")

except requests.exceptions.RequestException as error:

    print("Error:", error)

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

print("\n10. Display First Five Posts")

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts"
)

posts = response.json()

for post in posts[:5]:
    print(post["id"], "-", post["title"])

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

print("\n11. Display User Information")

response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1"
)

user = response.json()

print("Name :", user["name"])
print("Email:", user["email"])
print("City :", user["address"]["city"])

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

print("\n12. Display Todo")

response = requests.get(
    "https://jsonplaceholder.typicode.com/todos/1"
)

todo = response.json()

print("Task :", todo["title"])
print("Completed:", todo["completed"])

# =======================================================
# PRACTICAL EXAMPLE 4
# =======================================================

print("\n13. Display Comments")

response = requests.get(
    "https://jsonplaceholder.typicode.com/comments",
    params={"postId": 1}
)

comments = response.json()

for comment in comments[:3]:
    print(comment["name"])

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. requests.get() -> Retrieve data")
print("2. requests.post() -> Send new data")
print("3. requests.put() -> Update data")
print("4. requests.delete() -> Delete data")
print("5. response.json() -> Parse JSON")
print("6. response.status_code -> HTTP Status")
print("7. response.headers -> Response Headers")
print("8. params -> Query Parameters")
print("9. headers -> Custom HTTP Headers")
print("10. raise_for_status() -> Raise HTTP Errors")

print("\nEnd of Program")