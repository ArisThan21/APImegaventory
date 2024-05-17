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
 


if __name__ == "__main__":
    try:
        Product = Megaventoryproduct("6945f581fc8e7cef@m150627")
        Product1 = Megaventoryproduct("6945f581fc8e7cef@m150627")
        Client = MegaventoryClient("6945f581fc8e7cef@m150627")
        Client1 = MegaventoryClient("6945f581fc8e7cef@m150627")
        Inventory = MegaventoryInventory("6945f581fc8e7cef@m150627")
        Purchase = MegaventoryPurchase("6945f581fc8e7cef@m150627")
        Quantity = MegaventoryQuantity("6945f581fc8e7cef@m150627")
        Quantity1 = MegaventoryQuantity("6945f581fc8e7cef@m150627")
        Sales = MegaventorySales("6945f581fc8e7cef@m150627")


        

        product_data = Product.create_product("111", " Puma sneakers2", "Category A", "Gram(s)", "Dummy Supplier A", 79.99, 35.99)
        product_data1 = Product1.create_product("2299", "New Balance sneakers","Category A", "Gram(s)", "Dummy Supplier A", 89.99, 39.99)
        time.sleep(2)
        client = Client.createClient("Michalis", " Mihalis@exampletest.com", "Example 5, Athens", "9876543210","Shipping1","EUR")
        supplier = Client1.createClient("Helen", "helen@exampletest.com", " Example 6, Athens", " 9876543233","Shipping1","EUR")
        time.sleep(2)
        inventory = Inventory.createInventory("Logi", "Logi Project Location", " Example 28, Athens")
        time.sleep(2)
        purchase = Purchase.createPurchase("111", "Puma sneakers2","something","EUR","5", 20)
        time.sleep(2)
        sales = Sales.createSales("6","111","Puma sneakers","EUR","5", 15)
        time.sleep(2)
        quantity = Quantity.UpdateQuantity("111", 15, 5)
        quantity1 = Quantity1.UpdateQuantity("1112299", 30, 5)
    



        print(Product.send_data(product_data, Product.url_product))
        print(Product1.send_data(product_data1, Product1.url_product))

        print(client.send_data(client, Client.url_supplier_client))
        print(supplier.send_data(supplier, Client.url_supplier_client))

        print(Inventory.send_data(inventory, Inventory.url_inventory))

        print(Purchase.send_data(purchase, Purchase.url_order))
        print(Sales.send_data(sales,Sales.url_Sales))
        print(quantity.send_data(quantity, Quantity.url_Quantity))
        print(quantity1.send_data(quantity1, Quantity1.url_Quantity))

    except Exception as e:
       print(e)
