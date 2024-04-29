const Joke = require('../models/joke.model')

// Read All
// findAllJokes
module.exports.findAllJokes = (req, res) => {
    Joke.find()
        .then(allJokes => {
            console.log("All Jokes From DB", allJokes);
            res.json({ data: allJokes, message: 'All Jokes List', ok: true })
        })
        .catch(error => {
            console.log(error);
            res.json({ error })
        })
}

// findOneJoke
module.exports.findJokeById = (request, response) => {
    Joke.findOne({_id:request.params.id})
        .then(person => response.json(person))
        .catch(err => response.json(err))
}


// Create
module.exports.createNewJoke = (req, res) => {
    Joke.create(req.body)
        .then(newCreatedJoke => {
            console.log("New  Joke", newCreatedJoke);
            res.json({ data: newCreatedJoke, message: 'Joke Created with success', ok: true })
        })
        .catch(error => {
            console.log(error);
            res.json({ error })
        })
}
// Update

module.exports.updateJoke=(req,res)=>{
    Joke.findByIdAndUpdate({_id:req.params.id},req.body,{new:true,runValidators:true})
    .then(res=>{
        console.log('Update Jokes',res );
        res.json ({data: res,message: " joke updated with success",ok:true})
    })
    .catch(err=>{
        console.log(err);
        res.json({err})
    })
}

// Delete
module.exports.deleteJoke=(req,res)=>{
    Joke.findByIdAndDelete({_id:req.params.id})
    .then(res=>{
        res.json ({data: res,message: " joke delete with success",ok:true})
    })
    .catch(err=>{
        console.log(err);
        res.json({err})
    })
}

// deleteOneJoke