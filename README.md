# AFEX Backend Developer Coding Assessment

### Your Task

1. Get this app to work
2. Change the database config to use PostgreSQL
3. Config settings for dev, staging and production servers
4. Add Two(2) security updates to the settings file
5. Add Two(1) performance updates to the settings file

A Django app has been created under `/apps/` called `crm`

1. Configure this app to work with the main project
2. Two models has been created for you: "Client" and "ClientWallet":
   a. Write a CRUD option with the Client Model
   b. Write a PUT/POST option for the Client Wallet model (i.e ability to fund a particular client's wallet)
   c. Write/Configure API endpoints to fetch client (including their wallet balance)
   N:B You are to design an appropriate frontend for task in a & b above
3. Assuming you have been asked to tweak the code such that a client can have wallets in multiple currency, how will you
   approach this.

   - To achieve this if there are few currency, we can just add a field to hold the value for each currency 
   - But in the case where there are more currency, we can create a model for each currency hence the client will have a one to one field to 
   each currecy model.

\*\*\* Optional

1. Configure Docker for this project