The Challenge
Utilising either Flask or FastAPI, create a web application that does the following.
Allows somebody to create or edit a survey. This survey will be stored as a JSON file in a Google Storage Bucket.
Allows somebody to answer a survey. This flow should save their current process / answers as they go, and allow a person to return to complete a survey at any time. The progress will be stored as a JSON object in a Google Firestore Database.
Show a completed survey. Pulling data from both the Google Storage Bucket and the Firestore Database, display a completed survey.
Would also like to see evidence of PyTest.
