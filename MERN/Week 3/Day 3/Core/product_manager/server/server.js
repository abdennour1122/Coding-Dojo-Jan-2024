const express = require('express');
const app = express();
const cors = require("cors")
require("dotenv").config()


//middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cors())

const PORT = process.env.PORT
require("./config/config.mongoose")

const ProductsRoutes = require("./routes/product.route");
ProductsRoutes(app);



   
app.listen(PORT, () => console.log(`Listening on PORT: ${PORT}`) );