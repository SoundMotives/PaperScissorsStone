# Paper Scissors Stone project

As part of reviewing [Makers' Web Applications In Python](https://github.com/makersacademy/web-applications-in-python/), this is the Paper Scissors Stone challenge in the 'Going Further' section. 

It used the [Python Flask HTML starter project](git@github.com:makersacademy/web-applications-in-python-project-starter-html.git), but as this project doesn't use a database it's much simpler. 

To run this Paper Scissors Stone application locally follow the below instructions:

## Setup

# Clone the repository to your local machine
; git clone git@github.com:makersacademy/web-applications-in-python-project-starter-html.git YOUR_PROJECT_NAME

```shell
# Clone the repository to your local machine
; git clone https://github.com/SoundMotives/PaperScissorsStone.git YOUR_PROJECT_NAME

# Or, if you don't have SSH keys set up
; git clone https://github.com/makersacademy/web-applications-in-python-project-starter-html.git YOUR_PROJECT_NAME

# Enter the directory
; cd YOUR_PROJECT_NAME

# Install dependencies and set up the virtual environment
; pipenv install

# Activate the virtual environment
; pipenv shell

# Install the virtual browser we will use for testing
; playwright install
# If you have problems with the above, contact your coach

# Create a test and development database
; createdb YOUR_PROJECT_NAME
; createdb YOUR_PROJECT_NAME_test

# Open lib/database_connection.py and change the database names
; open lib/database_connection.py

# Seed the development database (ensure you have run `pipenv shell` first)
; python seed_dev_database.py

# Run the tests (with extra logging)
; pytest -sv

# Run the app
; python app.py
# Now visit http://localhost:5001/emoji in your browser
```

If you would like to remove the example code:

```shell
; ./remove_example_code.sh
```


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python-project-starter-html&prefill_File=README.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python-project-starter-html&prefill_File=README.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python-project-starter-html&prefill_File=README.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python-project-starter-html&prefill_File=README.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python-project-starter-html&prefill_File=README.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->


## Setup

* [A demonstration of setting up the project](https://www.youtube.com/watch?v=YStsRfMVx44&t=0s)
* [A walkthrough of the project codebase](https://www.youtube.com/watch?v=YStsRfMVx44&t=314s) 
