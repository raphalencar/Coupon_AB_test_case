# catalog
BRONZE_VOLUME_PATH = "/Volumes/ifood_cat/bronze/raw_files"
BRONZE_LAYER_PATH = "ifood_cat.bronze"
SILVER_LAYER_PATH = "ifood_cat.silver"
GOLD_LAYER_PATH = "ifood_cat.gold"

# URLs dos datasets
URLS = {
    "order.json.gz": "https://data-architect-test-source.s3-sa-east-1.amazonaws.com/order.json.gz",
    "consumer.csv.gz": "https://data-architect-test-source.s3-sa-east-1.amazonaws.com/consumer.csv.gz",
    "restaurant.csv.gz": "https://data-architect-test-source.s3-sa-east-1.amazonaws.com/restaurant.csv.gz",
    "ab_test_ref.tar.gz": "https://data-architect-test-source.s3-sa-east-1.amazonaws.com/ab_test_ref.tar.gz"
}

ORDER_COLUMN_COMMENTS = {
    "cpf": "Cadastro de Pessoa Física do usuário que realizou o pedido.",
    "customer_id": "Identificador único do usuário.",
    "customer_name": "Primeiro nome do usuário.",
    "delivery_address_city": "Cidade de entrega do pedido.",
    "delivery_address_country": "País da entrega do pedido.",
    "delivery_address_district": "Bairro da entrega do pedido.",
    "delivery_address_external_id": "Identificador único do endereço de entrega.",
    "delivery_address_latitude": "Latitude do endereço de entrega.",
    "delivery_address_longitude": "Longitude do endereço de entrega.",
    "delivery_address_state": "Estado da entrega do pedido.",
    "delivery_address_zip_code": "CEP da entrega.",
    "items": "Array com os itens que compõem o pedido.",
    "merchant_id": "Identificador único do restaurante.",
    "merchant_latitude": "Latitude do restaurante.",
    "merchant_longitude": "Longitude do restaurante.",
    "merchant_timezone": "Fuso horário em que o restaurante está localizado.",
    "order_created_at": "Data e hora em que o pedido foi criado no sistema.",
    "order_id": "Identificador único do pedido.",
    "order_scheduled": "Flag que indica se o pedido foi agendado para uma data/hora futura (True) ou é para entrega imediata (False).",
    "order_total_amount": "Valor total do pedido em Reais (BRL).",
    "origin_platform": "Sistema operacional do dispositivo do usuário no momento do pedido.",
    "order_scheduled_date": "Data e horário para entrega do pedido, caso seja agendado.",
    "partition_date": "Data de partição baseada em order_created_at."
}

ORDER_SILVER_COLUMN_COMMENTS = {
    "cpf": "Cadastro de Pessoa Física do usuário que realizou o pedido.",
    "customer_id": "Identificador único do usuário.",
    "customer_name": "Primeiro nome do usuário.",
    "delivery_address_city": "Cidade de entrega do pedido.",
    "delivery_address_country": "País da entrega do pedido.",
    "delivery_address_district": "Bairro da entrega do pedido.",
    "delivery_address_external_id": "Identificador único do endereço de entrega.",
    "delivery_address_state": "Estado da entrega do pedido.",
    "delivery_address_zip_code": "CEP da entrega.",
    "items": "Array com os itens que compõem o pedido.",
    "merchant_id": "Identificador único do restaurante.",
    "merchant_timezone": "Fuso horário em que o restaurante está localizado.",
    "order_created_at": "Data e hora em que o pedido foi criado no sistema.",
    "order_id": "Identificador único do pedido.",
    "order_scheduled": "Flag que indica se o pedido foi agendado para uma data/hora futura (True) ou é para entrega imediata (False).",
    "order_total_amount": "Valor total do pedido em Reais (BRL).",
    "origin_platform": "Sistema operacional do dispositivo do usuário no momento do pedido.",
    "items_parsed": "JSON com informações dos itens do pedido.",
    "total_items_quantity": "Quantidade total de itens em um pedido.",
    "total_items_value": "Soma do valor total de todos os itens do pedido.",
    "total_items_addition": "Soma do valor adicional de todos os itens do pedido.",
    "total_items_discount": "Soma do valor de desconto de todos os itens do pedido.",
    "num_distinct_items": "Número de itens distintos em um pedido.",
    "order_total_amount_capped": "Valor total do pedido após capping para valores maiores que o p95.",
    "partition_date": "Data de partição baseada em order_created_at."
}

CONSUMER_COLUMN_COMMENTS = {
    "customer_id": "Identificador único do usuário.",
    "language": "Idioma de preferência do usuário.",
    "created_at": "Data e hora em que o cadastro do usuário foi criado.",
    "active": "Flag que indica se o usuário está ativo ou inativo.",
    "customer_name": "Primeiro nome do usuário.",
    "customer_phone_area": "Código de área do telefone do usuário.",
    "customer_phone_number": "Número do telefone do usuário."
}

