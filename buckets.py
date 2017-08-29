class Bucketlists(object):
    
    def __init__(self):
        self.Buckets = {'Anto':{'bName':'Anto', 'owner':'admin@gmail.com', 'description':'My goals between...'}}
        self.items = {'Anto':{'items':['Driving','Skating']}}
    
    def create_bucket(self, bName, owner, bDescription):
        if bName not in self.Buckets.keys():
            self.Buckets[bName] = {'bName': bName, 'owner': owner, 'description': bDescription}
            return "Bucket created Successfully"
        else:
            return "BucketName already Exists"            

    def delete_bucket(self, bName):
        if bName in self.Buckets.keys():
            for bucket in self.Buckets.keys():
                if bucket==bName:
                    self.Buckets.pop(bucket)
                    return 'Bucket Successfully Deleted'
        else:
            return "Bucket does not Exist"

    def edit_bucket(self, owner, bName, NewbName, description):
        if bName in self.Buckets.keys():
            for bucket in self.Buckets.keys():	
                if bucket==bName:
                    self.Buckets.pop(bucket)
                    self.Buckets[NewbName] = {'bName': NewbName, 'owner': owner, 'description': description}
                    return "Bucket Successfully Edited"
        return "Bucket Does not Exist"
		
    def get_buckets(self):
        return self.Buckets

    def add_item(self, bName, item):
        if bName in self.items.keys():
            for items_dict in self.items.keys():
                if items_dict == bName:
                    self.items[bName]['items'].append(item)
                    return "The item added Successfully"
        self.items[bName] = {'items':[]}
        self.items[bName]['items'].append(item)
        return "The item added Successfully"
	
    def delete_item(self, bName, item):
        if bName in self.Buckets.keys():
            for items_dict in self.items:
                if items_dict['bName']==bName:
                    if item not in items_dict['items']:
                    	return 'The Item Does not Exist'
                    else:
                        for index, value in enumerate(items_dict['items']):
                            if value == item:
                                items_dict['items'].pop(index)
                                return "The item Deleted Successfully"
        return "The Bucket does not Exist"
	
    def edit_item(self, bName, oldItem, newItem):
        if bName in self.Buckets.keys():
            for items_dict in self.items:
                if items_dict['bName']==bName:
                    if oldItem not in items_dict['items']:
                        return "The old item does not Exist"
                    else:
                        for index, value in enumerate(items_dict['items']):
                            if value == oldItem:
                                items_dict['items'][index] = newItem
                                return "The item Edited Successfully"
        return "The Bucket Does not Exist"
    
    def get_items(self):
        return self.items











