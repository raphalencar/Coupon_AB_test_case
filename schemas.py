from pyspark.sql.types import (
    ArrayType,
    StructType, 
    StructField, 
    StringType, 
    IntegerType, 
    FloatType, 
    LongType, 
    DoubleType,
    TimestampType, 
    BooleanType
)

ORDER_SCHEMA = StructType([
    StructField("cpf", StringType(), True), 
    StructField("customer_id", StringType(), True), 
    StructField("customer_name", StringType(), True), 
    StructField("delivery_address_city", StringType(), True), 
    StructField("delivery_address_country", StringType(), True), 
    StructField("delivery_address_district", StringType(), True), 
    StructField("delivery_address_external_id", StringType(), True), 
    StructField("delivery_address_latitude", FloatType(), True), 
    StructField("delivery_address_longitude", FloatType(), True), 
    StructField("delivery_address_state", StringType(), True), 
    StructField("delivery_address_zip_code", StringType(), True), 
    StructField("items", StringType(), True),
    StructField("merchant_id", StringType(), True), 
    StructField("merchant_latitude", FloatType(), True), 
    StructField("merchant_longitude", FloatType(), True), 
    StructField("merchant_timezone", StringType(), True), 
    StructField("order_created_at", TimestampType(), True), 
    StructField("order_id", StringType(), True), 
    StructField("order_scheduled", BooleanType(), True), 
    StructField("order_total_amount", DoubleType(), True), 
    StructField("origin_platform", StringType(), True), 
    StructField("order_scheduled_date", TimestampType(), True) 
])

CURRENCY_VALUE_SCHEMA = StructType([
    StructField("currency", StringType(), True),
    StructField("value", StringType(), True)
])

GARNISH_ITEM_SCHEMA = StructType([
        StructField("name", StringType(), True),
        StructField("quantity", StringType(), True),
        StructField("totalValue", CURRENCY_VALUE_SCHEMA, True)
])

ITEM_SCHEMA = StructType([
    StructField("name", StringType(), True),
    StructField("quantity", StringType(), True),
    StructField("garnishItems", ArrayType(GARNISH_ITEM_SCHEMA), True),
    StructField("totalValue", CURRENCY_VALUE_SCHEMA, True),
    StructField("totalAddition", CURRENCY_VALUE_SCHEMA, True),
    StructField("totalDiscount", CURRENCY_VALUE_SCHEMA, True)
])

CONSUMER_SCHEMA = StructType([
    StructField("customer_id", StringType(), True), 
    StructField("language", StringType(), True),  
    StructField("created_at", TimestampType(), True),  
    StructField("active", BooleanType(), True),  
    StructField("customer_name", StringType(), True),  
    StructField("customer_phone_area", StringType(), True),  
    StructField("customer_phone_number", StringType(), True)
])

RESTAURANT_SCHEMA = StructType([
    StructField("id", StringType(), True),
    StructField("created_at", TimestampType(), True),
    StructField("enabled", BooleanType(), True),
    StructField("price_range", IntegerType(), True),
    StructField("average_ticket", DoubleType(), True),
    StructField("delivery_time", FloatType(), True),
    StructField("minimum_order_value", DoubleType(), True),
    StructField("merchant_zip_code", StringType(), True),
    StructField("merchant_city", StringType(), True),
    StructField("merchant_state", StringType(), True),
    StructField("merchant_country", StringType(), True)
])

AB_TEST_REF_SCHEMA = StructType([
    StructField("customer_id", StringType(), True),
    StructField("is_target", StringType(), True)
])
