const express = require("express");
const app = express();
const cors = require("cors");
require ("dotenv").config();
const port = process.env.PORT;




// === MIDDLEWARE === 
app.use(express.json(),express.urlencoded({extended:true}),cors());

// grab the config
require("./config/config.mongoose");



//  grab the routes 
require("./routes/author.route")(app);


app.listen(port,()=>{console.log("listening to port" ,port);
});