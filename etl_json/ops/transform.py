from dagster import op

@op
def transform_data(data):
   
    transformed_data = []
    for item in data:
        transformed_item = {
            "id": item["id"],
            "name": item["name"].upper(),  
            "age": item["age"],
            "age_category": "Adult" if item["age"] >= 18 else "Minor"
        }
        transformed_data.append(transformed_item)
    
    return transformed_data
