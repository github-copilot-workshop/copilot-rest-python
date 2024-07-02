
# New API Routes

>If you are note using Codespaces, make sure you run 
>
> ```
> cd copilot
>
> python -m pip install -r requirements.txt
>```
>
> before starting this exercise.

You can start the server by running, in the `$PROJECT_ROOT/copilot` directory the following command

```bash
python manage.py runserver  
```

The project is a Django project with a single app called `api` that contains a single route `/api/time` that returns the current date time as JSON.

The current route return the current Date Time as JSON, for example open a terminal and run:

```bash
curl http://localhost:8000/api/time/
```

This should return the current date time in JSON format.

## 001 Add a new route "Hello World"

`curl -L http://localhost:8000/api/hello?key=World` 

should return the JSON 

`{"message": "Hello World"}`

and should return a `HTTP 500` code when the query parameter `hello` is not present.

The test is already written in the file `copilot/api/tests.py` and it is failing, you are done when the test pass.

To run the tests, open a terminal and run the following command:

```bash
cd copilot

python manage.py test
```

<details>

<summary>Possible Flow</summary>

1. Open the file `./copilot/api/views.py`

2. Add a new route to the file using a simple comment for example

```python
# Create a new function GET hello?key=World
# that returns a JSON {"message": "Hello World"} when the query parameter key is present
# and return HTTP 500 code with message "key query parameter is required"
# when the query parameter key is not present
```

3. Keep the views file opened and open the `./copilot/api/urls.py` file

4. Add a comment to the file to ask Copilot to add the new route for get_hello function



3. Let the code be generated from the comment

> Note: it is true that the comment is longer that the code, but this is done to learn how to use copilot and understand the importance of being precise in the "prompt".

</details>

---
