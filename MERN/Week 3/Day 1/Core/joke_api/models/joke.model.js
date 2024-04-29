const mongoose = require('mongoose')

const JokesSchema = new mongoose.Schema({
    setup:{
        type:String,
        required:[true, "setup is required !"],
        minlength:[3, 'setup length must be at least 3 🚫🚫🚫🚫']
    },
    punchline:{
        type:String,
        required:[true, "punchline is required !"],
        minlength:[5, 'punchline length must be at least 5 🚫🚫🚫🚫']
    }
    
},{timestamps:true})

const Joke = mongoose.model("Joke",JokesSchema)
module.exports = Joke;