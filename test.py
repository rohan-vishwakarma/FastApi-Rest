import pandas as pd

# Define the route data as a list of dictionaries
route_data = [
    {"HTTP Method": "GET", "URL Endpoint": "/test", "Controller Name": "ComplaintController", "Controller Method": "index"},
    {"HTTP Method": "GET", "URL Endpoint": "/login", "Controller Name": "AuthController", "Controller Method": "login"},
    {"HTTP Method": "POST", "URL Endpoint": "/online-payment-received", "Controller Name": "OnlinePaymentController", "Controller Method": "onlinePaymentReceived"},
    {"HTTP Method": "POST", "URL Endpoint": "/online-payment-initialize", "Controller Name": "OnlinePaymentController", "Controller Method": "onlinePaymentInitialize"},
    {"HTTP Method": "POST", "URL Endpoint": "/debitnote-online-payment-initialize", "Controller Name": "OnlinePaymentController", "Controller Method": "onlineDebitNotePaymentInitialize"},
    {"HTTP Method": "POST", "URL Endpoint": "/debitnote-online-payment-received", "Controller Name": "OnlinePaymentController", "Controller Method": "onlineDebitNotePaymentReceived"},
    {"HTTP Method": "POST", "URL Endpoint": "/facilities-online-payment-link", "Controller Name": "FacilitiesController", "Controller Method": "onlineFacilitiesPaymentLink"},
    {"HTTP Method": "POST", "URL Endpoint": "/facilities-online-payment-initialize", "Controller Name": "OnlinePaymentController", "Controller Method": "onlineFacilitiesPaymentInitialize"},
    {"HTTP Method": "POST", "URL Endpoint": "/facilities-online-payment-received", "Controller Name": "OnlinePaymentController", "Controller Method": "onlineFacilitiesPaymentReceived"},
    {"HTTP Method": "POST", "URL Endpoint": "/payment-report", "Controller Name": "OnlinePaymentController", "Controller Method": "pgReportSend"},
    {"HTTP Method": "ANY", "URL Endpoint": "singleInvoice", "Controller Name": "BillingController", "Controller Method": "singleInvoice"},
    {"HTTP Method": "ANY", "URL Endpoint": "single-debit-note", "Controller Name": "DebitNoteController", "Controller Method": "getSingleDebitNote"},
    {"HTTP Method": "POST", "URL Endpoint": "/web-hook-payment-received", "Controller Name": "WebHookOnlinePaymentController", "Controller Method": "webHookPaymentReceived"},
    {"HTTP Method": "POST", "URL Endpoint": "/web-hook-deit-note-received", "Controller Name": "WebHookOnlinePaymentController", "Controller Method": "webHookDebitNotePaymentReceived"},
    {"HTTP Method": "POST", "URL Endpoint": "/web-hook-facilities-received", "Controller Name": "WebHookOnlinePaymentController", "Controller Method": "webHookFacilitiesPaymentReceived"},
    {"HTTP Method": "ANY", "URL Endpoint": "/removeMobileNumber", "Controller Name": "DeleteIdDataController", "Controller Method": "removeMobileNumber"},
    {"HTTP Method": "ANY", "URL Endpoint": "/removeEmail", "Controller Name": "DeleteIdDataController", "Controller Method": "removeEmail"},
    {"HTTP Method": "POST", "URL Endpoint": "/sendgrid/email-webhook", "Controller Name": "SendgridEmailWebHookController", "Controller Method": "sendgridEmailHandleWebhook"}
]

df = pd.DataFrame(route_data)
# Save it as an Excel
file_path = "route_data.xlsx"
df.to_excel(file_path, index=False)

file_path
