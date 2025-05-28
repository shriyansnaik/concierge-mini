**Question:** 
```
book me a cab to swiggy office banglore from banglore airport. i need an SUV
```

**Response:** 
```
{
  "key_entities": {
    "destination": "swiggy office banglore",
    "price_range": "",
    "pickup_location": "banglore airport",
    "cab_type": "SUV"
  },
  "intent": "cab_request",
  "intent_confidence": 0.95,
  "follow_up_questions": [
    "What price range are you looking for?"
  ]
}
```

**Question:** 
```
my moms birthday is coming up. i want to buy her a watch
```

**Response:** 
```
{
  "key_entities": {
    "budget": "",
    "occasion": "birthday",
    "gift": "watch",
    "recipient": "mom"
  },
  "intent": "gifting",
  "intent_confidence": 0.95,
  "follow_up_questions": [
    "What is your budget for the watch?"
  ]
}
```

**Question:** 
```
Need a sunset-view table for two tonight; gluten-free menu a must
```

**Response:** 
```
{
  "key_entities": {
    "number_of_members": "two",
    "date": "tonight",
    "time": "",
    "location": "",
    "cuisine": "gluten-free",
    "view": "sunset-view"
  },
  "intent": "dining",
  "intent_confidence": 0.95,
  "follow_up_questions": [
    "What time would you like to book the table for?",
    "In what location are you looking for a table?"
  ]
}
```

**Question:** 
```
i want to update my aadhar address
```

**Response:** 
```
[
  {
    "title": "Aadhaar Update Service - Unique Identification Authority of India",
    "href": "https://uidai.gov.in/en/my-aadhaar/update-aadhaar.html",
    "body": "Learn how to update your address and other documents in your Aadhaar database online or at an enrolment center. Check the status of your update request and view your Aadhaar update history."
  },
  {
    "title": "How To Change Address In Aadhaar Card Online? - ClearTax",
    "href": "https://cleartax.in/s/aadhar-card-address-change-online",
    "body": "Given below is the online address update process for your Aadhar card: Step 1: Login to myAadhaar portal by entering your Aadhaar number, captcha code and OTP. Step 2: After logging in, select the option 'Address Update' tab. Step 3: On the next tab, click on 'Update Aadhaar Online' tab."
  },
  {
    "title": "Aadhar Card Update Online: Mobile, Address, DOB, Name Correction",
    "href": "https://uidai-aadharcard.com/aadhar-card-update/",
    "body": "Learn how to update your Aadhar Card details online, such as address, name, DOB, gender, email, and mobile number. You need a registered mobile number and a scanned proof of address document to update your address online."
  },
  {
    "title": "Apply online for Aadhaar Card data update/correction",
    "href": "https://services.india.gov.in/service/detail/apply-online-for-aadhaar-card-data-updatecorrection-1",
    "body": "Learn how to update or correct your Aadhaar Card data online through the UIDAI website. You can also find FAQs, book appointment, download e-Aadhaar and search for enrolment centres."
  },
  {
    "title": "Aadhaar Card update for free online: Step-by-step guide to ... - Digit",
    "href": "https://www.digit.in/how-to/general/aadhaar-card-update-for-free-online-step-by-step-guide-to-change-address-name-and-more.html",
    "body": "Aadhaar update: Details that can be updated online. Users can only update selected demographic details online for free. They can update their name, date of birth (under certain limits), address ..."
  }
]
```

