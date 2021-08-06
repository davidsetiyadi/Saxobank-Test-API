# importing the requests library
import requests
import json
  
# api-endpoint
URL = "localhost:9665"
TOKEN = "eyJhbGciOiJFUzI1NiIsIng1dCI6IjhGQzE5Qjc0MzFCNjNFNTVCNjc0M0QwQTc5MjMzNjZCREZGOEI4NTAifQ.eyJvYWEiOiI3Nzc3NSIsImlzcyI6Im9hIiwiYWlkIjoiMTA5IiwidWlkIjoifEVzc3BSekVRbkNVcGd4SHl4cTktUT09IiwiY2lkIjoifEVzc3BSekVRbkNVcGd4SHl4cTktUT09IiwiaXNhIjoiRmFsc2UiLCJ0aWQiOiIyMDAyIiwic2lkIjoiZDU3Mjg5MzJkN2E0NDc4NGI4OTczMmQzZjUwZWEwZDMiLCJkZ2kiOiI4NCIsImV4cCI6IjE2MjgyMzc2MjIiLCJvYWwiOiIxRiJ9.2k_OOrcBZmfgvxavU_Wy1lsOX_fqr2PjHayZ00BYFkv5FlCaAM6hk8TXEpokZR49FQsBSOJr3xdERdtoLnMXyA"
# location given here
#location = "delhi technological university"
#token=   
# defining a params dict for the parameters to be sent to the API
#PARAMS = {'address':location}
URL2= "https://gateway.saxobank.com/sim/openapi/port/v1/users/me" #USER INFORMATION
URL3= "https://gateway.saxobank.com/sim/openapi/cm/v1/signups/status/" #CLINT STATUS
URL4= "https://gateway.saxobank.com/sim/openapi/cm/v1/signups/options" #oPTION fIELDS
param_client = {'ClientKey':'|EsspRzEQnCUpgxHyxq9-Q=='}
# sending get request and saving the response as response object
#r = requests.get(url = URL, params = PARAMS)
client_key = "|EsspRzEQnCUpgxHyxq9-Q=="
response = requests.get(URL2,headers={'Authorization': 'Bearer ' + TOKEN})

response2 = requests.get(URL3+client_key,headers={'Authorization': 'Bearer ' + TOKEN})
response3 = requests.get(URL4,headers={'Authorization': 'Bearer ' + TOKEN})
# extracting data in json format

data = response.json()
print ('User Status::',data)
print ('___\n')
datas = response2.json()
print ('SignUP Status::',datas)
print ('___\n')
#
datas2 = response3.json()
with open('convert.txt', 'w') as convert_file:
     convert_file.write(json.dumps(datas2))

