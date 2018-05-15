# Reference Server
Reference Sequence Retrieval API implementation (part of gsoc project)

## Steps to run the server locally

```
git clone https://github.com/someshchaturvedi/reference_server.git
cd reference_server
python manage.py runserver
```
## APIs
```
GET /sequence/:id
```

**Ranged queries Support** : start/end and Range header both  
**Encoding support** : text/plain  
**Circular Chromosome Support** : Yes  
**Errors Handled** :Yes (as far as I could think of)
