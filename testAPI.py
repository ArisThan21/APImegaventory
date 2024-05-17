import requests
import time
class Megaventoryproduct:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url_product = 'https://api.megaventory.com/v2017a/Product/ProductUpdate'
        self.requests = requests

    def send_data(self, data, url):
        headers = {'Content-Type': 'application/json'}
        data['APIKEY'] = self.api_key
        response = self.requests.post(url, json=data, headers=headers)
        return response.json()

    def create_product(self, sku, description, category, Weight, Supplier, Sprice, Pprice):
        data = {
            "APIKEY": "6945f581fc8e7cef@m150627",
            "mvProduct": {
                "ProductSKU": sku,
                "ProductDescription": description,
                "mvProductCategory": {
                    "ProductCategoryName": category,
                },
                "ProductSellingPrice": Sprice,
                "ProductPurchasePrice": Pprice,
                "mvProductWeightUnit": {
                    "WeightUnitName": Weight,
                },
                "mvProductMainSupplier": {
                    "SupplierClientName": Supplier,
                },
            },
         }
        return data
    
class MegaventoryClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url_supplier_client ='https://api.megaventory.com/v2017a/SupplierClient/SupplierClientUpdate'
        self.requests = requests
    
    def send_data(self, data, url):
        headers = {'Content-Type': 'application/json'}
        data['APIKEY'] = self.api_key
        response = self.requests.post(url, json=data, headers=headers)
        return response.json()
    
    def createClient(self, name, email, address, phone, AddressType, Currency):
        data = {
         "APIKEY": "6945f581fc8e7cef@m150627",
         "mvSupplierClient": {
            "SupplierClientName": name,
            "SupplierClientAddresses": [
                {
                    "AddressType": AddressType,
                    "AddressLine1": address,
                    "Name": "string",
                    "Phone": phone,
                    "Email": email,
                }
            ],
            "SupplierClientCurrency": Currency,
        },
        }
        return data

class MegaventoryInventory:
    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.url_inventory ='https://api.megaventory.com/v2017a/InventoryLocation/InventoryLocationUpdate'
        self.requests = requests
    
    def send_data(self, data, url):
        headers = {'Content-Type': 'application/json'}
        data['APIKEY'] = self.apiKey
        response = self.requests.post(url, json=data, headers=headers)
        return response.json()
    
    def createInventory(self, Abbreviation,Name,Address):
       data = {
        "APIKEY": "6945f581fc8e7cef@m150627",
        "mvInventoryLocation": {
            "InventoryLocationName": Name,
            "InventoryLocationAbbreviation": Abbreviation,
            "Address": {
                "AddressLine1": Address,
                "Name": Name,
            },
        },
    }
       return data

class MegaventoryPurchase:
    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.url_order ='https://api.megaventory.com/v2017a/PurchaseOrder/PurchaseOrderUpdate'
        self.requests = requests
    
    def send_data(self, data, url):
        headers = {'Content-Type': 'application/json'}
        data['APIKEY'] = self.apiKey
        response = self.requests.post(url, json=data, headers=headers)
        return response.json()
    
    def createPurchase(self, sku, Description, Address,Currency,InventoryLocationID,RowQuantity):
      data = {
        "APIKEY": "6945f581fc8e7cef@m150627",
        "mvPurchaseOrder": {
            "PurchaseOrderNo": sku,
            "PurchaseOrderCurrencyCode": Currency,
            "PurchaseOrderSupplierName": "string",
            "PurchaseOrderTypeDescription": Description,
            "PurchaseOrderAddresses": [
                {
                    "AddressType": "Billing",
                    "AddressLine1": Address,
                }
            ],
            "PurchaseOrderInventoryLocationID": InventoryLocationID,
            "PurchaseOrderDetails": [
                {
                    "PurchaseOrderRowProductSKU": sku,
                    "PurchaseOrderRowQuantity": RowQuantity,
                }
            ],
            "PurchaseOrderStatus": "Pending",
        },
    }
      return data
    

