# EE250_Lab3
Lab3 of EE250: API and web Server

Question 1: Why are RESTful APIs scalable?
RESTful APIs are scalable because the previous client request information is not stored by the server, and caching is managed only partially (AWS, aws.amazon.com/what-is/restful-api/)

Question 2: According to the definition of "resources" provided in the AWS article above, what are the resources the mail server is providing to clients?
The mail server provides the clients with resources such as information about the USER name, mail ID, subject of a mail, body of a mail. 

Question 3: What is one common REST Method not used in our mail server? How could we extend our mail server to use this method? 
One common REST method that is not used in our mail server is the API keys. This could be done by creating your own API-key for your device and then using a verification function to verify that API before giving information. 

Question 4: Why are API keys used for many RESTful APIs? What purpose do they serve?
API keys are used for many RESTful APIS because it assigns a key to each unique person.  They serve the purpose of verifying the person who is trying to connect.   

AI Use: AI was used to search for the formatting of the API key url. 
