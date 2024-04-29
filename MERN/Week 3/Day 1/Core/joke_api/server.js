const express = require('express');
require('dotenv').config()
const app = express()

// make sure these lines are above any app.get or app.post code blocks
app.use( express.json() );
app.use( express.urlencoded({ extended: true }) );

// connect to database
require('./config/mongoose.config')


// IMPORT ALL ROUTES
const routes = require('./routes/jokes.route')
routes(app)




app.listen(process.env.port,()=>{
    console.log('server is running  👍👍👍 port :',process.env.port)
})