class MegaventorySales:
    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.url_Sales ='https://api.megaventory.com/v2017a/PurchaseOrder/PurchaseOrderUpdate'
        self.requests = requests
    
    def send_data(self, data, url):
        headers = {'Content-Type': 'application/json'}
        data['APIKEY'] = self.apiKey
        response = self.requests.post(url, json=data, headers=headers)
        return response.json()
    
    def createSales(self,number, sku, name, currency, inventoryLocationID, quantity):
      data = {
        "APIKEY": "6945f581fc8e7cef@m150627",
        "mvSalesOrder":{
            "SalesOrderTypeDescription": name,
            "SalesOrderCurrencyCode": currency,
            "SalesOrderAddresses": [
                {
                    "AddressType": "Billing",
                }
            ],
            "SalesOrderInventoryLocationID": inventoryLocationID,
            "SalesOrderDetails": [
                {
                    "SalesOrderRowProductSKU": sku,
                    "SalesOrderRowQuantity": quantity,
                }
            ],
            "SalesOrderStatus": "Verified",
        },
      }
      return data


class MegaventoryQuantity:
    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.url_Quantity ='https://api.megaventory.com/v2017a/InventoryLocationStock/ProductStockUpdate'
        self.requests = requests
    
    def send_data(self, data, url):
        headers = {'Content-Type': 'application/json'}
        data['APIKEY'] = self.apiKey
        response = self.requests.post(url, json=data, headers=headers)
        return response.json()
    
    def UpdateQuantity(self, sku, ProductQuantity, InventoryLocationID):
       data = {
        "APIKEY": "6945f581fc8e7cef@m150627",
        "mvProductStockUpdateList": [
            {
                "ProductSKU": sku,
                "ProductQuantity": ProductQuantity,
                "InventoryLocationID": InventoryLocationID
            }
        ]
       }
       return data
 


try:
    megaventoryProduct = Megaventoryproduct("6945f581fc8e7cef@m150627")
    #megaventoryProduct1 = Megaventoryproduct("6945f581fc8e7cef@m150627")
    Megaventoryclient = MegaventoryClient("6945f581fc8e7cef@m150627")
    #Megaventoryclient1 = MegaventoryClient("6945f581fc8e7cef@m150627")
    Megaventoryinventory = MegaventoryInventory("6945f581fc8e7cef@m150627")
    megaventoryPurchase = MegaventoryPurchase("6945f581fc8e7cef@m150627")
    Megaventoryquantity = MegaventoryQuantity("6945f581fc8e7cef@m150627")
    #Megaventoryquantity1 = MegaventoryQuantity("6945f581fc8e7cef@m150627")
    Megaventorysales = MegaventorySales("6945f581fc8e7cef@m150627")

    product_data = megaventoryProduct.create_product("111", " Puma sneakers2", "Category A", "Gram(s)", "Dummy Supplier A", 79.99, 35.99)
    #product_data1 = megaventoryProduct1.create_product("2299", "New Balance sneakers","Category A", "Gram(s)", "Dummy Supplier A", 89.99, 39.99)
    time.sleep(2)
    client = Megaventoryclient.createClient("Michalis", " Mihalis@exampletest.com", "Example 5, Athens", "9876543210","Shipping1","EUR")
    #supplier = Megaventoryclient1.createClient("Helen", "helen@exampletest.com", " Example 6, Athens", " 9876543233","Shipping1","EUR")
    time.sleep(2)
    inventory = Megaventoryinventory.createInventory("Logi", "Logi Project Location", " Example 28, Athens")
    time.sleep(2)
    #purchase = megaventoryPurchase.createPurchase("111", "Puma sneakers2","something","EUR","5", 20)
    time.sleep(2)
    sales = Megaventorysales.createSales("6","111","Puma sneakers","EUR","5", 15)
    time.sleep(2)
    #quantity = Megaventoryquantity.UpdateQuantity("111", 15, 5)
    #quantity1 = Megaventoryquantity1.UpdateQuantity("1112299", 30, 5)
    



    print(megaventoryProduct.send_data(product_data, megaventoryProduct.url_product))
    #print(megaventoryProduct1.send_data(product_data1, megaventoryProduct1.url_product))

    print(Megaventoryclient.send_data(client, Megaventoryclient.url_supplier_client))
    #print(Megaventoryclient1.send_data(supplier, Megaventoryclient.url_supplier_client))

    print(Megaventoryinventory.send_data(inventory, Megaventoryinventory.url_inventory))

    #print(megaventoryPurchase.send_data(purchase, megaventoryPurchase.url_order))
    print(Megaventorysales.send_data(sales,Megaventorysales.url_Sales))
    #print(Megaventoryquantity.send_data(quantity, Megaventoryquantity.url_Quantity))
    #print(Megaventoryquantity1.send_data(quantity1, Megaventoryquantity1.url_Quantity))

except Exception as e:
    print(e)
