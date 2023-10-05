create table Restaurants (
    id BIGSERIAL NOT NULL PRIMARY KEY
);


create table Restaurant(
    restaurant_id BIGSERIAL NOT NULL PRIMARY KEY,
    restaurants_id BIGINT REFERENCES Restaurants(id)
);


create table Recipe(
    recipe_id BIGSERIAL NOT NULL PRIMARY KEY,
    restaurant_id BIGINT REFERENCES Restaurant(restaurant_id),
    instructions text NOT NULL
);


create table Supply(
    supply_id BIGSERIAL NOT NULL PRIMARY KEY,
    restaurant_id BIGINT REFERENCES Restaurant(restaurant_id),
    storage_location VARCHAR(20) NOT NULL,
    quantity INT,
    resupply BOOLEAN
);


create table Worker(
    username VARCHAR(70) NOT NULL PRIMARY KEY,
    restaurant_id BIGINT REFERENCES Restaurant(restaurant_id),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email TEXT,
    user_password TEXT NOT NULL
);


create table Shipment(
    tracking_number BIGINT NOT NULL PRIMARY KEY,
    restaurant_id BIGINT REFERENCES Restaurant(restaurant_id),
    expected TIMESTAMP,
    ordered TIMESTAMP NOT NULL,
    delivered TIMESTAMP
);


create table RecipeSupply (
    recipe_id BIGINT REFERENCES Recipe(recipe_id),
    supply_id BIGINT REFERENCES Supply(supply_id),
    amount REAL NOT NULL,
    PRIMARY KEY (recipe_id, supply_id)
);


create table ShipmentSupply(
    shipment_id BIGINT REFERENCES Shipment(tracking_number),
    supply_id BIGINT REFERENCES Supply(supply_id),
    quantity INT NOT NULL,
    PRIMARY KEY (shipment_id, supply_id)
);