CONSUMER_SILVER_COLUMN_COMMENTS = {
    "customer_id": "Identificador único do usuário.",
    "active": "Flag que indica se o usuário está ativo ou inativo.",
    "days_since_signup": "Total de dias desde o cadastro do cliente até o inicio da campanha em 01/01/2019 (data do primeiro pedido)."
}

RESTAURANT_COLUMN_COMMENTS = {
    "id": "Identificador único do restaurante.",
    "created_at": "Data e hora em que o cadastro do restaurante foi criado.",
    "enabled": "Flag que indica se o restaurante está habilitado para receber pedidos no iFood ou não.",
    "price_range": "Classificação de preço do restaurante, em uma escala inteira.",
    "average_ticket": "Valor do ticket médio dos pedidos no restaurante.",
    "delivery_time": "Tempo padrão de entrega estimado para pedidos neste restaurante.",
    "minimum_order_value": "Valor mínimo do pedido para este restaurante.",
    "merchant_zip_code": "CEP do restaurante.",
    "merchant_city": "Cidade onde o restaurante está localizado.",
    "merchant_state": "Estado onde o restaurante está localizado.",
    "merchant_country": "País onde o restaurante está localizado."
}

RESTAURANT_SILVER_COLUMN_COMMENTS = {
    "merchant_id": "Identificador único do restaurante.",
    "price_range": "Classificação de preço do restaurante, em uma escala inteira.",
    "average_ticket": "Valor do ticket médio dos pedidos no restaurante.",
    "minimum_order_value": "Valor mínimo do pedido para este restaurante.",
    "merchant_city": "Cidade onde o restaurante está localizado.",
    "merchant_state": "Estado onde o restaurante está localizado.",
    "merchant_country": "País onde o restaurante está localizado.",
    "restaurant_profile": "Perfil do restaurante."
}

AB_TEST_REF_COLUMN_COMMENTS = {
    "customer_id": "Identificador único do usuário.",
    "is_target": "Grupo ao qual o usuário pertence ('target' ou'control')."
}

AB_TEST_REF_SILVER_COLUMN_COMMENTS = {
    "customer_id": "Identificador único do usuário.",
    "is_target": "Se pertence ao grupo alvo ou não. True para target e False para controle"
}

ABT_SILVER_COLUMN_COMMENTS = {
    "cpf": "Cadastro de Pessoa Física do usuário que realizou o pedido.",
    "customer_id": "Identificador único do usuário.",
    "customer_name": "Primeiro nome do usuário.",
    "delivery_address_city": "Cidade de entrega do pedido.",
    "delivery_address_country": "País da entrega do pedido.",
    "delivery_address_district": "Bairro da entrega do pedido.",
    "delivery_address_external_id": "Identificador único do endereço de entrega.",
    "delivery_address_state": "Estado da entrega do pedido.",
    "delivery_address_zip_code": "CEP da entrega.",
    "items": "Array com os itens que compõem o pedido.",
    "merchant_id": "Identificador único do restaurante.",
    "merchant_timezone": "Fuso horário em que o restaurante está localizado.",
    "order_created_at": "Data e hora em que o pedido foi criado no sistema.",
    "order_id": "Identificador único do pedido.",
    "order_scheduled": "Flag que indica se o pedido foi agendado para uma data/hora futura (True) ou é para entrega imediata (False).",
    "order_total_amount": "Valor total do pedido em Reais (BRL).",
    "origin_platform": "Sistema operacional do dispositivo do usuário no momento do pedido.",
    "items_parsed": "JSON com informações dos itens do pedido.",
    "total_items_quantity": "Quantidade total de itens em um pedido.",
    "total_items_value": "Soma do valor total de todos os itens do pedido.",
    "total_items_addition": "Soma do valor adicional de todos os itens do pedido.",
    "total_items_discount": "Soma do valor de desconto de todos os itens do pedido.",
    "num_distinct_items": "Número de itens distintos em um pedido.",
    "order_total_amount_capped": "Valor total do pedido após capping para valores maiores que o p95.",
    "partition_date": "Data de partição baseada em order_created_at.",
    "is_target": "Se pertence ao grupo alvo ou não. True para target e False para controle",
    "active": "Flag que indica se o usuário está ativo ou inativo.",
    "days_since_signup": "Total de dias desde o cadastro do cliente até o inicio da campanha em 01/01/2019 (data do primeiro pedido).",
    "price_range": "Classificação de preço do restaurante, em uma escala inteira.",
    "average_ticket": "Valor do ticket médio dos pedidos no restaurante.",
    "minimum_order_value": "Valor mínimo do pedido para este restaurante.",
    "merchant_city": "Cidade onde o restaurante está localizado.",
    "merchant_state": "Estado onde o restaurante está localizado.",
    "merchant_country": "País onde o restaurante está localizado.",
    "restaurant_profile": "Perfil do restaurante."
}