# for dat in datas2['Data']:
#       print ('Name::',dat['PropertyName'])
#       for x in dat['ValuePairs']:
#             print ('Value::',x)
json = {
      "PersonalInformation": {
            "ContactInformation": {
        "EmailAddress": "abc@test.com",
        "PrimaryPhoneNumber": {
        "CountryCode": "US",
        "Number": "1234567890"
      }}
            ,
            "FirstName": "Sahrul",
            "LastName": "MVP",
            "ResidentialAddress": {
      "BuildingName": "Building Penhurst Park",
      "BuildingNumber": "Build# 34",
      "City": "Buffalo",
      "CountryOfResidenceCode": "US",
      "PostalCode": "14202",
      "State": "New York",
      "StreetName": "Niagara Square"
    },
            "ServiceLanguageCode": "ID"
      },
      "RegulatoryInformation": {
    "FatcaDeclaration": {
      "UnitedStatesCitizen": True,
      "UnitedStatesProducts": True,
      "UnitedStatesTaxId": "23456",
      "UnitedStatesTaxLiable": True
    }
  }
}
respnse = {
  "ClientId": "123456",
  "ClientKey": "5nvwODYxv55paw8HIpS2Uw==",
  "SignUpId": "f115f81f-f23d-4fcc-8cd0-5109b853fcfe"
}
{
  "ClientId": "123456",
  "ClientKey": "5nvwODYxv55paw8HIpS2Uw==",
  "SignUpId": "a67d98c7-5fe5-474c-9c06-b5bccd0882da"
}
"""
SignupFlowDocumentType
Document types accepted for signup

Name  Description
AccountViewToIb   Document detailing Introducing-Broker/Client details, authorization from client and Broker commission details
EsaContract Document detialing ESA Contract
FeePaymentAuthorization Document detailing Fee Payment Authorization
GeneralBusinessTerms    Document explaining general business terms
PensionTransferRequest  Document detailing Pension Transfer Request
PowerOfAttorney   Legal document mentioning the details of the acts that can be done on behalf of the principal (client)
PowerOfAttorneyToIb     Legal document mentioning the details of the acts that an IB can undertake on behalf of the principal (client)
ProofOfIdentity   Document to verify the identity of client
ProofOfResidency  Document to verify the residency of client
SourceOfFundsDocument   Document detailing all the sources which client have for generating funds
TermsAndConditions      Document explaining terms and conditions
TermsAndConditionsAldersopsparingPrivate  Document detailing Terms and Conditions Aldersopsparing Private
TermsAndConditionsKapitalPensionPrivate   Document detailing Terms and Conditions Kapital Pension Private
TermsAndConditionsRatePensionPrivate      Document detailing Terms and Conditions Rate Pension Private
"""
#AUTOWEALTH ONBOARDING 
#https://www.developer.saxo/openapi/referencedocs/cm/v1/signups
#Flow SAXO’s onboarding process
"""
Get all signup options
Return data set containing possible field values for each user selections.
1.  https://gateway.saxobank.com/sim/openapi/cm/v1/signups/options

2. Creates a new client
 https://gateway.saxobank.com/sim/openapi/cm/v1/signups/?OwnerKey={OwnerKey}
 {
  "ClientId": "123456",
  "ClientKey": "5nvwODYxv55paw8HIpS2Uw==",
  "SignUpId": "a67d98c7-5fe5-474c-9c06-b5bccd0882da"
}
3. Adds a file to a sign up case
https://gateway.saxobank.com/sim/openapi/cm/v1/signups/attachments/{SignUpId}/?RenewalDate={RenewalDate}&DocumentType={DocumentType}&Title={Title}

4. Completes the onboarding application
 https://gateway.saxobank.com/sim/openapi/cm/v1/signups/completeapplication/{SignUpId}/?AwaitAccountCreation={AwaitAccountCreation}

5. Initiate verification process from external vendor
Initiates the verification process for a client by returning a URL that will redirect the client to an external vendor. If successful, the onboarding status will be approved.
 https://gateway.saxobank.com/sim/openapi/cm/v1/signups/verification/initiate/{ClientKey}

"""
params_ownerkey = {'OwnerKey':'|EsspRzEQnCUpgxHyxq9-Q=='}
URL_SIGNUP = "https://gateway.saxobank.com/sim/openapi/cm/v1/signups/"
response_signup = requests.post(URL_SIGNUP,headers={'Authorization': 'Bearer ' + TOKEN},params=params_ownerkey,json=json)
print ('Response_signup:::',response_signup,response_signup.json())
print ('___\n')
#sign UP attachment
URL_ATTACHMENT = "https://gateway.saxobank.com/sim/openapi/cm/v1/signups/attachments/701ef352-7784-4841-8d07-0eda82d197b2/"
params_attachment ={
      'RenewalDate': '2021-01-01',
      'DocumentType': 'AccountViewToIb',
      'Title'     : 'Text'
}
files = {
'document': open('convert.txt', 'rb')
}
response_att = requests.post(URL_ATTACHMENT,headers={'Authorization': 'Bearer ' + TOKEN},params=params_attachment,files=files)
print ('Response Attachment::',response_att)

