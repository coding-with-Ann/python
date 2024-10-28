import requests

def get_product_by_id(id):
    url = 'https://api.freeapi.app/api/v1/public/randomproducts/'
    url = url + id
    response = requests.get(url)
    data = response.json()
    print(type(data))
    print('\n')

    if data['statusCode'] == 200 and 'data' in data:
        product_name = data['data']['title']
        return product_name

    raise Exception('failed to fetch product')


def main():
    try:
        id = input('Enter product id: ')
        product_name = get_product_by_id(id)
        print(product_name)
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    main()




# With break, the loop will exit when the product is found, but the function will continue executing any code after the loop.
#  In this case, there is no code after the loop, so it will work similarly to return. However, if you add more code after the loop, 
#  it will execute that code, which might not be what you want.