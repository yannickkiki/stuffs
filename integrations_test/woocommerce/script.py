from woocommerce import API

wcapi = API(
    url="http://yan-k.safary.xyz/",  # Your store URL
    consumer_key="xxx",  # Your consumer key
    consumer_secret="xxx",  # Your consumer secret
    wp_api=True,  # Enable the WP REST API integration
    version="wc/v3"  # WooCommerce WP REST API version
)

reviews = wcapi.get("products/reviews").json()
products = wcapi.get("products").json()
webhooks = wcapi.get("webhooks").json()

data2 = {
    "name": "Order updated",
    "topic": "ordera.updated",
    "delivery_url": "http://localhost:8000/webhooks/order.updated"
}

data3 = {
    "name": "Review created",
    "topic": "review.created",
    "delivery_url": "http://localhost:8000/webhooks/review.created"
}

data = data3
result3 = wcapi.post("webhooks", data).json()
