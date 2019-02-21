# A Basic Voice based application

This is a simple Flask based application that does two things
- Converts text to speech using the `Say` call function
- Plays a pre-recorded media file from a CDN using the `Play` call function

## Running this app

Clone this repo to your machine and run `source ./venv/bin/activate`. This will create a new Python virtual environment with all the dependencies pre-installed. 

## Running the app with Docker

Coming soon

## Testing the app's response

Use Postman to check what the application returns. 

This is the payload to send through post man

```
{
  "callStartTime": "2019-02-19+12:56:27",
  "callerNumber": "+255652353788",
  "callerCountryCode": "255",
  "isActive": "1",
  "destinationNumber": "+254711082518",
  "direction": "Inbound",
  "sessionId": "ATVId_5789c1ea623f669f798e79a7a55fbc47"
}
```