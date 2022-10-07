from azure.cosmos import exceptions, CosmosClient, PartitionKey
import uuid

def update_db(Account,Password,Nonce,Userid,token):
    # 進去cosmes 要是字典格式
    finish_concat = {"id":str(uuid.uuid4()),"Account":Account,"Password":Password,"Nonce":Nonce,"Userid":Userid,"token":token}

    endpoint = "https://XXXXXXX"
    key = 'XXXXXX'

    # <create_cosmos_client>
    client = CosmosClient(endpoint, key)
    # </create_cosmos_client>

    # Create a database
    # <create_database_if_not_exists>
    database_name = 'Linebot_Cosmes'
    database = client.create_database_if_not_exists(id=database_name)
    # </create_database_if_not_exists>

    # Create a container
    # Using a good partition key improves the performance of database operations.
    # <create_container_if_not_exists>
    container_name = 'Account_link'
    container = database.create_container_if_not_exists(
        id=container_name,
        partition_key=PartitionKey(path="/Userid"),
    offer_throughput=400)

    container.create_item(body=finish_concat)

