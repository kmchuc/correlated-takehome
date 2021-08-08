<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
I created a back-end logic along with a corresponding database to store keys and values submitted via JSON formatting with HTTP GET/POST requests. With each endpoint, conditions have been defined to ensure the user formats the input data correctly.

### Built With
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [PostgreSQL](https://www.postgresql.org/)
* [SQLAlchemy](https://www.sqlalchemy.org/)

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* environment
  ```sh
  python3 -m venv venv
  ```

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/kmchuc/correlated
   ```
2. Create a virtual environment in your project folder.
   ```sh
   cd <correlated>
   virtualenv venv
   ```
3. Activate virual environment
    ```sh
    . venv/bin/activate
    ```
4. Install python packages by running the following command
    ```sh
    pip install -r requirements.txt 
    ```

<!-- USAGE EXAMPLES -->
### Usage
I've deployed this app using Heroku, but since a front-end hasn't been made yet, the local host could also run on Postman (https://www.postman.com/). As required, the repo runs on a PORT:4000.

### "Set" endpoint:
I created a '/set' endpoint using a POST HTTP method when containing a JSON POST body formating like:
```sh
  {"key": "<some key>", "value": "<string value>" }
  ```
also shown in the example shown below:

<img width="1009" alt="Screen Shot 2021-08-07 at 2 58 27 PM" src="https://user-images.githubusercontent.com/59525393/128617400-8e885f9f-dd1d-49ed-8644-f5a277c6e66e.png">

When submitted, the key, value strings will set in the PostgreSQL database called, Data. If the strings have successfully been saved, a JSON message will appear showing the key, value strings that were saved as well as a 200 code.

<img width="1009" alt="Screen Shot 2021-08-07 at 3 04 05 PM" src="https://user-images.githubusercontent.com/59525393/128617485-7bab5fce-3bb9-425e-bc67-bc53fa608420.png">

If the user sets a key that has already been saved, the new input value will replace the previously set value within the database. When this occurs, another JSON message will output saying that the value has been updated with the newly submitted value.

<img width="1006" alt="Screen Shot 2021-08-07 at 3 07 21 PM" src="https://user-images.githubusercontent.com/59525393/128617530-fec1adc9-0830-45da-b386-e6548d79bfba.png">

If the user doesn't include a key or value string within the JSON POST body, an error message along with the error code will be output.

<img width="1008" alt="Screen Shot 2021-08-07 at 3 10 11 PM" src="https://user-images.githubusercontent.com/59525393/128617577-e9f75384-b029-4e51-87db-ab623ff0bfbb.png">

### "Get" endpoint:
The '/get' endpoint uses a GET HTTP method in the form of the url endpoint parameters, '/get?key=someKey'. When submitted, the parameter is assigned to a variable using the:
```sh
request.args.get('key')
```
The function then searches for the key within the database, checking to make sure it exists then returns the corresponding value in a JSON object:

<img width="1012" alt="Screen Shot 2021-08-07 at 3 15 29 PM" src="https://user-images.githubusercontent.com/59525393/128617645-fff13139-3a21-4f56-bae7-1557b856b0d1.png">

If a key parameter is not called, a JSON response is returned an error explaining what needs to in included.

<img width="1005" alt="Screen Shot 2021-08-07 at 3 18 51 PM" src="https://user-images.githubusercontent.com/59525393/128617710-a570d016-4c70-4dfe-b420-017896e60157.png">

If the key paramter does not exist within the database, an error message will be returned.

<img width="1012" alt="Screen Shot 2021-08-07 at 3 20 23 PM" src="https://user-images.githubusercontent.com/59525393/128617741-ae0ef18b-a796-47a6-87b1-c0dc760867e5.png">

### "Delete" endpoint:
The '/delete' endpoint uses a POST HTTP method in the form of a JSON object:
```sh
{"key": "<some key>"}
```
If the deletion is successful, a JSON is returned showing the key that has been deleted:

<img width="1013" alt="Screen Shot 2021-08-07 at 3 23 56 PM" src="https://user-images.githubusercontent.com/59525393/128617789-7a858ce9-18f9-4172-b5a5-66d5daa44c8e.png">

If the parameter called doesn't exist within the database, a corresponding JSON will be returned:

<img width="1011" alt="Screen Shot 2021-08-07 at 3 25 10 PM" src="https://user-images.githubusercontent.com/59525393/128617813-11d398da-3a29-4be6-bed6-578f088633e2.png">

If a parameter is not included within the JSON POST body, the error still passes as a 200 but an error message will return in JSON formatting:

<img width="1012" alt="Screen Shot 2021-08-07 at 3 26 06 PM" src="https://user-images.githubusercontent.com/59525393/128617830-ca4cc1bd-760a-4d79-88aa-d28ba9f71969.png">