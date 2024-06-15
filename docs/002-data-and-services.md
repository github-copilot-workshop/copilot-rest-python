# Generate Sample Data 

In this lab you will learn how to use Copilot to generate sample data for your application.


## 001 Create a new API that list Microsoft Azure VMs informations

Add a new route `http://localhost:8000/api/azure-vms` that returns a list of VMs with some properties, that will come from a local JSON file.


when calling:

```bash
curl http://localhost:8000/api/azure-vms
```

The API should return a list of VMs with the following properties:

```json
[
   ...
  {
    "size": "Standard_D32_v3",
    "vcpu": 32,
    "memory": 128,
  },
  ....
  {
    "size": "Standard_D64_v3",
    "vcpu": 64,
    "memory": 256,
  }
]
```


You can find the VMs properties here https://learn.microsoft.com/en-us/azure/virtual-machines/dv3-dsv3-series?source=recommendations 

> Tip: see how you can format the data in the chat using a simple copy/paste from the website.


<details>

<summary>Possible Flow</summary>

1. Generate the data from the website
  - Go to https://learn.microsoft.com/en-us/azure/virtual-machines/dv3-dsv3-series?source=recommendations
  - Copy the data from the table

2. Ask the following question in the chat
   - _Using the following data, create a JSON Array, with the fields Size, vCPU and Memory. Put the field name in lowercase. The Memory field should be a number without unit (since the default is GiB_
   - Paste the content from Wikipedia in the chat
   - This should generate a new JSON array

   
3. Click in the [...] button in the chat and select "Insert into New File" 

4. Create a the file : `$PROJECT_HOME/copilot/data/vms.json`

6. Open the file `$PROJECT_HOME/copilot/views.py` and add the following code
    - In the chat enter the following question : 
    - _Create a new GET view that read the ./data/vms.json file and return the JSON content_
    - The code should be something like this:
      ```python
      @api_view(['GET'])
      def get_vms(request):
        try:
          with open('./data/vms.json', 'r') as file:
            data = json.load(file)
          return JsonResponse(data, safe=False, status=status.HTTP_200_OK)
        except FileNotFoundError:
          return JsonResponse({'message': 'File not found'}, status=status.HTTP_404_NOT_FOUND)
      ```

8. Open the file `$PROJECT_HOME/copilot/urls.py` 
    - Go to the end of the list of urls, and add the new one,
    - Copilot should complete the code for you
      ```python
      urlpatterns = [
        path('time/', views.get_current_time),
        path('hello/', views.get_hello),
        path('vms/', views.get_vms),
      ]
      ```
   

9. In the terminal:
    - Make sure you are in the directory `/copilot-rest-python/copilot/`
    - Restart Django
      ```bash
      python manage.py runserver
      ```
    - Go to the browser and access the URL `http://localhost:8000/api/vms/`

    - You will probably have an error, if you have an error, go in the terminal select the error message and do:
    
    - right-click > `Copilot : Explain this`

10. When Fixed restart the server and test the API again

</details>


## 002 Add a test for the new API

Add new tests for the new API that list Microsoft Azure VMs informations.

<details>

<summary>Possible Flow</summary>

1. Open the file `$PROJECT_HOME/copilot/tests.py` and add the following code

    - Use the inline completion to write a new test
    - Something like :

      ```python
      class VmsAPITestCase(APITestCase):
          api_path = '/api/vms/'

          def test_get_vms(self):
              response = self.client.get(self.api_path)

              # Check if the response status code is 200
              self.assertEqual(response.status_code, 200)

              # The response content should be an array
              response_data = json.loads(response.content)
              self.assertIsInstance(response_data, list)
      ```


2. Go in the Chat, and ask the following question to test some values

    - Ask the following question using the `#file` command :
    - _Add some tests in #file:tests.py that validates the API based on the data found in #file:vms.json_

    - The generated test could look like 
      ```python
      class VmsDataAPITestCase(APITestCase):
          api_path = '/api/vms/'

          # Existing test_get_vms method...

          def test_vms_data_validation(self):
              expected_vms_data = [
                  {"size": "Standard_D2_v3", "vcpu": 2, "memory": 8},
                  {"size": "Standard_D4_v3", "vcpu": 4, "memory": 16},
                  {"size": "Standard_D8_v3", "vcpu": 8, "memory": 32},
                  {"size": "Standard_D16_v3", "vcpu": 16, "memory": 64},
                  {"size": "Standard_D32_v3", "vcpu": 32, "memory": 128},
                  {"size": "Standard_D48_v3", "vcpu": 48, "memory": 192},
                  {"size": "Standard_D64_v3", "vcpu": 64, "memory": 256},
              ]

              response = self.client.get(self.api_path)
              self.assertEqual(response.status_code, 200)
              response_data = json.loads(response.content)

              # Ensure the response contains the correct number of VMs
              self.assertEqual(len(response_data), len(expected_vms_data))

              # Validate each VM's data
              for vm_data in expected_vms_data:
                  self.assertIn(vm_data, response_data)    
      ```

</details>